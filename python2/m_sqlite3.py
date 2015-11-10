#!/usr/bin/env python

import sqlite3 as SQ
import sys

def test_exceptions():
    try:
        raise SQ.DatabaseError('err')
    except SQ.DatabaseError, e:
        assert e.message == 'err'
    
    try:
        raise SQ.DatabaseError('err',1,'two')
    except SQ.DatabaseError, e:
        assert e.args == ('err',1,'two')
    
    try:
        raise SQ.Warning('err')
    except SQ.Warning, e:
        assert e.message == 'err'
        assert e.args == ('err',)
    
    try:
        raise SQ.Error('err')
    except SQ.Error, e:
        assert e.message == 'err'
        assert e.args == ('err',)
    
    try:
        raise SQ.InterfaceError('err')
    except SQ.InterfaceError, e:
        assert e.message == 'err'
        assert e.args == ('err',)
    
    try:
        raise SQ.InternalError('err')
    except SQ.InternalError, e:
        assert e.message == 'err'
        assert e.args == ('err',)
    
    try:
        raise SQ.OperationalError('err')
    except SQ.OperationalError, e:
        assert e.message == 'err'
        assert e.args == ('err',)
    
    try:
        raise SQ.ProgrammingError('err')
    except SQ.ProgrammingError, e:
        assert e.message == 'err'
        assert e.args == ('err',)
    
    try:
        raise SQ.IntegrityError('err')
    except SQ.IntegrityError, e:
        assert e.message == 'err'
        assert e.args == ('err',)
    
    try:
        raise SQ.DataError('err')
    except SQ.DataError, e:
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
    
    print 'case 1'
    print >>sys.stderr, 'sqlite3.version=%s' % SQ.version
    print >>sys.stderr, 'sqlite3.sqlite_version=%s' % SQ.sqlite_version
    # Same data split-out into integer tuples:
    assert '.'.join(str(i) for i in SQ.version_info) == SQ.version
    assert ('.'.join(str(i) for i in SQ.sqlite_version_info)
            == SQ.sqlite_version)
    
    print 'case 2'
    cn = SQ.connect(':memory:')
    assert cn.isolation_level == ''
    assert cn.total_changes == 0
    cn.close()
    
    print 'case 3'
    cn = SQ.connect(':memory:',isolation_level='DEFERRED')
    assert cn.isolation_level == 'DEFERRED'
    cn.close()

    print 'case 4'
    cn = SQ.connect(':memory:',isolation_level='IMMEDIATE')
    assert cn.isolation_level == 'IMMEDIATE'
    # print list(cn.iterdump())
    cn.close()

    print 'case 5'
    cn = SQ.connect(':memory:',isolation_level='EXCLUSIVE')
    assert cn.isolation_level == 'EXCLUSIVE'
    # print list(cn.iterdump())
    cn.close()

    print 'case 6'
    cn = SQ.connect(':memory:')
    cn.close()
    try:
        cn.total_changes
    except SQ.ProgrammingError, e:
        pass
    else:
        assert 0
        
    print 'case 7'
    cn = SQ.connect(':memory:')
    cn.commit()
    assert cn.total_changes == 0
    cn.close()
    
    print 'case 8'
    cn = SQ.connect(':memory:')
    assert cn.commit() == None
    assert cn.close() == None
    
    print 'case 9'
    cn = SQ.connect(':memory:')
    c = cn.cursor()
    cn.commit()
    assert cn.total_changes == 0
    cn.close()
    
    print 'case 10'
    cn = SQ.connect(':memory:')
    c = cn.cursor()
    c.execute('create table ta(a integer not null)')
    assert cn.total_changes == 0
    cn.commit()
    assert cn.total_changes == 0
    cn.close()

    print 'case 11'
    cn = SQ.connect(':memory:')
    c = cn.cursor()
    c.execute('create table ta(a integer not null)')
    c.execute('insert into ta values (17)')
    assert cn.total_changes == 1
    cn.commit()
    assert cn.total_changes == 1
    cn.close()

    print 'case 12'
    cn = SQ.connect(':memory:')
    c = cn.cursor()
    c.execute('create table ta(a integer not null)')
    c.execute('insert into ta values (17)')
    assert cn.total_changes == 1
    cn.rollback()
    # unexpected:
    assert cn.total_changes == 1
    cn.close()

    print 'test_connect ok'

if __name__ == '__main__':
    test_exceptions()
    test_connect()

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
