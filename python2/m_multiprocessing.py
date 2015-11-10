#!/usr/bin/env python

import multiprocessing as MP
import os

# These first tests are cribbed from the python.org docs.

def test_process_1():

    def f(name):
        print 'hello', name
        
    p = MP.Process(target=f, args=('bob',))
    p.start()
    p.join()
    print 'test_process_1 ok'

def test_process_2():

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
    print 'test_process_2 ok'

def test_process_3():

    def f(q):
        q.put([42, None, 'hello'])

    q = MP.Queue()
    p = MP.Process(target=f, args=(q,))
    p.start()
    assert q.get() == [42, None, 'hello']
    p.join()
    print 'test_process_3 ok'

def test_process_4():
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
    print 'test_process_4 ok'

def test_process_5():
    # TBD: scan trace for safety violations

    def f(l, i):
        print "%2.2d  waiting" % i
        l.acquire()
        print "%2.2d  exclusive" % i
        l.release()
        print "%2.2d  release" % i

    lock = MP.Lock()
    for num in range(10):
        MP.Process(target=f, args=(lock, num)).start()
    print 'test_process_5 ok'

def test_process_6():

    def f(n):
        n.value = 3.1415927

    num = MP.Value('d', 0.0)
    p = MP.Process(target=f, args=(num,))
    p.start()
    p.join()
    assert num.value == 3.1415927
    print 'test_process_6 ok'

def test_process_7():

    def f(a):
        for i in range(len(a)):
            a[i] = -a[i]

    arr = MP.Array('i', range(10))
    p = MP.Process(target=f, args=(arr,))
    p.start()
    p.join()
    assert arr[:] == [0, -1, -2, -3, -4, -5, -6, -7, -8, -9] # why copy?
    print 'test_process_7 ok'


if __name__ == '__main__':
    test_process_1()
    test_process_2()
    test_process_3()
    test_process_4()
    test_process_5()
    test_process_6()
    test_process_7()

