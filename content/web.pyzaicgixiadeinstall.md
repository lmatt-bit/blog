Title: web.py在cgi下的install
Date: 2010-04-19 16:58
Author: lmatt wang
Slug: web.pyzaicgixiadeinstall

由于ixwebhosting下无法安装web.py之类的程序，只能将web.py当作工程的一部分。这需要将web.py下的web目录拷贝到工程目录中，以后只需要import
web就可以使用web.py了。

web.py可以和Lighttpd,Apache搭配使用。web.py的官网推荐的是使用lighttpd（fastcgi）。这里介绍的是Apache下的CGI方式（这种方式效率不高，不过在ixwebhosting下只能使用这种方式）。

在.htaccess下添加如下代码：

[codesyntax lang="apache"]

    Options +ExecCGI
    AddHandler cgi-script .py

[/codesyntax]

或者在http.conf（或apache2.conf）下添加如下代码：

[codesyntax lang="apache"]

    Alias /foo/static/ /path/to/static
    ScriptAlias /foo/ /path/to/code.py

[/codesyntax]

上述内容参见于[web.py](http://webpy.org/)的官网。

除了作以上配置外，web.py在CGI下运行还需要安装[flup](http://trac.saddi.com/flup)。同web.py一样，[flup](http://trac.saddi.com/flup)也存在无法安装的问题。这里同样将flup文件下载解压到工程目录，<span
style="text-decoration: line-through;">不过需要注意的是需要修改其中的部分代码。由于flup不是安装到机器上，其代码中的部分导入失败，这需要将"import
flup.\*"之类的语句去除掉flup。(如果将flup放在web.py的目录下才需要)</span>\

> 下面引用[web.py](http://webpy.org/)官网内容：
> </p>

产品
----

现在所运行 web.py 程序的web服务器是挺不错的，
但绝大多数网站还是需要更加专业一些的web服务器。web.py 实现了
[WSGI](http://www.python.org/dev/peps/pep-0333/)
并能在任何兼容它的服务器上运行。 WSGI
是一个web服务器与应用程序之间的通用API, 就如Java 的 Servlet 接口。
你需要安装 [flup](http://trac.saddi.com/flup) ([download
here](http://www.saddi.com/software/flup/dist/)) 使web.py 支持with CGI，
FastCGI 或 SCGI， flup提供了这些API的WSGI接口。

对于所有的CGI变量， 添加以下到你的 `code.py`:

    #!/usr/bin/env python

并运行 `chmod +x code.py` 添加可执行属性。

<a name="lighttpd"></a>\

### LightTPD

<a name="lighttpdfastcgi"></a>\

#### .. 使用 FastCGI

在产品中通过FastCGI结合lighttpd是web.py使用的一种推荐方法。
[reddit.com](http://reddit.com/) 通过该方法来处理百万次的点击。

lighttpd config设置参考如下：

     server.modules = ("mod_fastcgi", "mod_rewrite")
     server.document-root = "/path/to/root/"
     fastcgi.server = ( "/code.py" =>
     (( "socket" => "/tmp/fastcgi.socket",
        "bin-path" => "/path/to/root/code.py",
        "max-procs" => 1
     ))
     )

     url.rewrite-once = (
       "^/favicon.ico$" => "/static/favicon.ico",
       "^/static/(.*)$" => "/static/$1",
       "^/(.*)$" => "/code.py/$1"
     )

在某些版本的lighttpd中，
需要保证fastcgi.server选项下的"check-local"属性设置为"false",
特别是当你的 `code.py` 不在文档根目录下。

如果你得到错误显示不能够导入flup， 请在命令行下输入 "easy\_install flup"
来安装。

从修订版本 145开始，
如果你的代码使用了重定向，还需要在fastcgi选项下设置bin-environment变量。
如果你的代码重定向到<http://domain.com/> 而在url栏中你会看到
[http://domain.com/code.py/，](http://domain.com/code.py/%EF%BC%8C)
你可以通过设置这个环境变量来阻止。 这样你的fastcgi.server设置将会如下：

    fastcgi.server = ( "/code.py" =>
    ((
       "socket" => "/tmp/fastcgi.socket",
       "bin-path" => "/path/to/root/code.py",
       "max-procs" => 1,
       "bin-environment" => (
         "REAL_SCRIPT_NAME" => ""
       ),
       "check-local" => "disable"
    ))
    )

<a name="apache"></a>\

### Apache

<a name="apachecgi"></a>\

#### .. 使用 CGI

添加以下到 `httpd.conf` 或 `apache2.conf`。

    Alias /foo/static/ /path/to/static
    ScriptAlias /foo/ /path/to/code.py

<a name="apachecgihtaccess"></a>\

#### .. 使用 CGI .htaccess

CGI很容易配置， 但不适合高性能网站。 添加以下到你的 `.htaccess`：

    Options +ExecCGI
    AddHandler cgi-script .py

将你的浏览器指向 `http://example.com/code.py/`。
不要忘记最后的斜杠，否则你将会看到 `not found` 消息 (因为在 `urls`
列表中你输入的没有被匹配到). 为了让其运行的时候不需要添加 `code.py`，
启用mod\_rewrite 法则 (查看如下)。

注意: `web.py` 的实现破坏了 `cgitb` 模块，因为它截取了 `stdout`。
可以通过以下的方法来解决该问题：

    import cgitb; cgitb.enable()
    import sys

    # ... import web etc here...

    def cgidebugerror():
        """
        """        _wrappedstdout = sys.stdout

        sys.stdout = web._oldstdout
        cgitb.handler()

        sys.stdout = _wrappedstdout

    web.internalerror = cgidebugerror

<a name="apachefastcgi"></a>\

#### .. 使用 FastCGI

FastCGI很容易配置，运行方式如同mod\_python。

添加以下到 `.htaccess`：

          SetHandler fastcgi-script

不幸的是, 不像lighttpd, Apache不能够暗示你的web.py脚本以FastCGI
服务器的形式工作，因此你需要明确的告诉web.py。 添加以下到 `code.py`的
`if __name__ == "__main__":` 行前：

    web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)

将你的浏览器指向 `http://example.com/code.py/`。
不要忘记最后的斜杠，否则你将会看到 `not found` 消息 (因为在 `urls`
列表中你输入的没有被匹配到). 为了让其运行的时候不需要添加 `code.py`，
启用mod\_rewrite 法则 (查看如下)。

[Walter
还有一些额外建议](http://lemurware.blogspot.com/2006/05/webpy-apache-configuration-and-you.html).

<a name="apachescgi"></a>\

#### .. 使用 SCGI

<https://www.mems-exchange.org/software/scgi/> 从
<http://www.mems-exchange.org/software/files/mod_scgi/> 下载 `mod_scgi`
代码 windows apache 用户： 编辑 httpd.conf：

    LoadModule scgi_module Modules/mod_scgi.so
    SCGIMount / 127.0.0.1:8080

重启apache，并在命令行中如下方式启动code.py：

    python code.py 127.0.0.1:8080 scgi

打开你的浏览器，访问127.0.0.1 It's ok!

<a name="apachemodpython"></a>\

#### .. 使用 mod\_python

mod\_python 运行方式如同FastCGI， 但不是那么方便配置。

对于 Python 2.5 按照如下：

    cd /usr/lib/python2.5/wsgiref
    # or in windows: cd /python2.5/lib/wsgiref
    wget -O modpython_gateway.py http://projects.amor.org/misc/browser/modpython_gateway.py?format=raw
    # or fetch the file from that address using your browser

对于 Python \<2.5 按照如下：

    cd /usr/lib/python2.4/site-packages
    # or in windows: cd /python2.4/lib/site-packages
    svn co svn://svn.eby-sarna.com/svnroot/wsgiref/wsgiref
    cd wsgiref
    wget -O modpython_gateway.py http://projects.amor.org/misc/browser/modpython_gateway.py?format=raw
    # or fetch the file from that address using your browser

重命名 `code.py` 为 `codep.py` 或别的名字， 添加：

    main = web.wsgifunc(web.webpyfunc(urls, globals()))

在 `.htaccess` 中， 添加：

    AddHandler python-program .py
    PythonHandler wsgiref.modpython_gateway::handler
    PythonOption wsgi.application codep::main

你应该希望添加 `RewriteRule` 将 `/` 指向 `/codep.py/`

确保访问 `/codep.py/` 的时候有添加最后的 `/`。
否则，你将会看到一条错误信息，比如
`A server error occurred. Please contact the administrator.`

<a name="apachemodwsgi"></a>\

#### .. 使用 mod\_wsgi

mod\_wsgi 是一个新的Apache模块
[通常优于mod\_python](http://code.google.com/p/modwsgi/wiki/PerformanceEstimates)
用于架设WSGI应用，它非常容易配置。

在 `code.py` 的最后添加：

    application = web.wsgifunc(web.webpyfunc(urls, globals()))

mod\_wsgi 提供
[许多可行方法](http://code.google.com/p/modwsgi/wiki/ConfigurationDirectives)
来实现WSGI应用, 但一种简单的方法是添加以下到 .htaccess：

        SetHandler wsgi-script
        Options ExecCGI FollowSymLinks

如果在apache的 error.log 文件中出现 "ImportError: No module named web"，
在导入web之前，你可能需要在code.py中尝试设置绝对路径：

    import sys, os
    abspath = os.path.dirname(__file__)
    sys.path.append(abspath)
    os.chdir(abspath)
    import web

同时， 你可能需要查看
[WSGI应用的常见问题](http://code.google.com/p/modwsgi/wiki/ApplicationIssues)的
"Application Working Directory" 部分。

最终应该可以访问 `http://example.com/code.py/`。

<a name="apachemodrewrite"></a>\

#### mod\_rewrite 法则，Apache

如果希望 web.py 能够通过 '[http://example.com](http://example.com/)'
访问，代替使用 '<http://example.com/code.py/>'， 添加以下法则到
`.htaccess` 文件：

      RewriteEngine on
      RewriteBase /
      RewriteCond %{REQUEST_URI} !^/icons
      RewriteCond %{REQUEST_URI} !^/favicon.ico$
      RewriteCond %{REQUEST_URI} !^(/.*)+code.py/
      RewriteRule ^(.*)$ code.py/$1 [PT]

如果 `code.py` 在子目录 `myapp/`中， 调整 RewriteBase 为
`RewriteBase /myapp/`。 如果还有一些静态文件如CSS文件和图片文件,
复制这些并改成你需要的地址。
