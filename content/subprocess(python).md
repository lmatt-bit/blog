Title: subprocess(python)
Date: 2010-04-18 07:21
Author: lmatt wang
Slug: subprocess(python)

subprocess
是python在2.4版本之后引入的用于subprocess管理的module。subprocess中有一个重要的类Popen和一个重要的方法call。下面对Popen和call进行相关说明。

Popen用于新建一个subprocess，下面是它的构造函数。

*class* `subprocess.Popen`<big>(</big>*args*, *bufsize=0*,
*executable=None*, *stdin=None*, *stdout=None*, *stderr=None*,
*preexec\_fn=None*, *close\_fds=False*, *shell=False*, *cwd=None*,
*env=None*, *universal\_newlines=False*, *startupinfo=None*,
*creationflags=0*<big>)</big>

其中：

args是运行进程的命令行（与shell中输入的命令行一样）；

*bufsize*, if given, has the same meaning as the corresponding argument
to the built-in open() function: `0` means unbuffered, `1` means line
buffered, any other positive value means use a buffer of (approximately)
that size. A negative *bufsize* means to use the system default, which
usually means fully buffered. The default value for *bufsize* is `0`
(unbuffered).

The *executable* argument specifies the program to execute. It is very
seldom needed: Usually, the program to execute is defined by the *args*
argument. If `shell=True`, the *executable* argument specifies which
shell to use. On Unix, the default shell is `/bin/sh`. On Windows, the
default shell is specified by the **COMSPEC** environment variable. The
only reason you would need to specify `shell=True` on Windows is where
the command you wish to execute is actually built in to the shell, eg
`dir`, `copy`. You don’t need `shell=True` to run a batch file, nor to
run a console-based executable.

*stdin*, *stdout* and *stderr*
指定了subprocess的标准输入、输出和错误流。这些值可以是subprocess.PIPE，文件描叙符（file
descriptor），文件对象（file
object）和None。使用subprocess.PIPE，会新建一个pipe到子进程，通过这个pipe父子进程可以进行信息传递。stderr可以为subprocess.STDOUT，表示stderr和stdout使用同样的file
handle。

If *preexec\_fn* is set to a callable object, this object will be called
in the child process just before the child is executed. (Unix only)

If *close\_fds* is true, all file descriptors except `0`, `1` and `2`
will be closed before the child process is executed. (Unix only). Or, on
Windows, if *close\_fds* is true then no handles will be inherited by
the child process. Note that on Windows, you cannot set *close\_fds* to
true and also redirect the standard handles by setting *stdin*, *stdout*
or *stderr*.

If *shell* is
[`True`](http://docs.python.org/library/constants.html#True "True"), the
specified command will be executed through the shell.

If *cwd* is not `None`, the child’s current directory will be changed to
*cwd* before it is executed. Note that this directory is not considered
when searching the executable, so you can’t specify the program’s path
relative to *cwd*.

If *env* is not `None`, it must be a mapping that defines the
environment variables for the new process; these are used instead of
inheriting the current process’ environment, which is the default
behavior.

<div>

Note

If specified, *env* must provide any variables required for the program
to execute. On Windows, in order to run a [side-by-side
assembly](http://en.wikipedia.org/wiki/Side-by-Side_Assembly) the
specified *env* **must** include a valid **SystemRoot**.

</div>

If *universal\_newlines* is
[`True`](http://docs.python.org/library/constants.html#True "True"), the
file objects stdout and stderr are opened as text files, but lines may
be terminated by any of `'\n'`, the Unix end-of-line convention, `'\r'`,
the old Macintosh convention or `'\r\n'`, the Windows convention. All of
these external representations are seen as `'\n'` by the Python program.

<div>

Note

This feature is only available if Python is built with universal newline
support (the default). Also, the newlines attribute of the file objects
[`stdout`](http://docs.python.org/library/subprocess.html#subprocess.Popen.stdout "subprocess.Popen.stdout"),
[`stdin`](http://docs.python.org/library/subprocess.html#subprocess.Popen.stdin "subprocess.Popen.stdin")
and
[`stderr`](http://docs.python.org/library/subprocess.html#subprocess.Popen.stderr "subprocess.Popen.stderr")
are not updated by the communicate() method.

</div>

The *startupinfo* and *creationflags*, if given, will be passed to the
underlying CreateProcess() function. They can specify things such as
appearance of the main window and priority for the new process. (Windows
only)

**Example：**

[codesyntax lang="python" title="Example"]

    #! /usr/bin/python
    import subprocess
    import time

    if __name__ == '__main__':
     p = subprocess.Popen('./bt_download.out', stdin=subprocess.PIPE,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
     for i in range(0, 10):
            p.stdin.write('Info\n')
           print p.stdout.readline()
         time.sleep(5)
     p.stdin.write('Quit\n')
       print p.stdout.readline()
     time.sleep(5)

[/codesyntax]

上面的example通过subprocess，实现了父子进程的交流。需要注意的是，p.stdout.readline等操作都是阻塞操作。

call方法，同Popen的构造函数，其函数的declare如下：

`subprocess.call`<big>(</big>*\*popenargs*, *\*\*kwargs*<big>)</big>

其中openargs就是对应Popen中的args，kwargs就对Popen后面的一系列argument。

Example如下：

    retcode = subprocess.call(["ls", "-l"])
    它会等待ls命令执行完毕，retcode是子进程执行完的retcode。

