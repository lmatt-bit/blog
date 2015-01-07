Title: 确保FileOutputStream将内容写入硬盘
Date: 2010-10-14 12:51
Author: lmatt wang
Slug: quebaoFileOutputStreamjiangneirongxieruyingpan

最近写了一个程序，需要在数据写入文件后立即读取该文件内容。这一简单的功能，却会时不时抛异常，令我十分不解。

原程序如下：\

> FileOutputStream os = new FileOutputStream("some\_file");\
> os.write(data);\
> os.close();
> </p>

在查了jdk中关于flush()函数的介绍后，发现了一些问题。flush只保证数据已交付给了操作系统，无法确定已写入硬盘。

以下是jdk中关于flush()函数的介绍：\

> Flushes this output stream and forces any buffered output bytes to be
> written out. The general contract of `flush` is that calling it is an
> indication that, if any bytes previously written have been buffered by
> the implementation of the output stream, such bytes should immediately
> be written to their intended destination.
> </p>

在查看了一些资料后，找到如下的解决方法。\

> //在flush();后加上下面代码\
> FileDescriptor fd = os.getFD();\
> fd.sync();//Force all system buffers to synchronize with the
> underlying device.
> </p>

