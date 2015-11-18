#!/usr/bin/env python3


# -- int --
# Python ints are objects with a class, but they do not support dot access.
# 2.__add__ is invalid
# int.__add__ is OK.

# int.__abs__
assert abs(1) == abs(-1) == 1
assert all(abs(abs(i)) == abs(i) for i in [-1,0,1]) # all integers
assert int.__abs__(-7) == 7

# int.__add__
assert 3 + 5 == 5 + 3 == 8
assert 1 + (2 + 3) == (1 + 2) + 3 == 6
assert int.__add__(3, 4) == 7

# int.__and__

# int.__bool__
assert bool(0) == False
assert bool(1) == True
assert bool(2) == True
assert bool(-1) == True
assert int.__bool__(0) == False

# int.__ceil__
assert all(int.__ceil__(i) == i for i in [-2,-1,0,1,2]) # all integers

# int.__class__
assert type(2) == int

# int.__delattr__
## ?

# int.__dir__
assert int.__dir__(2) # returns a long list

# int.__divmod__
def h(n,d):
    q,r = divmod(n,d)
    return q*d + r == n
assert all(h(n,d) for n in range(-5,5) for d in range(-5,5) if d != 0)
del h

# int.__doc__
assert type(int.__doc__) == str

# int.__eq__
assert 1 == 1
assert int.__eq__(2, 2)

# int.__float__
assert int.__float__(3) == 3

# int.__floor__
assert int.__floor__(-1) == -1
assert int.__floor__(0) == 0
assert int.__floor__(1) == 1

# int.__floordiv__

# int.__format__

# int.__ge__
assert 3 >= 2
assert int.__ge__(3,2)
assert int.__ge__(2,2)
assert not int.__ge__(2,3)

# int.__getattribute__
## int.__getattribute__(1,'__abs__') returns a method wrapper, while
## int.__abs__ returns a slot wrapper

# int.__getnewargs__

# int.__gt__
assert 3 > 2
assert int.__gt__(3,2)
assert not int.__gt__(2,2)
assert not int.__gt__(2,3)

# int.__hash__

# int.__index__

# int.__init__

# int.__int__
## not the same as int().

# int.__invert__
## ones complement, I think. Same as ~.

# int.__le__
assert 2 < 3
assert int.__le__(2,3)
assert int.__le__(2,2)
assert not int.__le__(3,2)

# int.__lshift__
# int.__lt__
assert 2 <= 3
assert int.__lt__(2,3)
assert not int.__lt__(2,2)
assert not int.__lt__(3,2)

# int.__mod__
assert -5 % -3 == -2 
assert 5 % 3 == 2 
assert 5 % -3 == -1
assert -5 % 3 == 1
assert int.__mod__(5, 3) == 2

# int.__mul__
assert 3 * 5 == 5 * 3 == 15
assert int.__mul__(5,3) == 15

# int.__ne__
assert 1 != 2
assert int.__ne__(1, 2)

# int.__neg__
# - is a prefix operator even with a numberic literal: -1.
assert -1 == 0 - 1
assert --1 == 1
assert ---1 == -1
assert int.__neg__(-1) == 1
assert int.__neg__(0) == 0
assert int.__neg__(1) == -1

# int.__new__

# int.__or__
assert 0 | 0 == 0
assert 1 | 0 == 1
assert 0 | 1 == 1
assert 1 | 1 == 1

assert 2 | 0 == 2
assert 0 | 2 == 2
assert 2 | 2 == 2

# int.__pos__
# identity function
assert +1 == 1 == ++1
assert +0 == 0 == -0
assert +(-1) == -1
assert int.__pos__(1) == 1

# int.__pow__
assert 2**3 == 8 == pow(2,3)
assert int.__pow__(2,3) == 8
assert int.__pow__(2,-3) == 0.125
assert int.__pow__(7,2,5) == 4 == 7**2 % 5 == pow(7,2,5)

# int.__radd__
# int.__rand__
# int.__rdivmod__
# int.__reduce__
# int.__reduce_ex__
# int.__repr__
# int.__rfloordiv__
# int.__rlshift__
# int.__rmod__
# int.__rmul__
# int.__ror__
# int.__round__
# int.__rpow__
# int.__rrshift__
# int.__rshift__
# int.__rsub__
# int.__rtruediv__
# int.__rxor__
# int.__setattr__
# int.__sizeof__
# int.__str__
# int.__sub__
# int.__subclasshook__
# int.__truediv__
# int.__trunc__
# int.__xor__
# int.bit_length
# int.conjugate
# int.denominator
# int.from_bytes
# int.imag
# int.numerator
# int.real
# int.to_bytes

##               - - -  str  - - -
# str.__add__
assert '' + '' == ''
assert 'abc' == '' + 'abc' == 'abc' + ''
assert ('a' + 'b') + 'c' == 'a' + 'b' + 'c' == 'a' + ('b' + 'c')
assert 'a' + 'b' != 'b' + 'a'
assert 'abc' + 'def' == 'abcdef'
assert str.__add__('abc','def') == 'abcdef'

# str.__class__
# str.__contains__
assert 'y' in 'xyz'
assert '' in 'xyz' # remember: `while len(s) > 0` not `while string != ''`
assert str.__contains__('xyz', 'x')
assert str.__contains__('xyz', '')

# str.__delattr__
# str.__dir__
# str.__doc__

# str.__eq__

# str.__format__
# str.__ge__
# str.__getattribute__
# str.__getitem__
# str.__getnewargs__
# str.__gt__
# str.__hash__
# str.__init__
# str.__iter__
# str.__le__
# str.__len__
# str.__lt__
# str.__mod__
# str.__mul__
# str.__ne__
# str.__new__
# str.__reduce__
# str.__reduce_ex__
# str.__repr__
# str.__rmod__
# str.__rmul__
# str.__setattr__
# str.__sizeof__
# str.__str__
# str.__subclasshook__
# str.capitalize
# str.casefold
# str.center
# str.count
# str.encode
# str.endswith
# str.expandtabs
# str.find
# str.format
# str.format_map
# str.index
# str.isalnum
# str.isalpha
# str.isdecimal
# str.isdigit
# str.isidentifier
# str.islower
# str.isnumeric
# str.isprintable
# str.isspace
# str.istitle
# str.isupper
# str.join
# str.ljust
# str.lower
# str.lstrip
# str.maketrans
# str.partition
# str.replace
# str.rfind
# str.rindex
# str.rjust
# str.rpartition
# str.rsplit
# str.rstrip
# str.split
# str.splitlines
# str.startswith
# str.strip
# str.swapcase
# str.title
# str.translate
# str.upper
# str.zfill
