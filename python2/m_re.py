#!/usr/bin/env python

import re
import sys

"""
Note: the testcases here have a lot of copy-and-paste code. For real
testsuites that is a nightmare, as it makes consistent updates
difficult. But here I have a different objective. I want each test
case to be simple and self-contained.
"""

def report(p,s,b=0):
    print '- - -  pattern  - - -'
    pat = re.compile(p)
    print 'flags', pat.flags
    print 'groupindex', pat.groupindex
    print 'groups', pat.groups
    print 'pattern', pat.pattern
    # methods
    print pat.match
    print pat.findall
    print pat.finditer
    print pat.scanner
    print pat.search
    print pat.split
    print pat.sub
    print pat.subn
    
    print '- - -  match  - - -'
    m = pat.match(s,b)
    print 'endpos', m.endpos
    print 'lastgroup', m.lastgroup
    print 'lastindex', m.lastindex
    print 'pos', m.pos
    print 're', m.re
    print 'regs', m.regs
    print 'string', m.string
    # methods
    print 'end', m.end()
    # print m.expand(template)
    print 'group', m.group()
    print 'groupdict', m.groupdict()
    print 'groups', m.groups()
    print 'span', m.span()
    print 'start', m.start()

def re_01():
    p = re.compile(r'abc')
    s = 'abcdefghi'
    m = p.match(s)
    assert m.string == s
    assert m.start() == 0
    assert m.end() == 3
    assert m.group() == 'abc'
    assert m.groupdict() == {}
    assert m.groups() == ()
    assert m.lastgroup == None
    assert m.lastindex == None
    assert m.pos == 0 and m.endpos == len(s)
    assert m.span() == (0, 3)
    print 're_01'

def re_02():
    p = re.compile(r'...')
    s = 'abcdefghi'
    m = p.match(s)
    assert m.string == s
    assert m.start() == 0
    assert m.end() == 3
    assert m.group() == 'abc'
    assert m.groupdict() == {}
    assert m.groups() == ()
    assert m.lastgroup == None
    assert m.lastindex == None
    assert m.pos == 0 and m.endpos == len(s)
    assert m.span() == (0, 3)
    print 're_02'

def re_03():
    p = re.compile(r'...')
    s = 'abcdefghi'
    m = p.match(s,4)  # start offset
    assert m.string == s
    assert m.start() == 4
    assert m.end() == 7
    assert m.group() == 'efg'
    assert m.groupdict() == {}
    assert m.groups() == ()
    assert m.lastgroup == None
    assert m.lastindex == None
    assert m.pos == 4 and m.endpos == len(s)
    assert m.span() == (4, 7)
    print 're_03'

def re_04():
    """Explictly match the start"""
    p = re.compile(r'^...')
    s = 'abcdefghi'
    m = p.match(s)
    assert m.string == s
    assert m.start() == 0
    assert m.end() == 3
    assert m.group() == 'abc'
    assert m.groupdict() == {}
    assert m.groups() == ()
    assert m.lastgroup == None
    assert m.lastindex == None
    assert m.pos == 0 and m.endpos == len(s)
    assert m.span() == (0, 3)
    print 're_04'

def re_05():
    """Group"""
    p = re.compile(r'(...)')
    s = 'abcdefghi'
    m = p.match(s)
    assert m.string == s
    assert m.start() == 0
    assert m.end() == 3
    assert m.group() == 'abc'
    assert m.groupdict() == {}
    assert m.groups() == ('abc',)
    assert m.lastgroup == None
    assert m.lastindex == 1
    assert m.pos == 0 and m.endpos == len(s)
    assert m.span() == (0, 3)
    print 're_05'

def re_06():
    """Nested group"""
    p = re.compile(r'(.(.).)')
    s = 'abcdefghi'
    m = p.match(s)
    assert m.string == s
    assert m.start() == 0
    assert m.end() == 3
    assert m.group() == 'abc'
    assert m.groupdict() == {}
    assert m.groups() == ('abc', 'b')
    assert m.lastgroup == None
    assert m.lastindex == 1
    assert m.pos == 0 and m.endpos == len(s)
    assert m.span() == (0, 3)
    print 're_06'

def re_07():
    """Two groups"""
    p = re.compile(r'(.).(.)')
    s = 'abcdefghi'
    m = p.match(s)
    assert m.string == s
    assert m.start() == 0
    assert m.end() == 3
    assert m.group() == 'abc'
    assert m.groupdict() == {}
    assert m.groups() == ('a', 'c')
    assert m.lastgroup == None
    assert m.lastindex == 2
    assert m.pos == 0 and m.endpos == len(s)
    assert m.span() == (0, 3)
    print 're_07'

def re_08():
    """Non-capturing group"""
    p = re.compile(r'(?:.).(.)')
    s = 'abcdefghi'
    m = p.match(s)
    assert m.string == s
    assert m.start() == 0
    assert m.end() == 3
    assert m.group() == 'abc'
    assert m.groupdict() == {}
    assert m.groups() == ('c',)
    assert m.lastgroup == None
    assert m.lastindex == 1
    assert m.pos == 0 and m.endpos == len(s)
    assert m.span() == (0, 3)
    print 're_08'

def re_09():
    """Named groups groups"""
    p = re.compile(r'(?P<first>.).(?P<second>.)')
    s = 'abcdefghi'
    m = p.match(s)
    assert m.string == s
    assert m.start() == 0
    assert m.end() == 3
    assert m.group() == 'abc'
    assert m.groupdict() == {'second': 'c', 'first': 'a'}
    assert m.groups() == ('a', 'c')
    assert m.lastgroup == 'second'
    assert m.lastindex == 2
    assert m.pos == 0 and m.endpos == len(s)
    assert m.span() == (0, 3)
    print 're_09'

def re_10():
    p = re.compile(r'.(?# this comment should be ignored)..')
    s = 'abcdefghi'
    m = p.match(s)
    assert m.string == s
    assert m.start() == 0
    assert m.end() == 3
    assert m.group() == 'abc'
    assert m.groupdict() == {}
    assert m.groups() == ()
    assert m.lastgroup == None
    assert m.lastindex == None
    assert m.pos == 0 and m.endpos == len(s)
    assert m.span() == (0, 3)
    print 're_10'

def re_11():
    """Choice"""
    p = re.compile(r'(a|z)..')
    s = 'abcdefghi'
    m = p.match(s)
    assert m.string == s
    assert m.start() == 0
    assert m.end() == 3
    assert m.group() == 'abc'
    assert m.groupdict() == {}
    assert m.groups() == ('a',)
    assert m.lastgroup == None
    assert m.lastindex == 1
    assert m.pos == 0 and m.endpos == len(s)
    assert m.span() == (0, 3)
    print 're_11'

def re_12():
    """Choice"""
    p = re.compile(r'(a|x)(a|b)(b|c)')
    s = 'abcdefghi'
    m = p.match(s)
    assert m.string == s
    assert m.start() == 0
    assert m.end() == 3
    assert m.group() == 'abc'
    assert m.groupdict() == {}
    assert m.groups() == ('a','b','c')
    assert m.lastgroup == None
    assert m.lastindex == 3
    assert m.pos == 0 and m.endpos == len(s)
    assert m.span() == (0, 3)
    print 're_12'

def re_13():
    """0 or more"""
    p = re.compile(r'.*')
    s = 'abcdefghi'
    m = p.match(s)
    assert m.string == s
    assert m.start() == 0
    assert m.end() == 9
    assert m.group() == 'abcdefghi'
    assert m.groupdict() == {}
    assert m.groups() == ()
    assert m.lastgroup == None
    assert m.lastindex == None
    assert m.pos == 0 and m.endpos == len(s)
    assert m.span() == (0, 9)
    print 're_13'

def re_14():
    """1 or more"""
    p = re.compile(r'.+')
    s = 'abcdefghi'
    m = p.match(s)
    assert m.string == s
    assert m.start() == 0
    assert m.end() == 9
    assert m.group() == 'abcdefghi'
    assert m.groupdict() == {}
    assert m.groups() == ()
    assert m.lastgroup == None
    assert m.lastindex == None
    assert m.pos == 0 and m.endpos == len(s)
    assert m.span() == (0, 9)
    print 're_14'


if __name__ == '__main__':
    re_01()
    re_02()
    re_03()
    re_04()
    re_05()
    re_06()
    re_07()
    re_08()
    re_09()
    re_10()
    re_11()
    re_12()
    re_13()
    re_14()
    print 'ok'

