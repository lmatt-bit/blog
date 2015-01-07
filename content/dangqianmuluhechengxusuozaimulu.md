Title: 当前目录和程序所在目录
Date: 2010-10-20 10:19
Author: lmatt wang
Slug: dangqianmuluhechengxusuozaimulu

**1.python**\
当前目录：

    import os
    os.getcwd()

程序所在目录：

    import os
    #os.path.split( os.path.realpath( sys.argv[0] ) )[0]
    os.path.dirname(os.path.realpath(__file__))

**2.vc/mfc**\
当前目录:

    TCHAR path[MAX_PATH];
    GetCurrentDirectory(path, MAX_PATH);

程序所在目录:

    TCHAR path[MAX_PATH];
    GetModuleFileName(NULL, path, MAX_PATH);

**3.c/c++(linux)**\
当前目录:

    char buffer[MAX_PATH];
    #include < direct.h >
    getcwd(buffer, _MAX_PATH);

程序所在目录:

    #include < stdio.h >
    #include < unistd.h >
    int main() {
        char buf[256];
        readlink("/proc/self/exe", buf, sizeof(buf));
        printf("%s\n",buf);
        return 0;
    }

    ------------------------------------------------------------------
    todo:

    Linux:
    /proc/pid/exe

    Solaris:
    /proc/pid/object/a.out (filename only)
    /proc/pid/path/a.out (complete pathname)

    *BSD (and maybe Darwing too):
    /proc/pid/file
    ----------------------------------------------------------------

**4.java**\
当前目录:

    String curDir = System.getProperty("user.dir"); 
    //String currentDir = new File(".").getAbsolutePath();

程序所在目录:

    ClassName.class.getResource("ClassName.class").getPath();
    //jsp
    //getServletContext().getRealPath("/");
