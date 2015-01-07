Title: apache 配置http代理服务器
Date: 2010-03-16 09:45
Author: lmatt wang
Slug: apache-peizhihttpdailifuwuqi

以opensuse11.2为例，在/etc/apache2/sysconfig.d/目录中的loadmodule.conf中添加如下内容。分别是载入cache,disk\_cache,proxy和proxy\_http模块。其中cache和disk\_cache用于缓存信息，proxy和proxy\_http（用于支持http）用于启用代理。

[codesyntax lang="apache"]

    LoadModule cache_module /usr/lib/apache2-prefork/mod_cache.so
    LoadModule disk_cache_module /usr/lib/apache2-prefork/mod_disk_cache.so
    LoadModule proxy_module /usr/lib/apache2-prefork/mod_proxy.so
    LoadModule proxy_http_module /usr/lib/apache2-prefork/mod_proxy_http.so

[/codesyntax]

然后在/etc/apache2/conf.d目录下新建一个proxy.conf，文件中添加如下内容

[codesyntax lang="apache"]

    #CacheRoot cache存放的位置
    #CacheMaxFileSize 以byte为单位

     
      CacheRoot /home/cache/
        CacheEnable disk /
        CacheDirLevels 5
      CacheDirLength 3
      CacheMaxFileSize 2097152
     


    #直接代理
    ProxyRequests On
    ProxyVia On

    #需要密码验证。密码文件使用htpasswd 生成，存放的位置则由AuthUserFile指出。

    Order deny,allow
    Allow from all
    AuthType Basic
    AuthName "need password"
    AuthUserFile passwords
    Require valid-user

[/codesyntax]

然后重启apache就可以了。/etc/int.d/apache2 restart
