Title: gdb的基本使用（持续更新）
Date: 2010-04-23 03:11
Author: lmatt wang
Slug: gdbdejibenshiyongchixugengxin

> gcc -g test.c

通过-g参数，可以生成gdb所需要的debug信息。可能会生成一些只有gdb才能使用的debug信息，这对其他的debug程序会造成影响。要控制这些特殊的debug信息，可以通过-gstabs+, -gstabs, -gxcoff和-gvms参数。\

> gdb a.out
> </p>

通过上条命令，这会启动gdb。之后就可以对a.out进行debug了。

命令list(可以简写为字母"l")，列出代码。如果list后面没有参数，就是列出“上次列出代码”的后10行代码。"list -"，列出“上次列出代码”的前10行代码.
"list linenumber"列出linenumber附近的10行代码. "list
start,end"列出行号从start到end的代码。

命令break, 设置断点。break linenumber，在linenumber处设置断点。break
functionname，在函数functionname的入口处出设置断点。

命令run(可以简写为r），运行程序。

命令next（可以简写为n)，单步执行。

命令step（可以简写为s），单步执行，如果遇到函数，就进入函数内部。

命令continue（可以简写为c)，继续执行程序

命令print(可以简写为p)，打印参数的值

直接回车，重复执行上次命令。

命令quit（可以简写为q），退出gdb。
