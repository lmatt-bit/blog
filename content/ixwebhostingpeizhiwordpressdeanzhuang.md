Title: ixwebhosting配置wordpress的安装
Date: 2010-03-12 13:33
Author: lmatt wang
Slug: ixwebhostingpeizhiwordpressdeanzhuang

在域名目录下的cgi-bin目录中添加php.ini文件，文件内容如下。具体是什么意思，我还不太懂。:p

[codesyntax lang="apache"]

    [PHP]
    display_errors = Off

    mbstring.language = neutral
    mbstring.internal_encoding = EUC-JP
    mbstring.http_input = auto
    mbstring.http_output = SJIS
    mbstring.encoding_translation =
    mbstring.detect_order = auto
    mbstring.substitute_character =
    mbstring.func_overload = 0

    register_globals = Off

[/codesyntax]

其他如joolma,durpal,textpattern貌似都可以这样配置（其中只有durpal没有试过）。
