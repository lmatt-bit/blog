Title: 打包python运行环境
Date: 2013-03-31 20:51
Author: lmatt wang
Slug: dabaopythonyunxinghuanjing

1.准备以下文件：\
      python.exe(python安装目录下)\
      python27.dll(python安装目录下或System32目录下)\
      DLLs目录(python安装目录下)\
      libs目录(python安装目录下)\
     
Lib.zip(python安装目录下的Lib目录，将其打包为zip文件，可以减少文件数目)\
      main.py(需要运行的文件)\
2.创建run.bat文件\
---------------------------------------------------------------------\
     set PYTHONPATH=".;.\\Lib.zip;.\\DLLs;.\\libs"\
     .\\python.exe main.py %\*\
---------------------------------------------------------------------\
3.使用run.bat就可以直接运行main.py文件，并可以传递参数。
