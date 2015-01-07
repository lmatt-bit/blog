Title: 读取jar文件中的资源
Date: 2010-06-30 16:43
Author: lmatt wang
Slug: duqujarwenjianzhongdeziyuan

在前面一篇文中，生成仪表盘时使用了背景图片和指针图片，如果将这些图片（资源）和代码打包到一个jar文件中，读取的时候需要注意一下路径问题。

打包后路径如下图所示：

|ict\
|-dashboard\
|--Dashboard.java\
|image\
|-bg.png\
|-pointer.png

如需在Dashboard.java中读取bg.png和pointer.png资源，可以使用如下的代码：

    this.getClass().getClassLoader().getResourceAsStream("images/bg.png");
    this.getClass().getClassLoader().getResourceAsStream("images/pointer.png");
