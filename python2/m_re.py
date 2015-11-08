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

def t01():
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

def t02():
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

def t03():
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

def t04():
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

def t05():
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

def t06():
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

def t07():
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

def t08():
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

def t09():
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

def t10():
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

def t11():
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

def t12():
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

def t13():
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

def t14():
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


if __name__ == '__main__':
    t01()
    t02()
    t03()
    t04()
    t05()
    t06()
    t07()
    t08()
    t09()
    t10()
    t11()
    t12()
    t13()
    t14()
    print 'ok'

