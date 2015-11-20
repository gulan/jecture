#!/usr/bin/env python

import string
import sys

def string_01():
    assert string.ascii_lowercase == 'abcdefghijklmnopqrstuvwxyz'
    assert string.ascii_uppercase == 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    assert string.digits == '0123456789'
    assert string.hexdigits == '0123456789abcdefABCDEF'
    assert string.octdigits == '01234567'
    assert string.punctuation == '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    assert string.whitespace == '\t\n\x0b\x0c\r '
    assert string.ascii_letters == string.ascii_lowercase + string.ascii_uppercase
    assert string.ascii_letters == string.ascii_lowercase + string.ascii_uppercase
    print 'string_01 ok'

# TBD: locale dependent
def string_02():
    assert string.lowercase == 'abcdefghijklmnopqrstuvwxyz'
    assert string.uppercase == 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    assert string.letters == string.lowercase + string.uppercase
    print 'string_02 ok'
    
# Format
def string_03():
    assert '{0}, {1}, {2}'.format('a', 'b', 'c') == 'a, b, c'
    if sys.version_info.major == 2 and sys.version_info.minor > 6:
        assert '{}, {}, {}'.format('a', 'b', 'c') == 'a, b, c'
    assert '{2}, {1}, {0}'.format('a', 'b', 'c') == 'c, b, a'
    assert '{2}, {1}, {0}'.format(*'abc') == 'c, b, a'
    assert '{0}{1}{0}'.format('abra', 'cad') == 'abracadabra'
    # ... much more
    print 'string_03 ok'

# Functions
def string_03():
    assert string.capwords('a quick brown fox') == 'A Quick Brown Fox'
    assert string.capwords('a Quick brown Fox') == 'A Quick Brown Fox'
    assert string.capwords('a quicK browN fox') == 'A Quick Brown Fox'
    # odd results:
    assert string.capwords('a quick-brown fox') == 'A Quick-brown Fox'
    assert string.capwords('a quick-brown-fox', '-') == 'A quick-Brown-Fox'
    assert string.capwords('a quick brown-fox', '-') == 'A quick brown-Fox'
    print 'string_01 ok'

# Template

# The following functions are depreciated in favor of string methods.
# string.atof(s)
# string.atoi(s[, base])
# string.atol(s[, base])
# string.capitalize(word)
# string.expandtabs(s[, tabsize])
# string.find(s, sub[, start[, end]])
# string.rfind(s, sub[, start[, end]])
# string.index(s, sub[, start[, end]])
# string.rindex(s, sub[, start[, end]])
# string.count(s, sub[, start[, end]])
# string.lower(s)
# string.split(s[, sep[, maxsplit]])
# string.rsplit(s[, sep[, maxsplit]])
# string.splitfields(s[, sep[, maxsplit]])
# string.join(words[, sep])
# string.joinfields(words[, sep])
# string.lstrip(s[, chars])
# string.rstrip(s[, chars])
# string.strip(s[, chars])
# string.swapcase(s)
# string.translate(s, table[, deletechars])
# string.upper(s)
# string.ljust(s, width[, fillchar])
# string.rjust(s, width[, fillchar])
# string.center(s, width[, fillchar])
# string.zfill(s, width)
# string.replace(s, old, new[, maxreplace])

if __name__ == '__main__':
    string_01()
    string_02()
    string_03()
