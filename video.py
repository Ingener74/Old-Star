# encoding: utf8
from PySide.QtCore import Qt
from PySide.QtGui import QWidget, QApplication
import sys

from res import (Ui_VideoWidget)


class Video(QWidget, Ui_VideoWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    video = Video()
    video.show()

    sys.exit(app.exec_())
