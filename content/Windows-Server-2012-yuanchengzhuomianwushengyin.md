Title: Windows Server 2012 远程桌面无声音
Date: 2013-03-16 05:04
Author: lmatt wang
Slug: Windows-Server-2012-yuanchengzhuomianwushengyin

解决方法：\
1.查看远程桌面连接本地客户端中“Options（选项） =\> Local
Resource（本地资源） =\> Remote audio（远程音频） =\> Play on this
computer（在当前电脑播放）"是否被选中。\
2.查看windows server 2012是否开启windows audio service.
可以直接在搜索框中搜索service，打开service管理界面并找到windows
audio服务，确认服务是否开启。
