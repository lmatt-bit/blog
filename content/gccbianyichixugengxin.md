Title: gcc编译（持续更新）
Date: 2010-03-25 17:21
Author: lmatt wang
Slug: gccbianyichixugengxin

gcc -I[path] 后接include目录

gcc -L[path] 后接library目录,一般会与-l(L小写)[library
name（如libabc.a,名称就为abc）]连用。

gcc -static 静态链接。可能会产生"cannot
find -lm"错误，这是由于缺少glibc-static的原因（fedora系统上就可能存在这个问题）。安装上glibc-static后，/usr/lib/目录下会出现libm.a这个文件。

gcc -o[out name] 接输出文件的名称

gcc -w                inhibit all warning message
(不允许出现任何warning消息) ［东哥］

gcc -Wall            打开部分的warning的flag,这部分flag所对应的
warning可能是用户避免或觉得有问题的。

gcc -Wextra（或旧版-W)      打开-Wall剩下的部分flag

gcc -g test.c

通过-g参数，可以生成gdb所需要的debug信息。可能会生成一些只有gdb才能使用的debug信息，这对其他的debug程序会造成影响。要控制这些特殊的debug信息，可以通过-gstabs+, -gstabs, -gxcoff和-gvms参数。
