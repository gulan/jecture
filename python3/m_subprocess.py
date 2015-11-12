#!/usr/bin/env python3

import subprocess
import sys
import types

# print (sys.version)
r = None

def subprocess_00():
    assert isinstance(subprocess.getoutput, types.FunctionType)
    assert isinstance(subprocess.getstatusoutput, types.FunctionType)
    assert isinstance(subprocess.check_output, types.FunctionType)
    assert isinstance(subprocess.run, types.FunctionType)
    assert isinstance(subprocess.check_call, types.FunctionType)
    assert isinstance(subprocess.list2cmdline, types.FunctionType)
    assert isinstance(subprocess.call, types.FunctionType)
    assert subprocess.STDOUT == -2
    assert subprocess.PIPE == -1
    assert subprocess.DEVNULL == -3
    assert isinstance(subprocess.SubprocessError, type)
    assert isinstance(subprocess.TimeoutExpired, type)
    assert isinstance(subprocess.CalledProcessError, type)
    assert isinstance(subprocess.CompletedProcess, type)
    assert isinstance(subprocess.Popen, type)
    print ('subprocess_00 ok')

def subprocess_01():
    # simple run()
    r = subprocess.run(['echo', 'a'])
    assert isinstance(r, subprocess.CompletedProcess)
    assert r.args == ['echo', 'a']
    assert isinstance(r.check_returncode, types.MethodType)
    assert r.returncode == 0
    assert r.stderr == None
    assert r.stdout == None
    print ('subprocess_01 ok')

def subprocess_02():
    # error: 'echo b' is not the name of a program
    try:
        subprocess.run(['echo b'])
    except FileNotFoundError:
        pass
    else:
        assert(False)
    
    # ok: 'echo c' *is* valid shell input.
    r = subprocess.run(['echo c'], shell=True)
    assert isinstance(r, subprocess.CompletedProcess)
    assert r.args == ['echo c']
    assert isinstance(r.check_returncode, types.MethodType)
    assert r.returncode == 0
    assert r.stderr == None
    assert r.stdout == None
    print ('subprocess_02 ok')

def subprocess_03():
    # capture stdout 1
    r = subprocess.run(['echo', 'd'], stdout=subprocess.PIPE)
    assert isinstance(r.stdout, type(b'a byte string'))
    assert r.stdout == b'd\n'
    
    # capture stdout 2
    r = subprocess.run(['echo e'], shell=True, stdout=subprocess.PIPE)
    assert isinstance(r.stdout, type(b'a byte string'))
    assert r.stdout == b'e\n'
    
    # no stdout to capture
    r = subprocess.run(['echo f >/dev/null'], shell=True, stdout=subprocess.PIPE)
    assert isinstance(r.stdout, type(b'a byte string'))
    assert r.stdout == b''
    
    # capture stderr
    r = subprocess.run(['echo g >/dev/stderr'], shell=True, stderr=subprocess.PIPE)
    assert isinstance(r.stderr, type(b'a byte string'))
    assert r.stderr == b'g\n'
    
    # no stderr to capture
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
    subprocess_00()
    subprocess_01()
    subprocess_02()
    subprocess_03()
