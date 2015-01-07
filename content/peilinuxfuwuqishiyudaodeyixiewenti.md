Title: 配linux服务器时遇到的一些问题
Date: 2010-03-12 16:26
Author: lmatt wang
Slug: peilinuxfuwuqishiyudaodeyixiewenti

**1.硬盘安装**

有很长一段时间没有安装过linux了，所以对硬盘安装有些忘记。

这里对硬盘安装的一些步骤进行下记录。首先需要安装上grub，这里提下grub4dos的安装，xp系统(vista和win
7还不清楚)都可以通过修改boot.ini来引导grub。进入grub后，输入以下命令即可引导linux安装。命令中的vmlinuz和initrd.img都是从光盘映像中拷出来的，有可能名字不一样（这与不同版本的linux有关）。vmlinuz和initrd.img一般建议放在根目录下，这样可以方便知道分区的编号（命令中的“（hd0,0)”）。可以通过“find
/ vmlinuz”命令来获得，需要注意中间的空格。

[codesyntax lang="bash" lines="no"]

    kernel (hd0,0)/vmlinuz
    initrd (hd0,0)/initrd.img
    boot

[/codesyntax]

硬盘安装还需要注意的是映像所存放的文件系统。ntfs可能会使映像无法找到，最好使用fat32或linux的文件系统。

**2.opensuse liveUSB安装**

这次安装linux，本来打算是安装centos的，因为之前对centos进行过lamp的安装（参考[centos
pub](http://www.centospub.com/)）。可是后来硬盘安装centos时出现了问题，以致电脑无法启动。当时在实验室，手头只有u盘，只好用u盘来安装。在网上搜了些教程后，决定选择opensuse(因为它最简单)来安装。下面内容截取自[opensuse
wiki上liveUSB](http://cn.opensuse.org/index.php?title=LiveUSB&diff=prev&oldid=3791)的安装方法。

1\) 找到您的 USB 驱动盘被识别的方式:

``` {style="padding-left: 30px;"}
 linux-vgqb:~ # ls -l /dev/disk/by-id/*usb*
```

该命令将会输出如下结果:

``` {style="padding-left: 30px;"}
lrwxrwxrwx 1 root root 9 13. Aug 10:04 /dev/disk/by-id/usb-Kingston_DataTraveler_II+_5B751D8C1994-0:0 -> ../../sdb
```

在此 */dev/sdb* 是命令行中的简称，通常，直接使用 */dev/disk/by-id/..*
以防止写错硬盘导致数据丢失。

2\) 将 LiveCD iso 写入 usb stick, 请注意将这里举例的 /dev/sdb
用您自己的具体硬盘设备代替（上面命令输出的设备信息）:

``` {style="padding-left: 30px;"}
dd if=openSUSE-KDE4-LiveCD-x86_64-Build0219-Media.iso of=/dev/sdb bs=4M
```

**3. lamp的安装**

装上opensuse后，网上搜了下lamp的安装方法，结果意外找到一个不错的网站[howtoforge](http://www.howtoforge.com)。通过上面的教程，成功安装上了lamp。开始在本地都浏览都没有任何问题，可是后来换台主机浏览就出现了异常情况。好端端的html文件都打不开（提示下载什么bin文件），而且图片都无法显示，而linux服务器上却能正常访问。这着实让我郁闷！想找人问，却发现现在才早上8点。只好自己在网上搜索，在碰壁N次之后居然让我给找到了。在apache的配置文件中添加如下两行内容。不过这个原因，直到现在我也没弄懂。在xamp网站上，只是说不添加这两行，某些linux服务器下无法显示图片。这里只记录下问题的表现，所有的静态文件使用浏览器打开时会在首部添加上http的头信息和一些不知名的乱码（下次有空研究一下，可能会弄清楚问题的原因）。

[codesyntax lang="apache"]

    EnableSendfile Off
    EnableMMAP Off

[/codesyntax]

**4. ssh的配置**

这里简单写下ssh的配置

修改
sshd\_config中的一些配置，然后对/etc/host.deny和/etc/host.allow进行修改。

5.文件权限

之前程序是在windows下编写和运行的，在对文件操作时不用考虑太多文件的权限问题。可转到linux后，文件的读写出现比较严重的问题。通过修改/etc/profile(貌似还可以通过修改.bash\_profile或者.bashrc来实现)来实现文件创建时默认权限来解决。这里就用到了umask。umask
022是默认的，对新创建的文件夹是777-022=755,而文件则是666-022=644。
