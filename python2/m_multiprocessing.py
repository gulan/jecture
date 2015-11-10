#!/usr/bin/env python

import multiprocessing as MP
import os
import sys

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

