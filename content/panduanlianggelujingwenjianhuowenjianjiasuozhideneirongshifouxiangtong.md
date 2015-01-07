Title: 判断两个路径（文件或文件夹）所指的内容是否相同
Date: 2010-10-25 14:40
Author: lmatt wang
Slug: panduanlianggelujingwenjianhuowenjianjiasuozhideneirongshifouxiangtong

思路：\
1.判断文件是否都存在\
2.判断类型是否相同（是否都是文件夹，是否都是文件）\
3.如果是文件， 比较文件的二进制内容\
4.如果是文件夹：\
4.1 列出文件夹下的所有文件，并按文件名排序\
4.2 依次递归比较所有文件

<p>
代码：\

<script src="http://gist.github.com/646594.js?file=compare_file.cpp"></script>
</p>

