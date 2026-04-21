# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'njstatusframe.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_statusframe(object):
    def setupUi(self, statusframe):
        if not statusframe.objectName():
            statusframe.setObjectName(u"statusframe")
        statusframe.resize(437, 774)
        statusframe.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(statusframe)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_tools = QFrame(statusframe)
        self.frame_tools.setObjectName(u"frame_tools")
        self.frame_tools.setStyleSheet(u"")
        self.frame_tools.setFrameShape(QFrame.Panel)
        self.frame_tools.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_tools)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lb_riga = QLabel(self.frame_tools)
        self.lb_riga.setObjectName(u"lb_riga")
        font = QFont()
        font.setFamily(u"Ubuntu Condensed")
        font.setPointSize(18)
        self.lb_riga.setFont(font)
        self.lb_riga.setFrameShape(QFrame.Panel)
        self.lb_riga.setFrameShadow(QFrame.Sunken)
        self.lb_riga.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lb_riga)

        self.lb_rullo = QLabel(self.frame_tools)
        self.lb_rullo.setObjectName(u"lb_rullo")
        font1 = QFont()
        font1.setFamily(u"Ubuntu Condensed")
        self.lb_rullo.setFont(font1)
        self.lb_rullo.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"background-color: rgb(192, 192, 192);")
        self.lb_rullo.setFrameShadow(QFrame.Plain)
        self.lb_rullo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lb_rullo)

        self.lb_penna = QLabel(self.frame_tools)
        self.lb_penna.setObjectName(u"lb_penna")
        self.lb_penna.setFont(font1)
        self.lb_penna.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"background-color: rgb(192, 192, 192);")
        self.lb_penna.setFrameShadow(QFrame.Plain)
        self.lb_penna.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lb_penna)

        self.lb_lama = QLabel(self.frame_tools)
        self.lb_lama.setObjectName(u"lb_lama")
        self.lb_lama.setFont(font1)
        self.lb_lama.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"background-color: rgb(192, 192, 192);")
        self.lb_lama.setFrameShadow(QFrame.Plain)
        self.lb_lama.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lb_lama)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 1)

        self.verticalLayout.addWidget(self.frame_tools)

        self.frame_assi = QFrame(statusframe)
        self.frame_assi.setObjectName(u"frame_assi")
        self.frame_assi.setStyleSheet(u"")
        self.frame_assi.setFrameShape(QFrame.Panel)
        self.frame_assi.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_assi)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lb_xrun = QLabel(self.frame_assi)
        self.lb_xrun.setObjectName(u"lb_xrun")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_xrun.sizePolicy().hasHeightForWidth())
        self.lb_xrun.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamily(u"Ubuntu Condensed")
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setWeight(QFont.Weight.Normal)
        self.lb_xrun.setFont(font2)
        self.lb_xrun.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"background-color: rgb(192, 192, 192);")
        self.lb_xrun.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lb_xrun, 0, 2, 1, 1)

        self.lb_xalarm = QLabel(self.frame_assi)
        self.lb_xalarm.setObjectName(u"lb_xalarm")
        sizePolicy.setHeightForWidth(self.lb_xalarm.sizePolicy().hasHeightForWidth())
        self.lb_xalarm.setSizePolicy(sizePolicy)
        self.lb_xalarm.setFont(font2)
        self.lb_xalarm.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"background-color: rgb(192, 192, 192);")
        self.lb_xalarm.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lb_xalarm, 1, 2, 1, 1)

        self.lb_yrun = QLabel(self.frame_assi)
        self.lb_yrun.setObjectName(u"lb_yrun")
        sizePolicy.setHeightForWidth(self.lb_yrun.sizePolicy().hasHeightForWidth())
        self.lb_yrun.setSizePolicy(sizePolicy)
        self.lb_yrun.setFont(font2)
        self.lb_yrun.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"background-color: rgb(192, 192, 192);")
        self.lb_yrun.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lb_yrun, 2, 2, 1, 1)

        self.lb_yalarm = QLabel(self.frame_assi)
        self.lb_yalarm.setObjectName(u"lb_yalarm")
        sizePolicy.setHeightForWidth(self.lb_yalarm.sizePolicy().hasHeightForWidth())
        self.lb_yalarm.setSizePolicy(sizePolicy)
        self.lb_yalarm.setFont(font2)
        self.lb_yalarm.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"background-color: rgb(192, 192, 192);")
        self.lb_yalarm.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lb_yalarm, 3, 2, 1, 1)

        self.lb_crun = QLabel(self.frame_assi)
        self.lb_crun.setObjectName(u"lb_crun")
        sizePolicy.setHeightForWidth(self.lb_crun.sizePolicy().hasHeightForWidth())
        self.lb_crun.setSizePolicy(sizePolicy)
        self.lb_crun.setFont(font2)
        self.lb_crun.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"background-color: rgb(192, 192, 192);")
        self.lb_crun.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lb_crun, 4, 2, 1, 1)

        self.lb_calarm = QLabel(self.frame_assi)
        self.lb_calarm.setObjectName(u"lb_calarm")
        sizePolicy.setHeightForWidth(self.lb_calarm.sizePolicy().hasHeightForWidth())
        self.lb_calarm.setSizePolicy(sizePolicy)
        self.lb_calarm.setFont(font2)
        self.lb_calarm.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"background-color: rgb(192, 192, 192);")
        self.lb_calarm.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lb_calarm, 5, 2, 1, 1)

        self.label = QLabel(self.frame_assi)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setPointSize(24)
        font3.setBold(True)
        font3.setWeight(QFont.Weight.Bold)
        self.label.setFont(font3)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label, 0, 0, 2, 1)

        self.lb_xpos = QLabel(self.frame_assi)
        self.lb_xpos.setObjectName(u"lb_xpos")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(3)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lb_xpos.sizePolicy().hasHeightForWidth())
        self.lb_xpos.setSizePolicy(sizePolicy1)
        font4 = QFont()
        font4.setFamily(u"Digital")
        font4.setPointSize(28)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(QFont.Weight.Normal)
        self.lb_xpos.setFont(font4)
        self.lb_xpos.setStyleSheet(u"background-color: rgb(0, 85, 0);\n"
"color: rgb(85, 255, 127);")
        self.lb_xpos.setFrameShape(QFrame.Panel)
        self.lb_xpos.setFrameShadow(QFrame.Sunken)
        self.lb_xpos.setScaledContents(False)
        self.lb_xpos.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.lb_xpos, 0, 1, 2, 1)

        self.lb_ypos = QLabel(self.frame_assi)
        self.lb_ypos.setObjectName(u"lb_ypos")
        sizePolicy1.setHeightForWidth(self.lb_ypos.sizePolicy().hasHeightForWidth())
        self.lb_ypos.setSizePolicy(sizePolicy1)
        self.lb_ypos.setFont(font4)
        self.lb_ypos.setStyleSheet(u"background-color: rgb(0, 85, 0);\n"
"color: rgb(85, 255, 127);")
        self.lb_ypos.setFrameShape(QFrame.Panel)
        self.lb_ypos.setFrameShadow(QFrame.Sunken)
        self.lb_ypos.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.lb_ypos, 2, 1, 2, 1)

        self.label_6 = QLabel(self.frame_assi)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setFont(font3)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_6, 2, 0, 2, 1)

        self.label_7 = QLabel(self.frame_assi)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setFont(font3)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_7, 4, 0, 2, 1)

        self.lb_cpos = QLabel(self.frame_assi)
        self.lb_cpos.setObjectName(u"lb_cpos")
        sizePolicy1.setHeightForWidth(self.lb_cpos.sizePolicy().hasHeightForWidth())
        self.lb_cpos.setSizePolicy(sizePolicy1)
        self.lb_cpos.setFont(font4)
        self.lb_cpos.setStyleSheet(u"background-color: rgb(0, 85, 0);\n"
"color: rgb(85, 255, 127);")
        self.lb_cpos.setFrameShape(QFrame.Panel)
        self.lb_cpos.setFrameShadow(QFrame.Sunken)
        self.lb_cpos.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.lb_cpos, 4, 1, 2, 1)

        self.gridLayout_3.setColumnStretch(1, 3)
        self.gridLayout_3.setColumnStretch(2, 1)

        self.verticalLayout.addWidget(self.frame_assi)

        self.frame_bottoni = QFrame(statusframe)
        self.frame_bottoni.setObjectName(u"frame_bottoni")
        self.frame_bottoni.setStyleSheet(u"")
        self.frame_bottoni.setFrameShape(QFrame.Panel)
        self.frame_bottoni.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_bottoni)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.btAUTO = QPushButton(self.frame_bottoni)
        self.btAUTO.setObjectName(u"btAUTO")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btAUTO.sizePolicy().hasHeightForWidth())
        self.btAUTO.setSizePolicy(sizePolicy2)
        font5 = QFont()
        font5.setFamily(u"Ubuntu")
        font5.setPointSize(18)
        font5.setBold(True)
        font5.setWeight(QFont.Weight.Bold)
        self.btAUTO.setFont(font5)
        self.btAUTO.setCheckable(False)

        self.gridLayout_4.addWidget(self.btAUTO, 0, 0, 2, 1)

        self.lbover1 = QLabel(self.frame_bottoni)
        self.lbover1.setObjectName(u"lbover1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lbover1.sizePolicy().hasHeightForWidth())
        self.lbover1.setSizePolicy(sizePolicy3)

        self.gridLayout_4.addWidget(self.lbover1, 0, 1, 1, 1)

        self.SB01 = QSpinBox(self.frame_bottoni)
        self.SB01.setObjectName(u"SB01")
        font6 = QFont()
        font6.setFamily(u"Ubuntu")
        font6.setPointSize(18)
        font6.setBold(False)
        font6.setWeight(QFont.Weight.Normal)
        self.SB01.setFont(font6)
        self.SB01.setFrame(True)
        self.SB01.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.SB01.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.SB01.setMinimum(1)
        self.SB01.setMaximum(100)
        self.SB01.setValue(10)

        self.gridLayout_4.addWidget(self.SB01, 1, 1, 1, 1)

        self.btMANUAL = QPushButton(self.frame_bottoni)
        self.btMANUAL.setObjectName(u"btMANUAL")
        sizePolicy2.setHeightForWidth(self.btMANUAL.sizePolicy().hasHeightForWidth())
        self.btMANUAL.setSizePolicy(sizePolicy2)
        self.btMANUAL.setFont(font5)
        self.btMANUAL.setCheckable(False)

        self.gridLayout_4.addWidget(self.btMANUAL, 2, 0, 2, 1)

        self.lbover2 = QLabel(self.frame_bottoni)
        self.lbover2.setObjectName(u"lbover2")
        sizePolicy3.setHeightForWidth(self.lbover2.sizePolicy().hasHeightForWidth())
        self.lbover2.setSizePolicy(sizePolicy3)
        self.lbover2.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lbover2, 2, 1, 1, 1)

        self.SB02 = QSpinBox(self.frame_bottoni)
        self.SB02.setObjectName(u"SB02")
        self.SB02.setFont(font6)
        self.SB02.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.SB02.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.SB02.setMinimum(1)
        self.SB02.setMaximum(100)
        self.SB02.setValue(10)

        self.gridLayout_4.addWidget(self.SB02, 3, 1, 1, 1)

        self.gridLayout_4.setColumnStretch(0, 2)
        self.gridLayout_4.setColumnStretch(1, 1)

        self.verticalLayout_2.addLayout(self.gridLayout_4)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btSTART = QPushButton(self.frame_bottoni)
        self.btSTART.setObjectName(u"btSTART")
        self.btSTART.setMinimumSize(QSize(0, 48))
        self.btSTART.setFont(font5)
        self.btSTART.setCheckable(False)

        self.horizontalLayout_4.addWidget(self.btSTART)

        self.btHOLD = QPushButton(self.frame_bottoni)
        self.btHOLD.setObjectName(u"btHOLD")
        self.btHOLD.setMinimumSize(QSize(0, 48))
        self.btHOLD.setFont(font5)
        self.btHOLD.setCheckable(False)

        self.horizontalLayout_4.addWidget(self.btHOLD)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btRESET = QPushButton(self.frame_bottoni)
        self.btRESET.setObjectName(u"btRESET")
        self.btRESET.setMinimumSize(QSize(0, 48))
        font7 = QFont()
        font7.setFamily(u"Ubuntu Condensed")
        font7.setPointSize(14)
        font7.setBold(False)
        font7.setWeight(QFont.Weight.Normal)
        self.btRESET.setFont(font7)
        self.btRESET.setCheckable(False)

        self.horizontalLayout_5.addWidget(self.btRESET)

        self.btHOMING = QPushButton(self.frame_bottoni)
        self.btHOMING.setObjectName(u"btHOMING")
        self.btHOMING.setMinimumSize(QSize(0, 48))
        self.btHOMING.setFont(font7)
        self.btHOMING.setCheckable(False)

        self.horizontalLayout_5.addWidget(self.btHOMING)

        self.btMODE = QPushButton(self.frame_bottoni)
        self.btMODE.setObjectName(u"btMODE")
        self.btMODE.setMinimumSize(QSize(0, 48))
        self.btMODE.setFont(font7)

        self.horizontalLayout_5.addWidget(self.btMODE)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)


        self.verticalLayout.addWidget(self.frame_bottoni)

        self.frame_spie = QFrame(statusframe)
        self.frame_spie.setObjectName(u"frame_spie")
        self.frame_spie.setStyleSheet(u"")
        self.frame_spie.setFrameShape(QFrame.Panel)
        self.frame_spie.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_spie)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lb_homing = QLabel(self.frame_spie)
        self.lb_homing.setObjectName(u"lb_homing")
        font8 = QFont()
        font8.setFamily(u"Monospace")
        font8.setPointSize(20)
        font8.setBold(False)
        font8.setWeight(QFont.Weight.Normal)
        self.lb_homing.setFont(font8)
        self.lb_homing.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"background-color: rgb(192, 192, 192);")
        self.lb_homing.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_homing, 2, 0, 1, 3)

        self.lb_ecterror = QLabel(self.frame_spie)
        self.lb_ecterror.setObjectName(u"lb_ecterror")
        self.lb_ecterror.setFont(font7)
        self.lb_ecterror.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"background-color: rgb(192, 192, 192);")
        self.lb_ecterror.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_ecterror, 3, 0, 1, 1)

        self.lb_mcerror = QLabel(self.frame_spie)
        self.lb_mcerror.setObjectName(u"lb_mcerror")
        self.lb_mcerror.setFont(font7)
        self.lb_mcerror.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"background-color: rgb(192, 192, 192);")
        self.lb_mcerror.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_mcerror, 3, 1, 1, 1)

        self.lb_plcerror = QLabel(self.frame_spie)
        self.lb_plcerror.setObjectName(u"lb_plcerror")
        self.lb_plcerror.setFont(font7)
        self.lb_plcerror.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"background-color: rgb(192, 192, 192);")
        self.lb_plcerror.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_plcerror, 3, 2, 1, 1)

        self.lb_emergenza = QLabel(self.frame_spie)
        self.lb_emergenza.setObjectName(u"lb_emergenza")
        self.lb_emergenza.setFont(font8)
        self.lb_emergenza.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"background-color: rgb(192, 192, 192);")
        self.lb_emergenza.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_emergenza, 1, 0, 1, 3)

        self.lb_endread = QLabel(self.frame_spie)
        self.lb_endread.setObjectName(u"lb_endread")
        self.lb_endread.setFont(font7)
        self.lb_endread.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"background-color: rgb(192, 192, 192);")
        self.lb_endread.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_endread, 4, 0, 1, 3)


        self.verticalLayout.addWidget(self.frame_spie)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(statusframe)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.btCaricaCsv = QPushButton(statusframe)
        self.btCaricaCsv.setObjectName(u"btCaricaCsv")
        sizePolicy2.setHeightForWidth(self.btCaricaCsv.sizePolicy().hasHeightForWidth())
        self.btCaricaCsv.setSizePolicy(sizePolicy2)
        self.btCaricaCsv.setFont(font5)

        self.gridLayout.addWidget(self.btCaricaCsv, 0, 1, 2, 1)

        self.csv_start_point = QSpinBox(statusframe)
        self.csv_start_point.setObjectName(u"csv_start_point")
        font9 = QFont()
        font9.setFamily(u"Ubuntu")
        font9.setPointSize(18)
        self.csv_start_point.setFont(font9)
        self.csv_start_point.setWrapping(False)
        self.csv_start_point.setFrame(True)
        self.csv_start_point.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.csv_start_point.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.csv_start_point.setMaximum(32700)

        self.gridLayout.addWidget(self.csv_start_point, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalLayout.setStretch(3, 1)
#if QT_CONFIG(shortcut)
        self.label_2.setBuddy(self.csv_start_point)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.btAUTO, self.btMANUAL)
        QWidget.setTabOrder(self.btMANUAL, self.btSTART)
        QWidget.setTabOrder(self.btSTART, self.btHOLD)
        QWidget.setTabOrder(self.btHOLD, self.btRESET)
        QWidget.setTabOrder(self.btRESET, self.btHOMING)
        QWidget.setTabOrder(self.btHOMING, self.btMODE)
        QWidget.setTabOrder(self.btMODE, self.SB01)
        QWidget.setTabOrder(self.SB01, self.SB02)
        QWidget.setTabOrder(self.SB02, self.csv_start_point)
        QWidget.setTabOrder(self.csv_start_point, self.btCaricaCsv)

        self.retranslateUi(statusframe)

        QMetaObject.connectSlotsByName(statusframe)
    # setupUi

    def retranslateUi(self, statusframe):
        statusframe.setWindowTitle(QCoreApplication.translate("statusframe", u"Frame", None))
        self.lb_riga.setText(QCoreApplication.translate("statusframe", u"000000", None))
        self.lb_rullo.setText(QCoreApplication.translate("statusframe", u"rullo", None))
        self.lb_penna.setText(QCoreApplication.translate("statusframe", u"penna", None))
        self.lb_lama.setText(QCoreApplication.translate("statusframe", u"lama", None))
        self.lb_xrun.setText(QCoreApplication.translate("statusframe", u"RUN", None))
        self.lb_xalarm.setText(QCoreApplication.translate("statusframe", u"ALARM", None))
        self.lb_yrun.setText(QCoreApplication.translate("statusframe", u"RUN", None))
        self.lb_yalarm.setText(QCoreApplication.translate("statusframe", u"ALARM", None))
        self.lb_crun.setText(QCoreApplication.translate("statusframe", u"RUN", None))
        self.lb_calarm.setText(QCoreApplication.translate("statusframe", u"ALARM", None))
        self.label.setText(QCoreApplication.translate("statusframe", u"<html><head/><body><p><span style=\" color:#00557f;\">X<br/></span><span style=\" font-size:8pt; color:#00557f;\">mm</span></p></body></html>", None))
        self.lb_xpos.setText(QCoreApplication.translate("statusframe", u"0.00", None))
        self.lb_ypos.setText(QCoreApplication.translate("statusframe", u"0.00", None))
        self.label_6.setText(QCoreApplication.translate("statusframe", u"<html><head/><body><p><span style=\" color:#00557f;\">Y<br/></span><span style=\" font-size:8pt; color:#00557f;\">mm</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("statusframe", u"<html><head/><body><p><span style=\" color:#00557f;\">C<br/></span><span style=\" font-size:8pt; color:#00557f;\">gradi</span></p></body></html>", None))
        self.lb_cpos.setText(QCoreApplication.translate("statusframe", u"0.00", None))
        self.btAUTO.setText(QCoreApplication.translate("statusframe", u"AUTO", None))
        self.lbover1.setText(QCoreApplication.translate("statusframe", u"<html><head/><body><p><span style=\" font-size:8pt; color:#00557f;\">OVERRIDE AUTO</span></p></body></html>", None))
        self.btMANUAL.setText(QCoreApplication.translate("statusframe", u"MANUAL", None))
        self.lbover2.setText(QCoreApplication.translate("statusframe", u"<html><head/><body><p><span style=\" font-size:8pt; color:#00557f;\">OVERRIDE MAN</span></p></body></html>", None))
        self.btSTART.setText(QCoreApplication.translate("statusframe", u"START", None))
        self.btHOLD.setText(QCoreApplication.translate("statusframe", u"HOLD", None))
        self.btRESET.setText(QCoreApplication.translate("statusframe", u"RESET", None))
        self.btHOMING.setText(QCoreApplication.translate("statusframe", u"HOMING", None))
        self.btMODE.setText(QCoreApplication.translate("statusframe", u"TM OFF", None))
        self.lb_homing.setText(QCoreApplication.translate("statusframe", u"HOMING ESEGUITO", None))
        self.lb_ecterror.setText(QCoreApplication.translate("statusframe", u"ECT ERR", None))
        self.lb_mcerror.setText(QCoreApplication.translate("statusframe", u"MC ERR", None))
        self.lb_plcerror.setText(QCoreApplication.translate("statusframe", u"PLC ERR", None))
        self.lb_emergenza.setText(QCoreApplication.translate("statusframe", u"EMERGENZA", None))
        self.lb_endread.setText(QCoreApplication.translate("statusframe", u"FILE CSV CARICATO", None))
        self.label_2.setText(QCoreApplication.translate("statusframe", u"<html><head/><body><p><span style=\" font-size:8pt; color:#00557f;\">PUNTO INIZIALE</span></p></body></html>", None))
        self.btCaricaCsv.setText(QCoreApplication.translate("statusframe", u"RICARICA CSV", None))
    # retranslateUi

