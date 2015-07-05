# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Pavel/workspace/Video-receiver/res/Video.ui'
#
# Created: Sun Jul 05 18:30:26 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_VideoWidget(object):
    def setupUi(self, VideoWidget):
        VideoWidget.setObjectName("VideoWidget")
        VideoWidget.resize(909, 621)
        self.verticalLayout = QtGui.QVBoxLayout(VideoWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView = QtGui.QGraphicsView(VideoWidget)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.controlButton = QtGui.QPushButton(VideoWidget)
        self.controlButton.setObjectName("controlButton")
        self.verticalLayout.addWidget(self.controlButton)

        self.retranslateUi(VideoWidget)
        QtCore.QMetaObject.connectSlotsByName(VideoWidget)

    def retranslateUi(self, VideoWidget):
        VideoWidget.setWindowTitle(QtGui.QApplication.translate("VideoWidget", "Фильм", None, QtGui.QApplication.UnicodeUTF8))
        self.controlButton.setText(QtGui.QApplication.translate("VideoWidget", "Play", None, QtGui.QApplication.UnicodeUTF8))

