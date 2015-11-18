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

    print_hex(p)
    print 'struct_01'

def struct_02():
    print 'struct_02'

def examples():
    F = ">I"       # big-endian, unsigned 32 bit integer
    v0 = (130123,)
    p = pack(F,*v0)
    v1 = unpack(F,p)
    assert v0 == v1
    
    F = ">III"
    v0 = (130123,0,64)
    p = pack(F,*v0)
    v1 = unpack(F,p)
    assert v0 == v1
    
    F = ">20s" # 20 is the pad-to char count, which is not encoded.
    v0 = ("And so it begins ...",)
    assert len(v0[0]) == 20 # exact size prevents trailing nulls from unpack()
    p = pack(F,*v0)
    v1 = unpack(F,p)
    assert v0 == v1
    
    F = ">21s" # 20 is the pad-to char count, which is not encoded.
    v0 = ("And so it begins ...",)
    p = pack(F,*v0)
    assert len(p) == 21 # does NOT round-up to mod 4; no good for XDR.
    v1 = unpack(F,p)
    assert v0[0] + '\000' == v1[0]
    
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
