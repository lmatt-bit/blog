Title: 编译libtorrent rasterbar(linux下)
Date: 2010-03-26 19:20
Author: lmatt wang
Slug: bianyilibtorrent-rasterbar(linuxxia)

六维、晨光等ipv6的bt下载站只支持为数不多的client，仅支持utorrent,
k\*\*(名字忘记了，和KDE有些关系),
transmission(在linux上貌似没法下载，仅支持mac
os)。为了能在linux下下载电影，我只好用wine+utorrent来搞定（不想装k\*\*）。可是用的时间久了，总觉得有点什么。于是呢，我就想自己写个支持torrent协议的程序，再在上面添加上边下边播放（utorrent上一直没有，我觊觎这个功能很久了）的功能。在网上搜索了相关的一些资料，最后决定使用libtorrent
rasterbar（网上还有另外一个叫libtorrent的库，而且那个库仅支持linux）。libtorrent
rasterbar用到了boost的一些库，正好最近我也在学习boost。下面是libtorrent的编译过程。\

1.编译boost
-----------

这里我使用了boost.build来编译生成。

a.首先进入BOOST\_ROOT/tools/jam/src目录（BOOST\_ROOT为boost的根目录)，接着在命令行中运行./build.sh

b.将上一步所生成bin.XXX目录中的bjam拷贝到系统的path（如/usr/local/bin）中，这样以后就可以直接使用bjam这个命令。

c.切换到BOOST\_ROOT/tools/build/v2目录，修改user-config.jam（具体详细操作可以参看user-config.jam文件中的内容）内容。在user-config.jam中找到using
gcc这行，将前面的\#去掉。

d.进入BOOST\_ROOT目录，在命令行中运行bjam
stage。这个过程需要一段时间才能完成。完成后，BOOST\_ROOT目录下会出现一个stage的目录，里面包含了boost所生成的lib。\

2.编译libtorrent rasterbar
--------------------------

这里我使用了automake和auotconf来生成，所以需要首先确认机器上是否已安装automake和autoconf。

a.确保环境变量中有BOOST\_ROOT，即是boost的根目录。

b.进入libtorrent的根目录，在命令行下运行./configure --disable-debug --disable-encryption --without-zlib --prefix=\$HOME/libtorrent（其他具体参数可使用./configure --help来查看）。如果去掉--disable-encryption，需要确认你机器上安装有openssl。而--without-zlib是指不使用系统的zlib。--prefix是指libtorrent的安装目录（其实boost也是可以指定安装目录的，就是指其编译完后库文件的存放位置）。

c.输入make install即可完成编译。\

3.libtorrent rasterbar测试程序的编译运行
----------------------------------------

使用如下命令实现编译

g++ -I(boost的根目录) -I(libtorrent的include目录) -I(zlib的目录，在libtorrent的根目录下)
(boost的lib目录+\*.so) (libtorrent的lib目录+\*.so) xx.cpp

这里使用\*.so是用了共享的方式链接。

程序的运行需要确保，libtorrent的lib和boost的lib目录在系统搜索路径下。默认的搜索路径在/usr/lib，可以通过修改/etc/ld.so.conf来添加新的路径。添加完新的路径后，需要运行ldconfig命令以更新。
