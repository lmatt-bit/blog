Title: python解析html
Date: 2010-11-10 15:03
Author: lmatt wang
Slug: pythonjiexihtml

<p>
python自带有一个html的解析库，但这个库的功能有限，而且对网页中异常情况的处理不好。\
后来在网上找到一个叫[BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/)的网页解析库，这个库利用了正则表达式对网页进行处理，能比较完美地处理异常情况，还支持unicode。\
除此之外还有lxml等python库。\
下面是BeautifulSoup的一些例子，是从官网摘过来的。更多详细信息可以看[官方文档](http://www.crummy.com/software/BeautifulSoup/documentation.html)，有[中文版](http://www.crummy.com/software/BeautifulSoup/documentation.zh.html)\
<script src="https://gist.github.com/670947.js?file=BeautifulSoup.py"></script>
</p>

