Title: libvlc与pyqt搭配使用
Date: 2010-03-30 17:35
Author: lmatt wang
Slug: libvlcyupyqtdapeishiyong

libvlc是vlc播放器社区所提供的一个库，使用这个库，可以快速实现一个全能的播放器（支持很多视频格式的播放）。对于这个库，官方提供的是c++版本，不过现在有很多语言的binding，如python,
java,
c\#等。要提到的一点是，libvlc是gpl协议的。为了更方便与pyqt联合起来使用，我选择了python
binding的libvlc。对于python版本，官方wiki上所给出的链接地址是错误(可能是过期的原因)的，下面给出最新的地址。http://liris.cnrs.fr/advene/download/python-ctypes/
从最新的地址下载到vlc.py文件之后，你可以将vlc.py放到sit-package或当前工作目录中。如果要导入这个文件，只需要在python脚本中添加import
vlc即可。python版libvlc的api详情可参见http://liris.cnrs.fr/advene/download/python-ctypes/doc/index.html。要实现视频的播放，仅仅靠一个vlc.py是不够的，您还需要确保个人的机器上有vlc的lib（可以通过安装vlc播放器来获得，也可以自己讲lib的部分打包起来）。有了这些之后，你可以通过运行vlc.py这个文件来查看是否配置成功，直接在命令行中输入python
vlc.py
path（path为视频文件的路径）。如果成功配置，会弹出一个视频窗口播放您所输入的文件。

接着就是用pyqt来把libvlc封装起来，这里我参考了vlc官方wiki上关于在qt中使用libvlc的例子。从qt的c++到pyqt的python语言，其中的转变没有花费太多的时间。很多内容都是相同，只不过pyqt会显得更加简单。这里需要提到的是pyqt也是gpl的，不过你可以购买到商业许可。下面是我用pyqt和libvlc写的一个简单播放器代码。其中需要注意的一点，在绑定窗口和libvlc时，直接使用QWidget不会成功（代码中使用的是QFrame）。

[codesyntax lang="python"]

    #! /usr/bin/python
    # coding=utf-8

    import sys
    import time
    import json
    import vlc
    from PyQt4 import QtGui
    from PyQt4 import QtCore

    class VLCWidget(QtGui.QWidget):
        def __init__(self, parent=None):
            QtGui.QWidget.__init__(self, parent)

            self.videoWidget = QtGui.QFrame(self)

            self.volumeSlider = QtGui.QSlider(QtCore.Qt.Horizontal)
            self.volumeSlider.setMaximum(100)
            self.volumeSlider.setToolTip("Audio slider")

            self.positionSlider = QtGui.QSlider(QtCore.Qt.Horizontal)
            self.positionSlider.setMaximum(10000)

            layout = QtGui.QVBoxLayout()
            layout.addWidget(self.videoWidget)
            layout.addWidget(self.positionSlider)
            layout.addWidget(self.volumeSlider)
            self.setLayout(layout)
            self.setMinimumHeight(500)

            self.isPlaying = False
            self.poller = QtCore.QTimer()

            self.inst = vlc.Instance()
            self.player = self.inst.media_player_new()
            if sys.platform == 'linux2':
                self.player.set_xwindow(self.videoWidget.winId())
            elif sys.platform == 'win32':
                self.player.set_hwnd(self.videoWidget.winId())
            else:
                sys.exit(0)

            self.poller.timeout.connect(self.updateInterface)
            self.positionSlider.sliderMoved.connect(self.changePosition)
            self.volumeSlider.sliderMoved.connect(self.changeVolume)

            self.poller.start(400)

        def changeVolume(self, newVolume):
            #print 'volume'
            self.inst.audio_set_volume(newVolume)

        def changePosition(self, newPosition):
            media = self.player.get_media()
            if not media:
                return

            pos = float(newPosition) / 10000
            self.player.set_position(pos)

        def updateInterface(self):
            media = self.player.get_media()
            #print 'tick'

            if not media:
                return

            #print 'tick'
            pos = int(self.player.get_position() * 10000)
            self.positionSlider.setValue(pos)
            volume = self.inst.audio_get_volume()
            self.volumeSlider.setValue(volume)

        def play(self, path):
            print path
            media = self.inst.media_new(path)
            self.player.set_media(media)
            self.player.play()

        #def sizeHint(self):
        #   return QtCore.QSize(750, 500)

    class MainWindow(QtGui.QMainWindow):
        def __init__(self):
            super(QtGui.QMainWindow, self).__init__()

            self.setupActions()
            self.setupMenus()
            self.setupUI()
            self.center()



        def closeEvent(self, event):
            pass
            #event.ignore()

        def setupUI(self):
            self.player = VLCWidget()

            mainLayout = QtGui.QVBoxLayout()
            mainLayout.addWidget(self.player)

            widget = QtGui.QWidget()
            widget.setLayout(mainLayout)
            self.setCentralWidget(widget)
            self.resize(800, 600)
            self.setWindowTitle("SimplePlayer")

        def setupActions(self):
            self.addFilesAction = QtGui.QAction("Add &Files;", self,
                shortcut="Ctrl+F", triggered=self.addFiles)
            self.exitAction = QtGui.QAction("E&xit;", self,
                shortcut="Ctrl+X", triggered=self.close)
            self.settingsAction = QtGui.QAction("&Settings;", self,
                shortcut="Ctrl+S", triggered=self.settings)
            self.aboutAction=QtGui.QAction("&About;", self,
                shortcut="Ctrl+A", triggered=self.about)
            self.aboutAuthorAction = QtGui.QAction("Author's &HomePage;", self,
                shortcut="Ctrl+H", triggered=self.aboutAuthor)

        def settings(self):
            pass

        def about(self):
            pass

        def aboutAuthor(self):
            pass

        def addFiles(self):

            files = QtGui.QFileDialog.getOpenFileNames(self, "Select")

            if not files:
                return

            #self.player.play(unicode(files[0]))
            self.player.play(str(files[0].toUtf8()))

        def setupMenus(self):
            fileMenu = self.menuBar().addMenu("&File;")
            fileMenu.addAction(self.addFilesAction)
            fileMenu.addSeparator()
            fileMenu.addAction(self.exitAction)

            toolMenu = self.menuBar().addMenu("&Tools;")
            toolMenu.addAction(self.settingsAction)

            aboutMenu = self.menuBar().addMenu("&Help;")
            aboutMenu.addAction(self.aboutAction)
            aboutMenu.addAction(self.aboutAuthorAction)

        def center(self):
            screen = QtGui.QDesktopWidget().screenGeometry()
            size = self.geometry()
            self.move((screen.width() - size.width()) / 2,
                (screen.height() - size.height()) / 2)

    if __name__ == '__main__':
        app = QtGui.QApplication(sys.argv)
        app.setApplicationName("SimplePlayer")
        app.setQuitOnLastWindowClosed(True)

        window = MainWindow()
        window.show()

        sys.exit(app.exec_())

[/codesyntax]
