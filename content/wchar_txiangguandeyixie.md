Title: wchar_t相关的一些
Date: 2010-06-30 15:54
Author: lmatt wang
Slug: wchar_txiangguandeyixie

**1.单个宽字符的相关函数**

**wctomb** 将wchar\_t字符变成多字节表示

[codesyntax lang="cpp"]

    wchar_t ch = L'中';
    char mb[MB_CUR_MAX];
    int len = wctomb(mb, ch);//成功则返回的值大于0

[/codesyntax]

与wctomb类似有[int mbtowc ( wchar\_t \* pwc, const char \* pmb, size\_t
max );](http://www.cplusplus.com/reference/clibrary/cstdlib/mbtowc/)

**2.宽字符串的相关函数**

**wcstombs**将一个wchar\_t数组转为多字节表示

    size_t wcstombs ( char * mbstr, const wchar_t * wcstr, size_t max );

其中max是mbstr的最大长度。\
与mbstowcs相反的是size\_t mbstowcs ( wchar\_t \* wcstr, const char \*
mbstr, size\_t max );（max也是mbstr的长度）

-------------------------------------------------------

<span style="color: #ff0000;"><strong>

重要的备注</strong></span>\
以上的函数都与系统的locale相关，在执行前需要调用如下函数，否则可能执行失败。

[codesyntax lang="cpp"]

setlocale(LC\_ALL, "")

[/codesyntax]

这个函数除了以上的功能外，在用ifstream读入含有宽字符的文件时也需要使用。这个函数的具体作用需要以后继续了解。

-------------------------------------------------------------------------------

**不那么重要的备注**

以上的函数在linux下用的比较多，而在mfc下常用的是另外一些，需要在其他的文中介绍。

-----------------------------------------------------------------------------

//wcout, wcin, wstring
