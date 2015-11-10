#!/usr/bin/env python

import multiprocessing as MP
import os
import sys
import time

# These first tests are cribbed from the python.org docs.

def test_process_01():

    def f(name):
        print 'hello', name
        
    p = MP.Process(target=f, args=('bob',))
    p.start()
    p.join()
    print 'test_process_01 ok'

def test_process_02():

    def info(title):
        # Called in 2 different processes
        print `title`
        print '  parent process = %s' % os.getppid()
        print '  process id = %s' % os.getpid()

    def f(name):
        info('function f')
        print 'hello', name

    info('main line')
    p = MP.Process(target=f, args=('bob',))
    p.start()
    p.join()
    print 'test_process_02 ok'

def test_process_03():

    def f(q):
        q.put([42, None, 'hello'])

    q = MP.Queue()
    p = MP.Process(target=f, args=(q,))
    p.start()
    assert q.get() == [42, None, 'hello']
    p.join()
    print 'test_process_03 ok'

def test_process_04():
    # Values on the pipe are automatically pickled/unpickled

    def f(pipe):
        pipe.send([42, None, 'hello'])
        pipe.close()
        
    # not duplex means parent_end can recv only and child_end can send only
    parent_end, child_end = MP.Pipe(duplex=False)
    p = MP.Process(target=f, args=(child_end,))
    p.start()
    assert parent_end.recv() == [42, None, 'hello']
    p.join()
    print 'test_process_04 ok'

def test_process_05():
    # TBD: scan trace for safety violations
    # Tricky example. I do a *not* acquire exclusive access to
    # stdout. Critical section output characters could still be
    # interleaved with other non-critial processes.
    def f(l, i):
        print "%2.2d  waiting" % i
        l.acquire()
        print "%2.2d  exclusive" % i
        l.release()
        print "%2.2d  release" % i

    lock = MP.Lock()
    for num in range(10):
        MP.Process(target=f, args=(lock, num)).start()
    print 'test_process_05 ok'

def test_process_06():

    def f(n):
        n.value = 3.1415927

    num = MP.Value('d', 0.0)
    p = MP.Process(target=f, args=(num,))
    p.start()
    p.join()
    assert num.value == 3.1415927
    print 'test_process_06 ok'

def test_process_07():

    def f(a):
        for i in range(len(a)):
            a[i] = -a[i]

    arr = MP.Array('i', range(10))
    p = MP.Process(target=f, args=(arr,))
    p.start()
    p.join()
    assert arr[:] == [0, -1, -2, -3, -4, -5, -6, -7, -8, -9] # why copy?
    print 'test_process_07 ok'

def test_process_08():

    def f(d, l):
        d[1] = '1'
        d['2'] = 2
        d[0.25] = None
        l.reverse()

    manager = MP.Manager()
    d = manager.dict()
    l = manager.list(range(10))
    p = MP.Process(target=f, args=(d, l))
    p.start()
    p.join()
    # d and l are not the same types as dict and list, but they can be
    # copied to such.
    assert d.copy() == {0.25: None, 1: '1', '2': 2}, d
    assert l[:] == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    print 'test_process_08 ok'

def f_for_test_process_09(x):
    return x*x

def test_process_09():
    pool = MP.Pool(processes=4)
    result = pool.apply_async(f_for_test_process_09, [10])
    val = result.get(timeout=1) # A race, but not likely to fail
    assert val == 100
    print 'test_process_09 ok'

def f_for_test_process_10(x):
    return x % 3

def test_process_10():
    pool = MP.Pool(processes=4)
    val = pool.map(f_for_test_process_10, range(10))
    assert val == [0, 1, 2, 0, 1, 2, 0, 1, 2, 0]
    print 'test_process_10 ok'

def test_process_11():
    """
    Barrier synchronization of two processes with a pipe.
    """
    
    def process_1(pipe):
        print "p1 1"
        print "p1 1"
        time.sleep(0.01)
        print "p1 1"
        pipe.send(''); pipe.recv() # 2
        print "p1 2"
        pipe.send(''); pipe.recv() # 3
        print "p1 3"
        time.sleep(0.02)
        print "p1 3"
        pipe.send(''); pipe.recv() # 4
        pipe.send(''); pipe.recv() # 5
        print "p1 5"
        time.sleep(0.03)
        print "p1 5"
        print "p1 5"
        pipe.close()

    def process_2(pipe):
        pipe.recv(); pipe.send('') # 2
        print "p2 2"
        time.sleep(0.04)
        print "p2 2"
        print "p2 2"
        pipe.recv(); pipe.send('') # 3
        time.sleep(0.02)
        print "p2 3"
        print "p2 3"
        pipe.recv(); pipe.send('') # 4
        print "p2 4"
        time.sleep(0.01)
        print "p2 4"
        pipe.recv(); pipe.send('') # 5
        print "p2 5"
        print "p2 5"
        pipe.close()
        
    p1, p2 = MP.Pipe()
    pr1 = MP.Process(target=process_1, args=(p1,))
    pr1.start()
    pr2 = MP.Process(target=process_2, args=(p2,))
    pr2.start()
    
    pr1.join()
    pr2.join()
    print 'test_process_11 ok'

def test_process_12(): # FAIL
    
    """ raise EOFError on closed pipe """
    
    def f(pipe):
        pipe.send('arbitrary value')
        pipe.close()
        time.sleep(1) # No help
        
    parent_end, child_end = MP.Pipe(duplex=False)
    p = MP.Process(target=f, args=(child_end,))
    p.start()
    assert parent_end.recv() == 'arbitrary value'
    print >>sys.stderr, 'checkpoint 1'
    try:
        parent_end.recv()  # Hangs
    except EOFError:
        pass
    print >>sys.stderr, 'checkpoint 2'
    p.join()
    print 'test_process_12 ok'

def test_process_13(N=3):
    """
    Barrier synchronization of N processes with a pipes and a helper.
    """
    def worker(i,pipe):
        sp = 0
        sp_ = pipe.recv()
        assert sp_ == sp, "fail %s %s" % (i,sp)
        print "%2.2d working after syncpoint %2.2d" % (i,sp)
        
        sp = 1
        pipe.send(sp)
        sp_ = pipe.recv()
        assert sp_ == sp, "fail %s %s" % (i,sp)
        print "%2.2d working after syncpoint %2.2d" % (i,sp)
        
        sp = 2
        pipe.send(sp)
        sp_ = pipe.recv()
        assert sp_ == sp, "fail %s %s" % (i,sp)
        print "%2.2d QUITING after syncpoint %2.2d" % (i,sp)
        
        pipe.close()
        
    def helper(plist):
        print 'checkpoint helper 0'
        sp = 0
        for pi in plist: pi.send(sp)
        print 'checkpoint helper 1'
        
        sp = 1
        for i,pi in enumerate(plist):
            assert pi.recv() == sp, 'fail sync %s' % i
        print 'checkpoint helper 2'
        for pi in plist:
            pi.send(sp)
        
        sp = 2
        for i,pi in enumerate(plist):
            assert pi.recv() == sp, 'fail sync %s' % i
        print 'checkpoint helper 3'
        for pi in plist:
            pi.send(sp)
        
        print 'checkpoint helper 4'
        for pi in plist:
            pi.close()
            
        print 'checkpoint helper 5 (end)'

    worker_list, helper_list = [], []
    for i in range(1, N+1):
        w, h = MP.Pipe()
        worker_list.append((i,w)) # pipes given to workers, 1 each
        helper_list.append(h) # pipe list for helper
    he = MP.Process(target=helper, args=(helper_list,))
    he.start()
    workers = []
    for pi in worker_list:
        wo = MP.Process(target=worker, args=(pi[0],pi[1]))
        wo.start()
        workers.append(wo)
    print 'checkpoint main 1'
    for wo in workers:
        wo.join()
    print 'checkpoint main 2'
    he.join()
    print 'test_process_13 ok'

if __name__ == '__main__':
    test_process_01()
    test_process_02()
    test_process_03()
    test_process_04()
    test_process_05()
    test_process_06()
    test_process_07()
    test_process_08()
    test_process_09()
    test_process_10()
    test_process_11()
    # 12 fails
    test_process_13()

