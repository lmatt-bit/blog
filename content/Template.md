Title: Template
Date: 2010-03-21 08:38
Author: lmatt wang
Slug: Template

文章内容参考了<http://www.cplusplus.com/doc/tutorial/templates/>

个人觉得template的使用，使得
c++更加oo了。下面就记录下template的几种用法。\

**Function template**
=====================

函数template的声明和定义一般使用如下的方法。

[codesyntax lang="cpp" title="function template"]

    //declaration
    template //or template 
    T getMax(T, T);

    //definition
    template //or template 
    T getMax(T lfs, T rfs){
       return (lfs > rfs)?lfs:rfs;
    }

[/codesyntax]

函数的使用如下。\
中的内容为类型名称，在某些情况（编译器能够理解）下可以省略，下面的例子就可以省略。

[codesyntax lang="cpp"]

    int a = 10, b = 11;
    int c = getMax(a, b);//or getMax(a, b)

[/codesyntax]\

**Class template**
==================

类template的定义一般如下。

[codesyntax lang="cpp"]

    template
    class MyArray{
    private:
       const int N;
      int len;
      T *s;
     MyArray();
    public:
       MyArray(int n):N(n){
          s = new T[N];
         len = 0;
      }
     T at(int i);//declaration
    };

    template
    T MyArray::at(int i){
        if(i < len) return s[i];
      else ;//throw exception
    }

[/codesyntax]

类template的使用如下。

[codesyntax lang="cpp"]

    MyArray a(10);
    //some code here
    std::cout << a.at(0) << std::endl;

[/codesyntax]\

**Template specialization**
===========================

这里以文章开头[链接](http://www.cplusplus.com/doc/tutorial/templates/)中给出的例子来进行说明。其中的mychar.increase()是我添加上去的，这句话会导致编译错误（error:
‘class mycontainer<char>’ has no member named
‘increase’）。这是由于template specialization并不有继承的关系。

[codesyntax lang="cpp"]

    // template specialization
    #include 
    using namespace std;

    // class template:
    template 
    class mycontainer {
        T element;
      public:
        mycontainer (T arg) {element=arg;}
        T increase () {return ++element;}
    };

    // class template specialization:
    template 

    class mycontainer 

</char><char> {\
 char element;\
 public:\
 mycontainer (char arg) {element=arg;}\
 char uppercase ()\
 {\
 if ((element\>='a')&&(element\<='z'))\
 element+='A'-'a';\
 return element;\
 }\
};

int main () {\
 mycontainer<int> myint (7);\
 mycontainer</int></char><char> mychar ('j');\
 cout \<\< myint.increase() \<\< endl;\
 cout \<\< mychar.uppercase() \<\< endl;

//lmatt add,error!\
 cout \<\< (char)mychar.increase() \<\< endl;\
 //lmatt add

return 0;\
}\
[/codesyntax]\

Non-type parameters for templates
=================================

在template中也能像函数那样使用常规的类型作为参数。如下代码所示。其中的MyArray2有default参数，可以直接使用MyArray2
a;。

[codesyntax lang="cpp"]

    template
    class MyArray1{
        T s[N];
    };
    template
    class MyArray2{
     T s[N];
    };

[/codesyntax]\

> Template的声明和实现必须在同一个文件中，这是由于template是compiled on
> demand的，仅仅在被实例化的时候才被compile。同样由于这个原因，template的文件被多次引入也不会产生link
> error。
> </p>

</char>
