#!/usr/bin/env python3

import subprocess
import sys
import types

# print (sys.version)
r = None

def subprocess_00():
    # Examine subprocess module
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
    # Simple run()
    r = subprocess.run(['echo', 'a'])
    assert isinstance(r, subprocess.CompletedProcess)
    assert r.args == ['echo', 'a']
    assert isinstance(r.check_returncode, types.MethodType)
    assert r.returncode == 0
    assert r.stderr == None
    assert r.stdout == None
    print ('subprocess_01 ok')

def subprocess_02():
    # Error: 'echo b' is not the name of a program
    try:
        subprocess.run(['echo b'])
    except FileNotFoundError:
        pass
    else:
        assert(False)
    
    # OK: 'echo c' *is* valid shell input.
    r = subprocess.run(['echo c'], shell=True)
    assert isinstance(r, subprocess.CompletedProcess)
    assert r.args == ['echo c']
    assert isinstance(r.check_returncode, types.MethodType)
    assert r.returncode == 0
    assert r.stderr == None
    assert r.stdout == None
    print ('subprocess_02 ok')

def subprocess_03():
    # Capture stdout 1
    r = subprocess.run(['echo', 'd'], stdout=subprocess.PIPE)
    assert isinstance(r.stdout, type(b'a byte string'))
    assert r.stdout == b'd\n'
    
    # Capture stdout 2
    r = subprocess.run(['echo e'], shell=True, stdout=subprocess.PIPE)
    assert isinstance(r.stdout, type(b'a byte string'))
    assert r.stdout == b'e\n'
    
    # No stdout to capture
    r = subprocess.run(['echo f >/dev/null'], shell=True, stdout=subprocess.PIPE)
    assert isinstance(r.stdout, type(b'a byte string'))
    assert r.stdout == b''
    
    # Capture stderr
    r = subprocess.run(['echo g >/dev/stderr'], shell=True, stderr=subprocess.PIPE)
    assert isinstance(r.stderr, type(b'a byte string'))
    assert r.stderr == b'g\n'
    
    # No stderr to capture
    r = subprocess.run(['(echo hhh >/dev/stderr) 2>/dev/null'],
                       shell=True, stderr=subprocess.PIPE)
    assert isinstance(r.stderr, type(b'a byte string'))
    assert r.stderr == b''
    
    print ('subprocess_03 ok')

def subprocess_04():
    # arglist and shell == True
    print ('subprocess_04 ok')
    
def subprocess_05():
    # How to use check_returncode()?
    print ('subprocess_05 ok')

def subprocess_10():
    # Popen arguments
    args = 'echo'
    p = subprocess.Popen(
        args,                    # sequence or string
        bufsize=-1,              # io.DEFAULT_BUFFER_SIZE
        # bufsize=0,             # unbuffered
        # bufsize=1,             # line buffered
        # bufsize=512,           # >1, approx. bufsize
        executable=None,            # use program implied by args and shell
        # executable=/usr/bin/bash  # if shell == True, use this instead of /bin/sh
        # executable=xxx            # if shell == False, run xxx but display args[0] in ps
        stdin=None,              # None | PIPE | DEVNULL | > 0 | file-object
        stdout=None,             # None | PIPE | DEVNULL | > 0 | file-object
        stderr=None,             # None | PIPE | STDOUT | DEVNULL | > 0 | file-object
        preexec_fn=None,         # Call before running the child
        close_fds=True,          # file descriptors > 2 before running child
        shell=False,             # bool. See run()
        cwd=None,
        env=None,
        universal_newlines=False,
        startupinfo=None,
        creationflags=0,
        restore_signals=True,
        start_new_session=False,
        pass_fds=()
    )
    assert isinstance(p.communicate, types.MethodType)
    assert isinstance(p.kill, types.MethodType)
    assert isinstance(p.send_signal, types.MethodType)
    assert isinstance(p.terminate, types.MethodType)
    assert isinstance(p.wait, types.MethodType)
    assert isinstance(p.poll, types.MethodType)

    assert p.args == args
    save_pid = p.pid
    assert p.returncode == None
    assert p.stdin == None
    assert p.stdout == None
    assert p.stderr == None
    assert p.universal_newlines == False
    
    stdout_data, stderr_data = p.communicate(input=None, timeout=None)

    assert p.args == args
    assert p.pid == save_pid
    assert p.returncode == 0
    assert p.stdin == None
    assert p.stdout == None
    assert p.stderr == None
    assert p.universal_newlines == False
    print ('subprocess_10 ok')

if __name__ == '__main__':
    subprocess_00()
    subprocess_01()
    subprocess_02()
    subprocess_03()
    subprocess_04()
    subprocess_05()
    subprocess_10()
