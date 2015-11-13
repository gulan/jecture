#!/usr/bin/env python

import os
import sys
import types

def gen():
    for i in dir(os):
        if i[0] == '_':
            continue
        t = repr(type(os.__dict__[i]))
        if t == "<type 'module'>":
            continue
        elif t == "<type 'builtin_function_or_method'>":
            print '    assert isinstance(os.%s, types.BuiltinMethodType)' % i
        elif t == "<type 'function'>":
            print '    assert isinstance(os.%s, types.FunctionType)' % i
        elif t == "<type 'instance'>":
            print '    assert isinstance(os.%s, types.InstanceType)' % i
        elif t == "<type 'type'>":
            print '    assert isinstance(os.%s, type)' % i
        elif t == "<type 'dict'>":
            print '    assert isinstance(os.%s, dict)' % i
        elif t == "<type 'NoneType'>":
            print '    print os.%s' % i
        elif t == "<type 'str'>":
            print '    print os.%s' % i
        elif t == "<type 'int'>":
            print '    print os.%s' % i
        else:
            print 'X', t

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
    rc = os.fork()
    if rc == 0:
        print 'child %s' % os.getpid()
        os._exit(0)
    else:
        print 'parent %s' % os.getpid()
    print 'os_02 ok'
    

if __name__ == '__main__':
    os_01()
    os_02()
