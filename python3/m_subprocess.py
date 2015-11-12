#!/usr/bin/env python3

import subprocess
import sys
import types

# print (sys.version)
r = None

def subprocess_01():
    r = subprocess.run(['echo', 'a'])
    assert isinstance(r, subprocess.CompletedProcess)
    assert r.args == ['echo', 'a']
    assert isinstance(r.check_returncode, types.MethodType)
    assert r.returncode == 0
    assert r.stderr == None
    assert r.stdout == None
    print ('subprocess_01 ok')

def subprocess_02():
    # error:
    try:
        subprocess.run(['echo b'])
    except FileNotFoundError:
        pass
    else:
        assert(False)
    
    # no error:
    r = subprocess.run(['echo c'], shell=True)
    assert isinstance(r, subprocess.CompletedProcess)
    assert r.args == ['echo c']
    assert isinstance(r.check_returncode, types.MethodType)
    assert r.returncode == 0
    assert r.stderr == None
    assert r.stdout == None
    print ('subprocess_02 ok')

def subprocess_03():
    r = subprocess.run(['echo', 'd'], stdout=subprocess.PIPE)
    assert isinstance(r.stdout, type(b'a byte string'))
    assert r.stdout == b'd\n'
    
    r = subprocess.run(['echo e'], shell=True, stdout=subprocess.PIPE)
    assert isinstance(r.stdout, type(b'a byte string'))
    assert r.stdout == b'e\n'
    
    r = subprocess.run(['echo f >/dev/null'], shell=True, stdout=subprocess.PIPE)
    assert isinstance(r.stdout, type(b'a byte string'))
    assert r.stdout == b''
    
    r = subprocess.run(['echo g >/dev/stderr'], shell=True, stderr=subprocess.PIPE)
    assert isinstance(r.stderr, type(b'a byte string'))
    assert r.stderr == b'g\n'
    
    r = subprocess.run(['(echo hhh >/dev/stderr) 2>/dev/null'],
                       shell=True, stderr=subprocess.PIPE)
    assert isinstance(r.stderr, type(b'a byte string'))
    assert r.stderr == b''
    
    print ('subprocess_03 ok')
    
if r:
    print (r.args)
    print (r.check_returncode)
    print (r.returncode)
    print (r.stderr)
    print (r.stdout)

if __name__ == '__main__':
    subprocess_01()
    subprocess_02()
    subprocess_03()
    pass
