#!/usr/bin/env python3

import array
import sys

def gen(m = array):
    for i in dir(m):
        v = m.__dict__[i]
        if isinstance(v, int):
            print ("    assert %s.%s == %s" % (m.__name__, i, v))
            continue
        if v == None:
            print ("    assert %s.%s == %s" % (m.__name__, i, None))
            continue
        # print (i, type(m.__dict__[i]))

def array_00():
    assert array.typecodes == 'bBuhHiIlLqQfd'
    for tc in array.typecodes:
        assert array.array(tc).typecode == tc
    print ('array_00 ok')

# __add__
# __class__
# __contains__
# __copy__
# __deepcopy__
# __delattr__
# __delitem__
# __dir__
# __doc__
# __eq__
# __format__
# __ge__
# __getattribute__
# __getitem__
# __gt__
# __hash__
# __iadd__
# __imul__
# __init__
# __iter__
# __le__
# __len__
# __lt__
# __mul__
# __ne__
# __new__
# __reduce__
# __reduce_ex__
# __repr__
# __rmul__
# __setattr__
# __setitem__
# __sizeof__
# __str__
# __subclasshook__

# append
def array_01():
    a = array.array('B', b'abc')
    try:
        a.append(b'd')
    except TypeError:
        pass # an integer is required (got type bytes)
    else:
        assert False
    a.append(ord(b'd'))
    assert a == array.array('B', b'abcd')
    print ('array_01 ok')

# buffer_info
def array_02():
    a = array.array('B', b'a' * 100)
    address, length = a.buffer_info()
    assert length == 100

    a = array.array('H', [0] * 100)
    address, length = a.buffer_info()
    assert length == 100
    print ('array_02 ok')


# byteswap
# count
# extend
# frombytes
# fromfile
# fromlist
# fromstring
# fromunicode
# index
# insert
# itemsize
def array_03():
    assert sys.byteorder == 'little' # x86_64
    assert array.array('b', [70]).itemsize == 1
    assert array.array('B', [70]).itemsize == 1
    assert array.array('u', ['a']).itemsize == 4
    assert array.array('h', [70]).itemsize == 2
    assert array.array('H', [70]).itemsize == 2
    assert array.array('i', [70]).itemsize == 4
    assert array.array('I', [70]).itemsize == 4
    assert array.array('l', [70]).itemsize == 8
    assert array.array('L', [70]).itemsize == 8
    assert array.array('q', [70]).itemsize == 8
    assert array.array('Q', [70]).itemsize == 8
    assert array.array('f', [70]).itemsize == 4
    assert array.array('d', [70]).itemsize == 8
    print ('array_03 ok')

# pop
# remove
# reverse
# tobytes
# tofile
# tolist
# tostring
# tounicode
# typecode

def array_99():
    assert array.typecodes == 'bBuhHiIlLqQfd'
    for tc in array.typecodes:
        assert array.array(tc).typecode == tc
    print ('array_99 ok')

if __name__ == '__main__':
    array_01()
    array_02()
    array_03()
    array_99()

