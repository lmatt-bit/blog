Title: c++ const的一些知识
Date: 2010-03-15 16:58
Author: lmatt wang
Slug: c++-constdeyixiezhishi

const 指针

const在\*左边，是指指针所指的对象是不可以改变的；在\*右边，则是指指针不能指向另外一个对象。

[codesyntax lang="cpp"]

    int b = 10;
    const int *a = &b;//or int const *a = &b;
    *a = 11;//error

    int d = 20;
    int * const c = &b;
    c = &d;//error

[/codesyntax]

const 引用

const只能在&左边，指所引用的对象不能被改变。如

[codesyntax lang="cpp"]

    int a = 10;
    const int &b; = a;

[/codesyntax]

const 函数

一般将const放在签名的最后。如

[codesyntax lang="cpp"]

    int add(int b) const;

[/codesyntax]

如果是成员函数，则不能改变数据成员的value.
