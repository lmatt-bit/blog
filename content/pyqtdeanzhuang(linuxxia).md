Title: pyqt的安装(linux下)
Date: 2010-04-18 06:34
Author: lmatt wang
Slug: pyqtdeanzhuang(linuxxia)

nokia在收购qt之后，让qt出现了lgpl的licence，这一举动获得了不少赞许。nokia也希望pyqt能有lgpl的licence，只可惜与Riverbank谈判不拢，pyqt依旧是gpl的licence。迫不得已，nokia只好自己搞个类似pyqt的项目（pyside）。这个pyside项目的协议是lgpl的，目前还不够完善，但相信以后的前景是不错的。

目前pyqt仍然是主流，所以下面说一下pyqt的安装。由于windows有安装的exe，几乎不用配置就可以安装上，这里就不做说明。

要在linux下安装pyqt，首先需要安装Riverbank的SIP。在SIP安装前需要确保系统上安装了python-devel（python
开发的一些文件，在fedora下可以直接yum安装）。

安装SIP过程：

<span style="color: #3366ff;">1.下载SIP，解压。</span>

<span style="color: #3366ff;">2.从命令行中进入SIP的目录，输入python
configure.py</span>

<span
style="color: #3366ff;">3.在上一步成功之后，输入make（需要确保有make，gcc等一系列编译工具）</span>

<span style="color: #3366ff;">4.在上一步成功之后，输入make
install。到此sip安装完成。</span>

接着是pyqt的安装：

<span style="color: #3366ff;">1.下载pyqt，解压</span>

<span style="color: #3366ff;">2.从命令行进入pyqt的目录，输入python
configure.py</span>

<span
style="color: #3366ff;">3.在上一步成功之后，输入make（需要确保有make，gcc等一系列编译工具）</span>

<span style="color: #3366ff;">4.在上一步成功之后，输入make
install。到此pyqt安装完成。</span>

<span style="color: #3366ff;"><span style="color: #000000;">bug:pyqt
4.7.2貌似存在bug，在import
QtGui和QtCore时，需要先引入QtGui。这个问题导致许多pyqt程序无法运行。</span>\
</span>
