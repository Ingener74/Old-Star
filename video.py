# encoding: utf8
from PySide.QtCore import Qt, QThread
from PySide.QtGui import QWidget, QApplication
import sys
from librtmp import RTMP, RTMPError

from res import (Ui_VideoWidget)


class StreamThread(QThread):
    def __init__(self):
        QThread.__init__(self)

    def run(self):
        try:
            rtmp = RTMP(url='rtmp://127.0.0.1:1935/live/test')

            print '1'
            print rtmp

            print '2'
            print rtmp.connect()

            print '3'
            pkt = rtmp.read_packet()

            print '4'
            print pkt

            print '5'
            stream = rtmp.create_stream()

            print '6'
            print stream

            # data = stream.read(1024)

        except RTMPError, e:
            print e


class Video(QWidget, Ui_VideoWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)

        self.controlButton.clicked.connect(self.onControlButton)

    def onControlButton(self):
        self.streamThread = StreamThread()
        self.streamThread.start()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

if __name__ == '__main__':
    # noinspection PyCallByClass
    QApplication.setStyle("plastique")
    app = QApplication(sys.argv)

    video = Video()
    video.show()

    sys.exit(app.exec_())
