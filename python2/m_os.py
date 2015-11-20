#!/usr/bin/env python

import os
import pwd
import signal
import socket
import sys
import time
import types

def os_01():
    assert os.EX_CANTCREAT == 73
    assert os.EX_CONFIG == 78
    assert os.EX_DATAERR == 65
    assert os.EX_IOERR == 74
    assert os.EX_NOHOST == 68
    assert os.EX_NOINPUT == 66
    assert os.EX_NOPERM == 77
    assert os.EX_NOUSER == 67
    assert os.EX_OK == 0
    assert os.EX_OSERR == 71
    assert os.EX_OSFILE == 72
    assert os.EX_PROTOCOL == 76
    assert os.EX_SOFTWARE == 70
    assert os.EX_TEMPFAIL == 75
    assert os.EX_UNAVAILABLE == 69
    assert os.EX_USAGE == 64
    assert os.F_OK == 0
    assert os.NGROUPS_MAX == 65536
    assert os.O_APPEND == 1024
    assert os.O_ASYNC == 8192
    assert os.O_CREAT == 64
    assert os.O_DIRECT == 16384
    assert os.O_DIRECTORY == 65536
    assert os.O_DSYNC == 4096
    assert os.O_EXCL == 128
    assert os.O_LARGEFILE == 0
    assert os.O_NDELAY == 2048
    assert os.O_NOATIME == 262144
    assert os.O_NOCTTY == 256
    assert os.O_NOFOLLOW == 131072
    assert os.O_NONBLOCK == 2048
    assert os.O_RDONLY == 0
    assert os.O_RDWR == 2
    assert os.O_RSYNC == 1052672
    assert os.O_SYNC == 1052672
    assert os.O_TRUNC == 512
    assert os.O_WRONLY == 1
    assert os.P_NOWAIT == 1
    assert os.P_NOWAITO == 1
    assert os.P_WAIT == 0
    assert os.R_OK == 4
    assert os.SEEK_CUR == 1
    assert os.SEEK_END == 2
    assert os.SEEK_SET == 0
    assert os.ST_APPEND == 256
    assert os.ST_MANDLOCK == 64
    assert os.ST_NOATIME == 1024
    assert os.ST_NODEV == 4
    assert os.ST_NODIRATIME == 2048
    assert os.ST_NOEXEC == 8
    assert os.ST_NOSUID == 2
    assert os.ST_RDONLY == 1
    assert os.ST_RELATIME == 4096
    assert os.ST_SYNCHRONOUS == 16
    assert os.ST_WRITE == 128
    assert os.TMP_MAX == 238328
    assert os.WCONTINUED == 8
    assert os.WNOHANG == 1
    assert os.WUNTRACED == 2
    assert os.W_OK == 2
    assert os.X_OK == 1
    assert os.altsep == None
    assert os.curdir == '.'
    assert os.defpath == ':/bin:/usr/bin'
    assert os.devnull == '/dev/null'
    assert os.extsep == '.'
    assert os.linesep == '\n'
    assert os.name == 'posix'
    assert os.pardir == '..'
    assert os.pathsep == ':'
    assert os.sep == '/'
    assert isinstance(os.WSTOPSIG, types.BuiltinMethodType)
    assert isinstance(os.WTERMSIG, types.BuiltinMethodType)
    assert isinstance(os.WCOREDUMP, types.BuiltinMethodType)
    assert isinstance(os.WEXITSTATUS, types.BuiltinMethodType)
    assert isinstance(os.WIFCONTINUED, types.BuiltinMethodType)
    assert isinstance(os.WIFEXITED, types.BuiltinMethodType)
    assert isinstance(os.WIFSIGNALED, types.BuiltinMethodType)
    assert isinstance(os.WIFSTOPPED, types.BuiltinMethodType)
    assert isinstance(os.abort, types.BuiltinMethodType)
    assert isinstance(os.access, types.BuiltinMethodType)
    assert isinstance(os.chdir, types.BuiltinMethodType)
    assert isinstance(os.chmod, types.BuiltinMethodType)
    assert isinstance(os.chown, types.BuiltinMethodType)
    assert isinstance(os.chroot, types.BuiltinMethodType)
    assert isinstance(os.close, types.BuiltinMethodType)
    assert isinstance(os.closerange, types.BuiltinMethodType)
    assert isinstance(os.confstr, types.BuiltinMethodType)
    assert isinstance(os.confstr_names, dict)
    assert isinstance(os.ctermid, types.BuiltinMethodType)
    assert isinstance(os.dup, types.BuiltinMethodType)
    assert isinstance(os.dup2, types.BuiltinMethodType)
    assert isinstance(os.environ, types.InstanceType)
    assert isinstance(os.error, type)
    assert isinstance(os.execl, types.FunctionType)
    assert isinstance(os.execle, types.FunctionType)
    assert isinstance(os.execlp, types.FunctionType)
    assert isinstance(os.execlpe, types.FunctionType)
    assert isinstance(os.execv, types.BuiltinMethodType)
    assert isinstance(os.execve, types.BuiltinMethodType)
    assert isinstance(os.execvp, types.FunctionType)
    assert isinstance(os.execvpe, types.FunctionType)
    assert isinstance(os.fchdir, types.BuiltinMethodType)
    assert isinstance(os.fchmod, types.BuiltinMethodType)
    assert isinstance(os.fchown, types.BuiltinMethodType)
    assert isinstance(os.fdatasync, types.BuiltinMethodType)
    assert isinstance(os.fdopen, types.BuiltinMethodType)
    assert isinstance(os.fork, types.BuiltinMethodType)
    assert isinstance(os.forkpty, types.BuiltinMethodType)
    assert isinstance(os.fpathconf, types.BuiltinMethodType)
    assert isinstance(os.fstat, types.BuiltinMethodType)
    assert isinstance(os.fstatvfs, types.BuiltinMethodType)
    assert isinstance(os.fsync, types.BuiltinMethodType)
    assert isinstance(os.ftruncate, types.BuiltinMethodType)
    assert isinstance(os.getcwd, types.BuiltinMethodType)
    assert isinstance(os.getcwdu, types.BuiltinMethodType)
    assert isinstance(os.getegid, types.BuiltinMethodType)
    assert isinstance(os.getenv, types.FunctionType)
    assert isinstance(os.geteuid, types.BuiltinMethodType)
    assert isinstance(os.getgid, types.BuiltinMethodType)
    assert isinstance(os.getgroups, types.BuiltinMethodType)
    assert isinstance(os.getloadavg, types.BuiltinMethodType)
    assert isinstance(os.getlogin, types.BuiltinMethodType)
    assert isinstance(os.getpgid, types.BuiltinMethodType)
    assert isinstance(os.getpgrp, types.BuiltinMethodType)
    assert isinstance(os.getpid, types.BuiltinMethodType)
    assert isinstance(os.getppid, types.BuiltinMethodType)
    assert isinstance(os.getresgid, types.BuiltinMethodType)
    assert isinstance(os.getresuid, types.BuiltinMethodType)
    assert isinstance(os.getsid, types.BuiltinMethodType)
    assert isinstance(os.getuid, types.BuiltinMethodType)
    assert isinstance(os.initgroups, types.BuiltinMethodType)
    assert isinstance(os.isatty, types.BuiltinMethodType)
    assert isinstance(os.kill, types.BuiltinMethodType)
    assert isinstance(os.killpg, types.BuiltinMethodType)
    assert isinstance(os.lchown, types.BuiltinMethodType)
    assert isinstance(os.link, types.BuiltinMethodType)
    assert isinstance(os.listdir, types.BuiltinMethodType)
    assert isinstance(os.lseek, types.BuiltinMethodType)
    assert isinstance(os.lstat, types.BuiltinMethodType)
    assert isinstance(os.major, types.BuiltinMethodType)
    assert isinstance(os.makedev, types.BuiltinMethodType)
    assert isinstance(os.makedirs, types.FunctionType)
    assert isinstance(os.minor, types.BuiltinMethodType)
    assert isinstance(os.mkdir, types.BuiltinMethodType)
    assert isinstance(os.mkfifo, types.BuiltinMethodType)
    assert isinstance(os.mknod, types.BuiltinMethodType)
    assert isinstance(os.nice, types.BuiltinMethodType)
    assert isinstance(os.open, types.BuiltinMethodType)
    assert isinstance(os.openpty, types.BuiltinMethodType)
    assert isinstance(os.pathconf, types.BuiltinMethodType)
    assert isinstance(os.pathconf_names, dict)
    assert isinstance(os.pipe, types.BuiltinMethodType)
    assert isinstance(os.popen, types.BuiltinMethodType)
    assert isinstance(os.popen2, types.FunctionType)
    assert isinstance(os.popen3, types.FunctionType)
    assert isinstance(os.popen4, types.FunctionType)
    assert isinstance(os.putenv, types.BuiltinMethodType)
    assert isinstance(os.read, types.BuiltinMethodType)
    assert isinstance(os.readlink, types.BuiltinMethodType)
    assert isinstance(os.remove, types.BuiltinMethodType)
    assert isinstance(os.removedirs, types.FunctionType)
    assert isinstance(os.rename, types.BuiltinMethodType)
    assert isinstance(os.renames, types.FunctionType)
    assert isinstance(os.rmdir, types.BuiltinMethodType)
    assert isinstance(os.setegid, types.BuiltinMethodType)
    assert isinstance(os.seteuid, types.BuiltinMethodType)
    assert isinstance(os.setgid, types.BuiltinMethodType)
    assert isinstance(os.setgroups, types.BuiltinMethodType)
    assert isinstance(os.setpgid, types.BuiltinMethodType)
    assert isinstance(os.setpgrp, types.BuiltinMethodType)
    assert isinstance(os.setregid, types.BuiltinMethodType)
    assert isinstance(os.setresgid, types.BuiltinMethodType)
    assert isinstance(os.setresuid, types.BuiltinMethodType)
    assert isinstance(os.setreuid, types.BuiltinMethodType)
    assert isinstance(os.setsid, types.BuiltinMethodType)
    assert isinstance(os.setuid, types.BuiltinMethodType)
    assert isinstance(os.spawnl, types.FunctionType)
    assert isinstance(os.spawnle, types.FunctionType)
    assert isinstance(os.spawnlp, types.FunctionType)
    assert isinstance(os.spawnlpe, types.FunctionType)
    assert isinstance(os.spawnv, types.FunctionType)
    assert isinstance(os.spawnve, types.FunctionType)
    assert isinstance(os.spawnvp, types.FunctionType)
    assert isinstance(os.spawnvpe, types.FunctionType)
    assert isinstance(os.stat, types.BuiltinMethodType)
    assert isinstance(os.stat_float_times, types.BuiltinMethodType)
    assert isinstance(os.stat_result, type)
    assert isinstance(os.statvfs, types.BuiltinMethodType)
    assert isinstance(os.statvfs_result, type)
    assert isinstance(os.strerror, types.BuiltinMethodType)
    assert isinstance(os.symlink, types.BuiltinMethodType)
    assert isinstance(os.sysconf, types.BuiltinMethodType)
    assert isinstance(os.sysconf_names, dict)
    assert isinstance(os.system, types.BuiltinMethodType)
    assert isinstance(os.tcgetpgrp, types.BuiltinMethodType)
    assert isinstance(os.tcsetpgrp, types.BuiltinMethodType)
    assert isinstance(os.tempnam, types.BuiltinMethodType)
    assert isinstance(os.times, types.BuiltinMethodType)
    assert isinstance(os.tmpfile, types.BuiltinMethodType)
    assert isinstance(os.tmpnam, types.BuiltinMethodType)
    assert isinstance(os.ttyname, types.BuiltinMethodType)
    assert isinstance(os.umask, types.BuiltinMethodType)
    assert isinstance(os.uname, types.BuiltinMethodType)
    assert isinstance(os.unlink, types.BuiltinMethodType)
    assert isinstance(os.unsetenv, types.BuiltinMethodType)
    assert isinstance(os.urandom, types.BuiltinMethodType)
    assert isinstance(os.utime, types.BuiltinMethodType)
    assert isinstance(os.wait, types.BuiltinMethodType)
    assert isinstance(os.wait3, types.BuiltinMethodType)
    assert isinstance(os.wait4, types.BuiltinMethodType)
    assert isinstance(os.waitpid, types.BuiltinMethodType)
    assert isinstance(os.walk, types.FunctionType)
    assert isinstance(os.write, types.BuiltinMethodType)

    print 'os_01 ok'

def os_02():
    # TBD: write pid to file, confirm.
    pid = os.fork()
    if pid == 0:
        # print 'child %s' % os.getpid()
        os._exit(0)
    else:
        # print 'parent %s' % os.getpid()
        pass
    print 'os_02 ok'

def os_03():
    chpid = os.fork()
    if chpid == 0:
        os._exit(0)
    else:
        try:
            (pid, status) = os.waitpid(chpid,0)
        except OSError, e:
            print >>sys.stderr, 'unexpected error on wait()'
            raise
        # pid < -1   some child of process group abs(pip)
        # pid == -1  some child of mine
        # pid == 0   some child in my process group
        # pid > 1    my child
        assert pid > 0
        assert os.WCOREDUMP(status) == False
        assert os.WIFCONTINUED(status) == False
        assert os.WIFSTOPPED(status) == False
        assert os.WIFSIGNALED(status) == False
        assert os.WIFEXITED(status) == True
        assert os.WEXITSTATUS(status) == 0
    print 'os_03 ok'

def os_04():
    chpid = os.fork()
    if chpid == 0:
        os._exit(1)
    else:
        (pid, status) = os.waitpid(chpid,0)
        assert pid > 0
        assert os.WCOREDUMP(status) == False
        assert os.WIFCONTINUED(status) == False
        assert os.WIFSTOPPED(status) == False
        assert os.WIFSIGNALED(status) == False
        assert os.WIFEXITED(status) == True
        assert os.WEXITSTATUS(status) == 1
    print 'os_04 ok'

def os_05():
    chpid = os.fork()
    if chpid == 0:
        time.sleep(0)
        os._exit(0)
    else:
        (pid, status) = os.waitpid(chpid,0)
        assert pid > 0
        assert os.WCOREDUMP(status) == False
        assert os.WIFCONTINUED(status) == False
        assert os.WIFSTOPPED(status) == False
        assert os.WIFSIGNALED(status) == False
        assert os.WIFEXITED(status) == True
        assert os.WEXITSTATUS(status) == 0
    print 'os_05 ok'

def os_06():
    chpid = os.fork()
    if chpid == 0:
        time.sleep(1)
        os._exit(0)
    else:
        os.kill(chpid, signal.SIGTERM)
        (pid, status) = os.waitpid(chpid,0)
        assert pid > 0
        assert os.WCOREDUMP(status) == False
        assert os.WIFCONTINUED(status) == False
        assert os.WIFSTOPPED(status) == False
        assert os.WIFSIGNALED(status) == True
        assert os.WIFEXITED(status) == False
        assert os.WEXITSTATUS(status) == 0
        # print os.WSTOPSIG(status)
        assert os.WTERMSIG(status) == signal.SIGTERM
    print 'os_06 ok'

def os_07():
    chpid = os.fork()
    if chpid == 0:
        time.sleep(0.1)
        os._exit(0)
    else:
        os.kill(chpid, signal.SIGSTOP)
        os.kill(chpid, signal.SIGCONT)
        (pid, status) = os.waitpid(chpid,0)
        assert pid > 0
        assert os.WCOREDUMP(status) == False
        assert os.WIFCONTINUED(status) == False
        assert os.WIFSTOPPED(status) == False
        assert os.WIFSIGNALED(status) == False
        assert os.WIFEXITED(status) == True
        assert os.WEXITSTATUS(status) == 0
        # print os.WSTOPSIG(status)
        assert os.WTERMSIG(status) == 0
    print 'os_07 ok'

def os_08():
    # TBD: setuid
    os.getlogin() == 'gulan'
    pwd.getpwuid(os.getuid()) == 'gulan'
    # Note: os.environ is an dict-like instance of _Environ.
    os.environ['USER'] == 'gulan'
    os.environ['LOGNAME'] == 'gulan'
    print 'os_08 ok'

def os_09():
    os.name == 'posix' # 'nt', 'os2', 'ce', 'java', 'riscos'
    print 'os_09 ok'
    
def os_10():
    # status = os.system('echo hello-os05 >/dev/null')
    status = os.system('sleep 0.1')
    assert os.WCOREDUMP(status) == False
    assert os.WIFCONTINUED(status) == False
    assert os.WIFSTOPPED(status) == False
    assert os.WIFSIGNALED(status) == False
    assert os.WIFEXITED(status) == True
    assert os.WEXITSTATUS(status) == 0

    status = os.system('exit 0')
    assert os.WCOREDUMP(status) == False
    assert os.WIFCONTINUED(status) == False
    assert os.WIFSTOPPED(status) == False
    assert os.WIFSIGNALED(status) == False
    assert os.WIFEXITED(status) == True
    assert os.WEXITSTATUS(status) == 0
    
    status = os.system('exit 1')
    assert os.WCOREDUMP(status) == False
    assert os.WIFCONTINUED(status) == False
    assert os.WIFSTOPPED(status) == False
    assert os.WIFSIGNALED(status) == False
    assert os.WIFEXITED(status) == True
    assert os.WEXITSTATUS(status) == 1
    
    os.WSTOPSIG    #  types.BuiltinMethodType)
    os.WTERMSIG    #  types.BuiltinMethodType)
    os.WCOREDUMP    #  types.BuiltinMethodType)
        #  types.BuiltinMethodType)
    print 'os_10 ok'

def os_11():
    # For my system and locale:
    assert os.strerror(1) == 'Operation not permitted'
    assert os.strerror(2) == 'No such file or directory'
    assert os.strerror(3) == 'No such process'
    print 'os_11 ok'

def os_12():
    m = os.umask(0)             # set
    assert os.umask(m) == 0     # restore
    assert os.umask(123) == m   # set
    assert os.umask(m) == 123   # restore
    print 'os_12 ok'

def os_13():
    (sysname, nodename, release, version, machine) = os.uname()
    assert sysname == 'Linux'
    # print nodename
    # print release
    # print version
    assert machine == 'x86_64'
    (m, mlist, addrs) = socket.gethostbyaddr(socket.gethostname())
    assert m == nodename
    print 'os_13 ok'

def os_14():
    fd = os.open('os_14', os.O_WRONLY | os.O_CREAT)
    rec = '<000><001><002><003><004><005><006><007><008><009>'
    m = len(rec)
    n = os.write(fd, rec)
    while m - n:
        n += os.write(fd, rec[n:])
    os.close(fd)
    
    fd = os.open('os_14', os.O_RDONLY)
    data = ''
    r = os.read(fd, 11)
    while r != '':
        data += r
        r = os.read(fd, 11)
        
    os.close(fd)
    os.unlink('os_14')
    assert data == rec
    print 'os_14 ok'

def os_15():
    fd = os.open('os_15', os.O_WRONLY | os.O_CREAT)
    fh = os.fdopen(fd, 'w')
    rec = '<000><001><002><003><004><005><006><007><008><009>'
    fh.write(rec)
    fh.close()
    try:                     # The file is completely closed.
        os.write(fd, rec)
    except OSError, e:
        assert e.errno == 9  # Bad file descriptor
    else:
        assert 0
    os.unlink('os_15')
    print 'os_15 ok'

def os_16():
    rec = '<000><001><002><003><004><005><006><007><008><009>'
    assert len(rec) == 50
    
    def write_data(fname):
        fd = os.open(fname, os.O_WRONLY | os.O_CREAT)
        m = len(rec)
        n = os.write(fd, rec)
        while m - n:
            n += os.write(fd, rec[n:])
        os.close(fd)
    
    write_data('os_16')
    # Open the same file twice.
    fd1 = os.open('os_16', os.O_RDONLY)
    fd2 = os.open('os_16', os.O_RDONLY)
    data1 = os.read(fd1, 25)
    data2 = os.read(fd2, 25)        
    os.close(fd2)
    os.close(fd1)
    os.unlink('os_16')
    assert data1 == rec[:25]
    assert data2 == rec[:25]  # offset not shared
    print 'os_16 ok'

def os_17():
    rec = '<000><001><002><003><004><005><006><007><008><009>'
    assert len(rec) == 50
    
    def write_data(fname):
        fd = os.open(fname, os.O_WRONLY | os.O_CREAT)
        m = len(rec)
        n = os.write(fd, rec)
        while m - n:
            n += os.write(fd, rec[n:])
        os.close(fd)
    
    write_data('os_17')
    # Dup the opened file
    fd1 = os.open('os_17', os.O_RDONLY)
    fd2 = os.dup(fd1)
    data1 = os.read(fd1, 25)
    data2 = os.read(fd2, 25)        
    os.close(fd2)
    os.close(fd1)
    os.unlink('os_17')
    assert data1 == rec[:25]
    assert data2 == rec[25:]  # offset *is* shared
    print 'os_17 ok'

def os_18():
    rec = '<000><001><002><003><004><005><006><007><008><009>'
    assert len(rec) == 50
    
    def write_data(fname):
        fd = os.open(fname, os.O_WRONLY | os.O_CREAT)
        m = len(rec)
        n = os.write(fd, rec)
        while m - n > 0:
            n += os.write(fd, rec[n:])
        os.close(fd)
    
    write_data('os_18')
    fd = os.open('os_18', os.O_RDONLY)
    assert os.SEEK_SET == 0
    assert os.SEEK_CUR == 1
    assert os.SEEK_END == 2
    # Advance pos to 25.
    assert os.lseek(fd, 25, os.SEEK_SET) == 25
    # Now there are 25 more bytes to read.
    data = os.read(fd, 25)
    os.close(fd)
    os.unlink('os_18')
    assert data == rec[25:]
    print 'os_18 ok'

def os_19():
    rec = '<000><001><002><003><004><005><006><007><008><009>'
    assert len(rec) == 50
    fname = 'os_19'
    
    fd = os.open(fname, os.O_WRONLY | os.O_CREAT)
    m = len(rec)
    n = os.write(fd, rec)
    while m - n > 0:
        n += os.write(fd, rec[n:])
    os.ftruncate(fd, 40) # Drop the last 10 bytes
    os.close(fd)
    
    fd = os.open('os_19', os.O_RDONLY)
    data = os.read(fd, 100)
    os.close(fd)
    os.unlink('os_19')
    assert data == rec[:40]

    # ftruncate can also extend the file with holes, but it does not
    # change the read/write position.
    
    N = 10
    fd = os.open(fname, os.O_WRONLY | os.O_CREAT)
    os.ftruncate(fd, N) # This is pointless because of the lseek
    os.lseek(fd, N, 0)
    m = len(rec)
    n = os.write(fd, rec)
    while m - n > 0:
        n += os.write(fd, rec[n:])
    os.close(fd)
    
    fd = os.open('os_19', os.O_RDONLY)
    data = os.read(fd, max(N*2,100))
    os.close(fd)
    os.unlink('os_19')
    
    assert len(data) == len(rec) + N
    assert data[:N] == '\000' * N
    assert data[N:] == rec
    print 'os_19 ok'

def os_20(): print 'os_20 ok'
def os_21(): print 'os_21 ok'
def os_22(): print 'os_22 ok'
def os_23(): print 'os_23 ok'
def os_24(): print 'os_24 ok'
def os_25(): print 'os_25 ok'
def os_26(): print 'os_26 ok'
def os_27(): print 'os_27 ok'
def os_28(): print 'os_28 ok'
def os_29(): print 'os_29 ok'


if __name__ == '__main__':
    os_01()
    os_02()
    os_03()
    os_04()
    os_05()
    os_06()
    os_07()
    os_08()
    os_09()
    os_10()
    os_11()
    os_12()
    os_13()
    os_14()
    os_15()
    os_16()
    os_17()
    os_18()
    os_19()
