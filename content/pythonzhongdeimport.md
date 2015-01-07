Title: python中的import
Date: 2010-04-21 14:28
Author: lmatt wang
Slug: pythonzhongdeimport

[codesyntax lang="python" lines="fancy"]

    import test1
    import pack1.pack2.test1
    from test1 import fun, cla, mod_name
    from .pack import test1

[/codesyntax]

第一行是python中导入module或者package的普通方式，通过这个语句，在接下来的代码中就可以使用test1
module中所定义的function, class,
var等。这类似C语言中的\#include，只是在使用module中的的内容时需要加上"test."前缀（相当于c++中的namespace）。

第二行同第一行，其中的pack1和pack2都是package，而test1只能是package或module（这与第三行有区别）。

第三行是从test1
module中导入fun(方法)，cla(类)，mod\_name(子模块)。在使用这些被导入的内容时，可以不用使用前缀（不同于第一行内容）。

第四行是在python2.5以后加入的相对路径（显式的，以前不是）导入。

import时module的搜索路径。这个路径首先是当前目录（是指包含被运行的python
script的目录），接着是PYTHONPATH（如果定义的话，这就是系统上的环境变量，格式同PATH），最后是python的安装目录（包括一些python库的目录）等。通过sys.path就可以获取该搜索路径。

“from pack import \*”这个语句和java中的“import
pack.\*"的含义有所不同。在python中，如果pack
module下的\_\_init\_\_.py中定义了\_\_all\_\_变量（如<span
style="color: #ff0000;">\_\_all\_\_ = ["echo", "surround",
"reverse"]</span>）,那么就可以在接下来的代码中直接使用echo,
surround,reverse三个子模块（其他子模块就不行）。而如果没有定义\_\_all\_\_变量，那么仅仅只是引入pack（除非在import \*语句前有import其他子模块，这样的子模块也不需要前缀，例子见下面代码）。

[codesyntax lang="python"]

    import pack.test1
    from pack import *

    test1.fun()
    pack.test2.fun()//error

[/codesyntax]

"from mod\_name
import \*"这个语句就可以直接调用module中的内容，不需要前缀

下面内容不太懂，需要实验。这个top-level是最顶层的还是只是上一层的\

> <span style="color: #ff0000;">if the imported module is not found in
> the current package (the package of which the current module is a
> submodule), the
> [import](http://docs.python.org/reference/simple_stmts.html#import)
> statement looks for a top-level module with the given name.</span>
> </p>

