Title: apache url rewrite
Date: 2010-04-19 16:17
Author: lmatt wang
Slug: apache-url-rewrite

最近在ixwebhosting上安装了web.py(python下的一个full stack web
framework)，为了在路径中隐藏.py，需要使用url
rewrite。apache中mod\_rewrite可以实现这个功能。

在ixwebhosting下，可以修改网页根目录下的.htaccess，具体内容见下。

[codesyntax lang="apache"]

    RewriteEngine On
    RewriteBase /
    RewriteCond %{REQUEST_URI} !^/icons
    RewriteCond %{REQUEST_URI} !^/favicon.ico$
    RewriteCond %{REQUEST_URI} !^(/.*)+index.py/
    RewriteRule ^(.*)$ index.py/$1 [PT]

[/codesyntax]

以后使用http://www.test.com/就相当于访问index.py，而且/\*都由index.py来处理。\

> mod\_rewrite还有更多的内容，以后逐渐更新
> </p>

