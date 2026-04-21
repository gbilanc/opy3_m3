# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'axisframe.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_axisframe(object):
    def setupUi(self, axisframe):
        if not axisframe.objectName():
            axisframe.setObjectName(u"axisframe")
        axisframe.resize(511, 203)
        self.gridLayout = QGridLayout(axisframe)
        self.gridLayout.setObjectName(u"gridLayout")
        self.led001 = QLabel(axisframe)
        self.led001.setObjectName(u"led001")
        font = QFont()
        font.setFamily(u"Ubuntu Condensed")
        font.setPointSize(12)
        self.led001.setFont(font)
        self.led001.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"background-color: rgb(192, 192, 192);")
        self.led001.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.led001, 1, 0, 1, 1)

        self.led003 = QLabel(axisframe)
        self.led003.setObjectName(u"led003")
        self.led003.setFont(font)
        self.led003.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"background-color: rgb(192, 192, 192);")
        self.led003.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.led003, 1, 2, 1, 1)

        self.led005 = QLabel(axisframe)
        self.led005.setObjectName(u"led005")
        self.led005.setFont(font)
        self.led005.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"background-color: rgb(192, 192, 192);")
        self.led005.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.led005, 2, 0, 1, 1)

        self.led002 = QLabel(axisframe)
        self.led002.setObjectName(u"led002")
        self.led002.setFont(font)
        self.led002.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"background-color: rgb(192, 192, 192);")
        self.led002.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.led002, 1, 1, 1, 1)

        self.label_1 = QLabel(axisframe)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setStyleSheet(u"color: rgb(0, 85, 127);")
        self.label_1.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout.addWidget(self.label_1, 3, 0, 1, 1)

        self.label_2 = QLabel(axisframe)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(0, 85, 127);")
        self.label_2.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 1)

        self.label_3 = QLabel(axisframe)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(0, 85, 127);")
        self.label_3.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout.addWidget(self.label_3, 3, 2, 1, 1)

        self.lab001 = QLabel(axisframe)
        self.lab001.setObjectName(u"lab001")
        self.lab001.setMinimumSize(QSize(60, 30))
        font1 = QFont()
        font1.setFamily(u"Digital")
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(QFont.Weight.Normal)
        self.lab001.setFont(font1)
        self.lab001.setStyleSheet(u"background-color: rgb(0, 85, 0);\n"
"color: rgb(85, 255, 127);")
        self.lab001.setFrameShape(QFrame.Panel)
        self.lab001.setFrameShadow(QFrame.Sunken)
        self.lab001.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lab001, 4, 0, 1, 1)

        self.lab002 = QLabel(axisframe)
        self.lab002.setObjectName(u"lab002")
        self.lab002.setMinimumSize(QSize(60, 30))
        font2 = QFont()
        font2.setFamily(u"Digital")
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setWeight(QFont.Weight.Normal)
        self.lab002.setFont(font2)
        self.lab002.setStyleSheet(u"background-color: rgb(0, 85, 0);\n"
"color: rgb(85, 255, 127);")
        self.lab002.setFrameShape(QFrame.Panel)
        self.lab002.setFrameShadow(QFrame.Sunken)
        self.lab002.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lab002, 4, 1, 1, 1)

        self.lab003 = QLabel(axisframe)
        self.lab003.setObjectName(u"lab003")
        self.lab003.setMinimumSize(QSize(60, 30))
        self.lab003.setFont(font2)
        self.lab003.setStyleSheet(u"background-color: rgb(0, 85, 0);\n"
"color: rgb(85, 255, 127);")
        self.lab003.setFrameShape(QFrame.Panel)
        self.lab003.setFrameShadow(QFrame.Sunken)
        self.lab003.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lab003, 4, 2, 1, 1)

        self.lab005 = QLabel(axisframe)
        self.lab005.setObjectName(u"lab005")
        self.lab005.setMinimumSize(QSize(60, 30))
        self.lab005.setFont(font)
        self.lab005.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"background-color: rgb(192, 192, 192);")
        self.lab005.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lab005, 2, 2, 1, 1)

        self.led006 = QLabel(axisframe)
        self.led006.setObjectName(u"led006")
        self.led006.setFont(font)
        self.led006.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"background-color: rgb(192, 192, 192);")
        self.led006.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.led006, 1, 3, 1, 1)

        self.led004 = QLabel(axisframe)
        self.led004.setObjectName(u"led004")
        self.led004.setFont(font)
        self.led004.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"background-color: rgb(192, 192, 192);")
        self.led004.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.led004, 2, 1, 1, 1)

        self.lab006 = QLabel(axisframe)
        self.lab006.setObjectName(u"lab006")
        self.lab006.setMinimumSize(QSize(60, 30))
        self.lab006.setFont(font)
        self.lab006.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"background-color: rgb(192, 192, 192);")
        self.lab006.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lab006, 2, 3, 1, 1)

        self.label_4 = QLabel(axisframe)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: rgb(0, 85, 127);")
        self.label_4.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout.addWidget(self.label_4, 3, 3, 1, 1)

        self.lab004 = QLabel(axisframe)
        self.lab004.setObjectName(u"lab004")
        self.lab004.setMinimumSize(QSize(60, 30))
        self.lab004.setFont(font2)
        self.lab004.setStyleSheet(u"background-color: rgb(0, 85, 0);\n"
"color: rgb(85, 255, 127);")
        self.lab004.setFrameShape(QFrame.Panel)
        self.lab004.setFrameShadow(QFrame.Sunken)
        self.lab004.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lab004, 4, 3, 1, 1)

        self.labtitle = QLabel(axisframe)
        self.labtitle.setObjectName(u"labtitle")
        font3 = QFont()
        font3.setFamily(u"Courier 10 Pitch")
        font3.setPointSize(16)
        font3.setBold(True)
        font3.setWeight(QFont.Weight.Bold)
        self.labtitle.setFont(font3)
        self.labtitle.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labtitle, 0, 0, 1, 4)

        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(4, 1)

        self.retranslateUi(axisframe)

        QMetaObject.connectSlotsByName(axisframe)
    # setupUi

    def retranslateUi(self, axisframe):
        axisframe.setWindowTitle(QCoreApplication.translate("axisframe", u"axisframe", None))
        self.led001.setText(QCoreApplication.translate("axisframe", u"<html><head/><body><p>driver<br>alarm</p></body></html>", None))
        self.led003.setText(QCoreApplication.translate("axisframe", u"<html><head/><body><p>run servo<br>look</p></body></html>", None))
        self.led005.setText(QCoreApplication.translate("axisframe", u"<html><head/><body><p>positive<br>overtravel</p></body></html>", None))
        self.led002.setText(QCoreApplication.translate("axisframe", u"<html><head/><body><p>main<br>power</p></body></html>", None))
        self.label_1.setText(QCoreApplication.translate("axisframe", u"position", None))
        self.label_2.setText(QCoreApplication.translate("axisframe", u"coppia", None))
        self.label_3.setText(QCoreApplication.translate("axisframe", u"velocit\u00e0", None))
        self.lab001.setText(QCoreApplication.translate("axisframe", u"0.00", None))
        self.lab002.setText(QCoreApplication.translate("axisframe", u"0.00", None))
        self.lab003.setText(QCoreApplication.translate("axisframe", u"0.00", None))
        self.lab005.setText(QCoreApplication.translate("axisframe", u"00", None))
        self.led006.setText(QCoreApplication.translate("axisframe", u"<html><head/><body>axis<br>home</body></html>", None))
        self.led004.setText(QCoreApplication.translate("axisframe", u"<html><head/><body><p>negative<br>overtravel</p></body></html>", None))
        self.lab006.setText(QCoreApplication.translate("axisframe", u"00", None))
        self.label_4.setText(QCoreApplication.translate("axisframe", u"destinaz", None))
        self.lab004.setText(QCoreApplication.translate("axisframe", u"0.00", None))
        self.labtitle.setText(QCoreApplication.translate("axisframe", u"nome asse", None))
    # retranslateUi

