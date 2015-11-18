#!/usr/bin/env python

import struct
from struct import *
import sys

def print_hex(string, N=8):
    def dot_fill(x):
        return x  +  '.' * (N - len(x))
    def gen():
        c = ''.join((" %s" % ch if ord(ch) > 32 else '--') for ch in string)
        h = ''.join("%.2x" % ord(ch) for ch in string)
        while len(h) > N:
            hhead, h = h[:N], h[N:]
            chead, c = c[:N], c[N:]
            yield (chead, hhead)
        if h:
            yield (c, dot_fill(h))
    pair_list = list(gen())
    chars = ' '.join(ch for (ch, _) in pair_list)
    hexs = ' '.join(x for (_, x) in pair_list)
    print chars
    print hexs

def struct_01():
    assert sys.byteorder == 'little'
    # c - character / byte
    p = pack('c', 'A')
    assert unpack('c', p)[0] == 'A'
    
    p = pack('ccc', 'A', 'B', 'C')
    assert p == 'ABC'
    assert unpack('ccc', p) == ('A', 'B', 'C')
    
    # The x adds a null byte
    p = pack('cxcc', 'A', 'B', 'C')
    assert p == 'A\x00BC'
    assert unpack('cxcc', p) == ('A', 'B', 'C')
    
    # b - signed character (integer)
    p = pack('b', ord('A'))
    assert unpack('b', p)[0] == ord('A')
    
    p = pack('b', 127) # Maximum allowed even though it packs in to 4 bytes
    assert unpack('b', p)[0] == 127
    
    p = pack('bbbb', 65, 66, 67, 68) # Fills 4 bytes
    assert unpack('bbbb', p) == (65, 66, 67, 68)

    p = pack('b', -128)
    assert unpack('b', p)[0] == -128
    
    # B - unsigned char
    p = pack('B', 255)
    assert unpack('B', p)[0] == 255
    
    p = pack('B', 0)
    assert unpack('B', p)[0] == 0
    
    p = pack('BBBB', 165, 166, 167, 168) # Fills 4 bytes
    assert unpack('BBBB', p) == (165, 166, 167, 168)
    
    try:
        p = pack('B', -1)
    except struct.error:
        pass  # Must greater than 0
    else:
        assert False

    # ? - boolean
    p = pack('?', 0)
    assert unpack('?', p)[0] == 0

    p = pack('?', True)
    assert unpack('?', p)[0] == True

    # H - unsigned short
    p = pack('H', 0xffff)
    assert unpack('H', p)[0] == 0xffff

    try:
        p = pack('H', 0x1ffff)
    except struct.error:
        pass  # too big
    else:
        assert False

    try:
        p = pack('H', -1)
    except struct.error:
        pass  # cannot be negative
    else:
        assert False

    # h - signed short
    p = pack('h', -1)
    assert unpack('h', p)[0] == -1

    p = pack('h', 0x7fff)
    assert unpack('h', p)[0] == 0x7fff
    
    try:
        p = pack('h', 0x8fff)
    except struct.error:
        pass  # too big
    else:
        assert False

    # i - signed int
    p = pack('i', -1)
    assert unpack('i', p)[0] == -1

    p = pack('i', 0x7fffffff)
    assert unpack('i', p)[0] == 0x7fffffff
    
    try:
        p = pack('i', 0x8fffffff)
    except struct.error:
        pass  # too big
    else:
        assert False

    # I - unsigned int
    p = pack('I', 0xffffffff)
    assert unpack('I', p)[0] == 0xffffffff

    try:
        p = pack('I', 0x1ffffffff)
    except struct.error:
        pass  # too big
    else:
        assert False

    try:
        p = pack('I', -1)
    except struct.error:
        pass  # cannot be negative
    else:
        assert False

    # L - unsigned long
    p = pack('L', 0xffffffffffffffff)
    assert unpack('L', p)[0] == 0xffffffffffffffff

    # l - signed long
    p = pack('l', 0x7fffffffffffffff)
    assert unpack('l', p)[0] == 0x7fffffffffffffff

    p = pack('l', -1)
    assert unpack('l', p)[0] == -1

    # Q - unsigned long long (same as L)
    p = pack('Q', 0xffffffffffffffff)
    assert unpack('Q', p)[0] == 0xffffffffffffffff

    # f - float
    p = pack('f', 1.234)
    q = unpack('f', p)[0] # Because float conversions are approximate
    p = pack('f', q)
    assert unpack('f', p)[0] == q

    # d - double
    p = pack('d', 1.234)
    q = unpack('d', p)[0] # Because float conversions are approximate
    p = pack('d', q)
    assert unpack('d', p)[0] == q
    
    print 'struct_01 ok'

def struct_02():
    # s - string
    F = "20s" # 20 is the pad-to char count, which is not encoded.
    v0 = ("And so it begins ...",)
    assert len(v0[0]) == 20 # exact size prevents trailing nulls in unpack()
    p = pack(F, *v0)
    v1 = unpack(F, p)
    assert v0 == v1
    
    # Declared length longer than actual length.
    dlen = 21 # declared string len
    alen = 20 # actual string len
    F = "%ss" % dlen
    v0 = ("And so it begins ...",)
    assert len(v0[0]) == alen
    p = pack(F, *v0)
    v1 = unpack(F, p)
    # The string is padded with nulls on the end to declared length.
    # There are no extra nulls for alignment
    padding = '\000' * (dlen - alen)
    assert v0[0] + padding == v1[0]
    
    # Declared length shorter than actual length.
    dlen = 10 # declared string len
    alen = 20 # actual string len
    F = "%ss" % dlen
    v0 = ("And so it begins ...",)
    assert len(v0[0]) == alen
    p = pack(F, *v0)
    v1 = unpack(F, p)
    # The string is truncated to declared length.
    assert v0[0][:dlen] == v1[0]
    
    # Declared length of 0 truncates the whole string.
    dlen = 0 # declared string len
    alen = 20 # actual string len
    F = "%ss" % dlen
    v0 = ("And so it begins ...",)
    assert len(v0[0]) == alen
    p = pack(F, *v0)
    v1 = unpack(F, p)
    # The string is truncated to declared length (0).
    assert v1[0] == ''
    
    # The default declared length is 1.
    alen = 20 # actual string len
    F = "s"
    v0 = ("And so it begins ...",)
    assert len(v0[0]) == alen
    p = pack(F, *v0)
    v1 = unpack(F, p)
    # The string is truncated to declared length (1).
    assert v0[0][:1] == v1[0]
    
    print_hex(p)
    print 'struct_02 ok'

def examples():
    F = ">21p" # 21 is the pad-to char count, which IS encoded.
    v0 = ("And so it begins ...",)
    p = pack(F,*v0)
    assert len(p) == 1+20 # len encoded in one byte; no good for XDR
    # The one byte encoded char count contributes to the packed length.
    # Hence, 21 to pack a string of length 20.
    v1 = unpack(F,p)
    assert v0 == v1

if __name__ == '__main__':
    struct_01()
    struct_02()
