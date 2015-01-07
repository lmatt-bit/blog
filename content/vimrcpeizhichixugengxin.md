Title: vimrc配置（持续更新）
Date: 2010-04-18 05:59
Author: lmatt wang
Slug: vimrcpeizhichixugengxin

文章转载自http://jmcpherson.org/vimrc.html

.vimrc and customization

vim is extremely customizable. It will read the file .vimrc in your home
directory before it starts. This file can contain settings and even
scripts. The below settings are ones I've found helpful -- give them a
try!

set nocompatible

This setting prevents vim from emulating the original vi's bugs and
limitations.\
set autoindent\
set smartindent

The first setting tells vim to use "autoindent" (that is, use the
current line's indent level to set the indent level of new lines). The
second makes vim attempt to intelligently guess the indent level of any
new line based on the previous line, assuming the source file is in a
C-like language. Combined, they are very useful in writing
well-formatted source code.\
set tabstop=4\
set shiftwidth=4

I prefer 4-space tabs to 8-space tabs. The first setting sets up 4-space
tabs, and the second tells vi to use 4 spaces when text is indented
(auto or with the manual indent adjustmenters.)\
set showmatch

This setting will cause the cursor to very briefly jump to a
brace/parenthese/bracket's "match" whenever you type a closing or
opening brace/parenthese/bracket. I've had almost no
mismatched-punctuation errors since I started using this setting.\
set guioptions-=T

I find the toolbar in the GUI version of vim (gvim) to be somewhat
useless visual clutter. This option gets rid of the toolbar.\
set vb t\_vb=

This setting prevents vi from making its annoying beeps when a command
doesn't work. Instead, it briefly flashes the screen -- much less
annoying.\
set ruler

This setting ensures that each window contains a statusline that
displays the current cursor position.\
set nohls

By default, search matches are highlighted. I find this annoying most of
the time. This option turns off search highlighting. You can always turn
it back on with :set hls.\
set incsearch

With this nifty option, vim will search for text as you enter it. For
instance, if you type /bob to search for bob, vi will go to the first
"b" after you type the "b," to the first "bo" after you type the "o,"
and so on. It makes searching much faster, since if you pay attention
you never have to enter more than the minimum number of characters to
find your target location. Make sure that you press Enter to accept the
match after vim finds the location you want.\
set virtualedit=all

By default, vim doesn't let the cursor stray beyond the defined text.
This setting allows the cursor to freely roam anywhere it likes in
command mode. It feels weird at first but is quite useful.

Type :help options within vim to get a complete list of options.

Many more advanced techniques, options, and mappings are available on
[the official vim site](http://www.vim.org/).

//下面是个人的一些配置

set smarttab 按backspace键时自动将4个空格一次删除

set number

set expandtab

set scrolloff=3

syntax on

-------------------- for windows vim-------------------------\
set nocampatible\
set autoindent\
set smartindent\
set tabstop=4\
set shiftwidth=4\
set showmatch\
set ruler\
set smarttab\
set number\
set expandtab\
set scrolloff=3\
syntax on\
--------------------end for windows vim--------------------
