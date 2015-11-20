#!/usr/bin/env python

import multiprocessing
import sqlite3
import sys
import time

def test_exceptions():
    try:
        raise sqlite3.DatabaseError('err')
    except sqlite3.DatabaseError, e:
        assert e.message == 'err'
    
    try:
        raise sqlite3.DatabaseError('err',1,'two')
    except sqlite3.DatabaseError, e:
        assert e.args == ('err',1,'two')
    
    try:
        raise sqlite3.Warning('err')
    except sqlite3.Warning, e:
        assert e.message == 'err'
        assert e.args == ('err',)
    
    try:
        raise sqlite3.Error('err')
    except sqlite3.Error, e:
        assert e.message == 'err'
        assert e.args == ('err',)
    
    try:
        raise sqlite3.InterfaceError('err')
    except sqlite3.InterfaceError, e:
        assert e.message == 'err'
        assert e.args == ('err',)
    
    try:
        raise sqlite3.InternalError('err')
    except sqlite3.InternalError, e:
        assert e.message == 'err'
        assert e.args == ('err',)
    
    try:
        raise sqlite3.OperationalError('err')
    except sqlite3.OperationalError, e:
        assert e.message == 'err'
        assert e.args == ('err',)
    
    try:
        raise sqlite3.ProgrammingError('err')
    except sqlite3.ProgrammingError, e:
        assert e.message == 'err'
        assert e.args == ('err',)
    
    try:
        raise sqlite3.IntegrityError('err')
    except sqlite3.IntegrityError, e:
        assert e.message == 'err'
        assert e.args == ('err',)
    
    try:
        raise sqlite3.DataError('err')
    except sqlite3.DataError, e:
        assert e.message == 'err'
        assert e.args == ('err',)
        
    print 'test_exceptions ok'

def test_connect():
    """
    close
    commit
    create_aggregate
    create_collation
    create_function
    cursor
    enable_load_extension
    execute
    executemany
    executescript
    interrupt
    isolation_level
    iterdump
    load_extension
    rollback
    row_factory
    set_authorizer
    set_progress_handler
    text_factory
    total_changes
    """
    
    # print 'case 1'
    # These number-strings are in the form 12.34.56
    # print >>sys.stderr, 'sqlite3.version=%s' % sqlite3.version
    # print >>sys.stderr, 'sqlite3.sqlite_version=%s' % sqlite3.sqlite_version
    # Same data split-out into integer tuples:
    assert '.'.join(str(i) for i in sqlite3.version_info) == sqlite3.version
    assert ('.'.join(str(i) for i in sqlite3.sqlite_version_info)
            == sqlite3.sqlite_version)
    
    # print 'case 2'
    cn = sqlite3.connect(':memory:')
    assert cn.isolation_level == ''
    assert cn.total_changes == 0
    cn.close()
    
    # print 'case 3'
    cn = sqlite3.connect(':memory:',isolation_level='DEFERRED')
    assert cn.isolation_level == 'DEFERRED'
    cn.close()

    # print 'case 4'
    cn = sqlite3.connect(':memory:',isolation_level='IMMEDIATE')
    assert cn.isolation_level == 'IMMEDIATE'
    # print list(cn.iterdump())
    cn.close()

    # print 'case 5'
    cn = sqlite3.connect(':memory:',isolation_level='EXCLUSIVE')
    assert cn.isolation_level == 'EXCLUSIVE'
    # print list(cn.iterdump())
    cn.close()

    # print 'case 6'
    # Do not use a connection object after it has been closed
    cn = sqlite3.connect(':memory:')
    cn.close()
    try:
        cn.total_changes
    except sqlite3.ProgrammingError, e:
        pass
    else:
        assert 0
        
    # print 'case 7'
    cn = sqlite3.connect(':memory:')
    cn.commit()
    assert cn.total_changes == 0
    cn.close()
    
    # print 'case 8'
    cn = sqlite3.connect(':memory:')
    assert cn.commit() == None
    assert cn.close() == None
    
    # print 'case 9'
    cn = sqlite3.connect(':memory:')
    c = cn.cursor()
    cn.commit()
    assert cn.total_changes == 0
    cn.close()
    
    # print 'case 10'
    cn = sqlite3.connect(':memory:')
    c = cn.cursor()
    c.execute('create table ta(a integer not null)')
    assert cn.total_changes == 0
    cn.commit()
    assert cn.total_changes == 0
    cn.close()

    # print 'case 11'
    cn = sqlite3.connect(':memory:')
    c = cn.cursor()
    c.execute('create table ta(a integer not null)')
    c.execute('insert into ta values (17)')
    assert cn.total_changes == 1
    cn.commit()
    assert cn.total_changes == 1
    cn.close()

    # print 'case 12'
    cn = sqlite3.connect(':memory:')
    c = cn.cursor()
    c.execute('create table ta(a integer not null)')
    c.execute('insert into ta values (17)')
    assert cn.total_changes == 1
    cn.rollback()
    # Unexpected:
    assert cn.total_changes == 1
    cn.close()
    print 'test_connect ok'

def sqlite_11():
    """
    There is no explict commit. This will create a persistent table,
    but the inserts are never committed.
    """
    cx = sqlite3.connect('counters.db')
    c = cx.cursor()
    c.execute('drop table if exists test_11;')
    c.execute('create table test_11 (value integer);')
    c.execute('insert into test_11 values (1);')
    c.execute('select value from test_11')
    assert c.fetchone()[0] == 1
    cx.close()
    print 'sqlite_11 ok'

def sqlite_12():
    """
    Create a new table, and commit a value. On a fresh connection,
    verify that the value persists.
    """
    cx = sqlite3.connect('counters.db')
    c = cx.cursor()
    c.execute('drop table if exists test_12;')
    c.execute('create table test_12 (value integer);')
    c.execute('insert into test_12 values (1);')
    c.execute('select value from test_12')
    assert c.fetchone()[0] == 1
    cx.commit()
    cx.close()
    
    cx = sqlite3.connect('counters.db')
    c = cx.cursor()
    c.execute('select value from test_12')
    assert c.fetchone()[0] == 1
    cx.close()
    print 'sqlite_12 ok'

def sqlite_13():
    """
    1. Create a new table, and commit a value.
    2. On a new connection, increment the value and commit.
    3. On another new connection, verify the increment persists.
    """
    cx = sqlite3.connect('counters.db')
    c = cx.cursor()
    c.execute('drop table if exists test_13;')
    c.execute('create table test_13 (value integer);')
    c.execute('insert into test_13 values (1);')
    cx.commit()
    cx.close()
    
    cx = sqlite3.connect('counters.db')
    c = cx.cursor()
    c.execute('update test_13 set value = (select value from test_13) + 1;')
    cx.commit()
    cx.close()
    
    cx = sqlite3.connect('counters.db')
    c = cx.cursor()
    c.execute('select value from test_13;')
    assert c.fetchone()[0] == 2
    cx.close()
    print 'sqlite_13 ok'

def sqlite_14():
    """
    In process A,
      1. Create a new table, and commit a value.

    In Process B,
      2. Wait for process A to commit
      3. Query and verify the value
    """

    def A(pipe):
        # print "A 1"
        cx = sqlite3.connect('counters.db')
        c = cx.cursor()
        c.execute('drop table if exists test_14;')
        c.execute('create table test_14 (value integer);')
        c.execute('insert into test_14 values (1);')
        cx.commit()
        cx.close()
        pipe.send(''); pipe.recv() # sync point
        # print "A 2"
        pipe.close()
        # print "A 3"

    def B(pipe):
        # print "B 1"
        pipe.recv(); pipe.send('') # sync point
        # print "B 2"
        cx = sqlite3.connect('counters.db')
        c = cx.cursor()
        c.execute('select value from test_14;')
        assert c.fetchone()[0] == 1
        cx.close()
        pipe.close()
        # print "B 3"
        
    # print "M 1"
    p1, p2 = multiprocessing.Pipe()
    procA = multiprocessing.Process(target=A, args=(p1,))
    procA.start()
    # print "M 2"
    procB = multiprocessing.Process(target=B, args=(p2,))
    procB.start()
    # print "M 3"
    
    procA.join()
    # print "M 4"
    procB.join()
    print 'sqlite_14 ok'

# def sqlite_15(): FAIL. sqlite3 module has limitations. Switching to apsw.
#     """
#     In process Main,
#       1. Create a new table, and commit a value.

#     In Process A and B,
#       1. Select the last inserted row
#       2. Wait awhile
#       3. Increment the value and insert a new row

#     The values of the rows must be seen as successive increments.
#     """
    
#     def AB(pid):
#         for _ in range(10):
#             cx = sqlite3.connect('counters.db')
#             # isolation_level = 'IMMEDIATE')
#             isolation_level = None
#             c = cx.cursor()
#             c.execute('begin;')
#             c.execute('select value, max(seq) from test_15;')
#             value = c.fetchone()[0]
#             time.sleep(0.01)
#             value += 1
#             try:
#                 c.execute('insert into test_15 (value) values (?);', (value,))
#                 c.execute('commit;')
#                 print 'value %s commmited by process %s' % (value, pid)
#             except sqlite3.OperationalError:
#                 # c.execute('rollback;')
#                 print 'process %s abandoned %s' % (pid, value)
#             # cx.commit()
#             cx.close()

#     print "M 1"
#     cx = sqlite3.connect('counters.db')
#     c = cx.cursor()
#     c.execute('drop table if exists test_15;')
#     c.execute('create table test_15 (seq integer primary key autoincrement, value integer);')
#     c.execute('insert into test_15 (value) values (1);')
#     cx.commit()
#     cx.close()

#     procA = multiprocessing.Process(target=AB, args=(1,))
#     procA.start()
#     print "M 2"
#     procB = multiprocessing.Process(target=AB, args=(2,))
#     procB.start()
#     print "M 3"
    
#     procA.join()
#     print "M 4"
#     procB.join()
#     print 'sqlite_15 ok'

if __name__ == '__main__':
    test_exceptions()
    test_connect()
    sqlite_11()
    sqlite_12()
    sqlite_13()
    sqlite_14()

# arraysize
# close
# connection
# description
# execute
# executemany
# executescript
# fetchall
# fetchmany
# fetchone
# lastrowid
# next
# row_factory
# rowcount
# setinputsizes
# setoutputsize
