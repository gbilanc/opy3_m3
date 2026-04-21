# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainapp.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from .axis import Axis
from .gvplotter import GVPlotter
from .njstatus import NjStatus


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 712)
        self.actionAcquisisci_dxf = QAction(MainWindow)
        self.actionAcquisisci_dxf.setObjectName(u"actionAcquisisci_dxf")
        icon = QIcon()
        icon.addFile(u":/img/res/open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAcquisisci_dxf.setIcon(icon)
        self.actionFine_lavoro = QAction(MainWindow)
        self.actionFine_lavoro.setObjectName(u"actionFine_lavoro")
        icon1 = QIcon()
        icon1.addFile(u":/img/res/exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionFine_lavoro.setIcon(icon1)
        self.actionStartMonitor = QAction(MainWindow)
        self.actionStartMonitor.setObjectName(u"actionStartMonitor")
        icon2 = QIcon()
        icon2.addFile(u":/img/res/up-and-down.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionStartMonitor.setIcon(icon2)
        self.actionStopMonitor = QAction(MainWindow)
        self.actionStopMonitor.setObjectName(u"actionStopMonitor")
        icon3 = QIcon()
        icon3.addFile(u":/img/res/no.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionStopMonitor.setIcon(icon3)
        self.actionSimula_plotter = QAction(MainWindow)
        self.actionSimula_plotter.setObjectName(u"actionSimula_plotter")
        icon4 = QIcon()
        icon4.addFile(u":/img/res/preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSimula_plotter.setIcon(icon4)
        self.actionInformazioni = QAction(MainWindow)
        self.actionInformazioni.setObjectName(u"actionInformazioni")
        icon5 = QIcon()
        icon5.addFile(u":/img/res/about_(info).png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionInformazioni.setIcon(icon5)
        self.actionImpostazioni = QAction(MainWindow)
        self.actionImpostazioni.setObjectName(u"actionImpostazioni")
        icon6 = QIcon()
        icon6.addFile(u":/img/res/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionImpostazioni.setIcon(icon6)
        self.actionAaaa = QAction(MainWindow)
        self.actionAaaa.setObjectName(u"actionAaaa")
        self.actionFile2 = QAction(MainWindow)
        self.actionFile2.setObjectName(u"actionFile2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.plotter = GVPlotter(self.widget)
        self.plotter.setObjectName(u"plotter")

        self.verticalLayout.addWidget(self.plotter)

        self.progBar1 = QProgressBar(self.widget)
        self.progBar1.setObjectName(u"progBar1")
        self.progBar1.setValue(0)
        self.progBar1.setTextVisible(False)

        self.verticalLayout.addWidget(self.progBar1)


        self.horizontalLayout.addWidget(self.widget)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(360, 0))
        font = QFont()
        font.setFamily(u"Courier 10 Pitch")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(QFont.Weight.Bold)
        font.setKerning(True)
        self.tabWidget.setFont(font)
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.gridLayout_2 = QGridLayout(self.tab_1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tableWidget_layers = QTableWidget(self.tab_1)
        if (self.tableWidget_layers.columnCount() < 4):
            self.tableWidget_layers.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_layers.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_layers.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_layers.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_layers.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget_layers.setObjectName(u"tableWidget_layers")
        font1 = QFont()
        font1.setFamily(u"Liberation Mono")
        font1.setPointSize(10)
        self.tableWidget_layers.setFont(font1)
        self.tableWidget_layers.horizontalHeader().setDefaultSectionSize(75)

        self.gridLayout_2.addWidget(self.tableWidget_layers, 0, 0, 1, 3)

        self.tableWidget_colors = QTableWidget(self.tab_1)
        if (self.tableWidget_colors.columnCount() < 4):
            self.tableWidget_colors.setColumnCount(4)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_colors.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_colors.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_colors.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_colors.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        self.tableWidget_colors.setObjectName(u"tableWidget_colors")
        self.tableWidget_colors.setFont(font1)
        self.tableWidget_colors.horizontalHeader().setDefaultSectionSize(75)

        self.gridLayout_2.addWidget(self.tableWidget_colors, 1, 0, 1, 3)

        self.rbPenna = QRadioButton(self.tab_1)
        self.rbPenna.setObjectName(u"rbPenna")
        font2 = QFont()
        font2.setFamily(u"Courier 10 Pitch")
        font2.setPointSize(14)
        self.rbPenna.setFont(font2)
        self.rbPenna.setStyleSheet(u"border: 1px solid blue; \n"
"border-radius: 5px; ")
        self.rbPenna.setChecked(True)

        self.gridLayout_2.addWidget(self.rbPenna, 2, 0, 1, 1)

        self.rbLama = QRadioButton(self.tab_1)
        self.rbLama.setObjectName(u"rbLama")
        self.rbLama.setFont(font2)
        self.rbLama.setStyleSheet(u"border: 1px solid blue; \n"
"border-radius: 5px; ")

        self.gridLayout_2.addWidget(self.rbLama, 2, 1, 1, 1)

        self.rbRullo = QRadioButton(self.tab_1)
        self.rbRullo.setObjectName(u"rbRullo")
        self.rbRullo.setFont(font2)
        self.rbRullo.setStyleSheet(u"border: 1px solid blue; \n"
"border-radius: 5px; ")

        self.gridLayout_2.addWidget(self.rbRullo, 2, 2, 1, 1)

        self.cbxcolor = QCheckBox(self.tab_1)
        self.cbxcolor.setObjectName(u"cbxcolor")
        font3 = QFont()
        font3.setPointSize(14)
        self.cbxcolor.setFont(font3)
        self.cbxcolor.setStyleSheet(u"border: 1px solid green; \n"
"border-radius: 5px; ")

        self.gridLayout_2.addWidget(self.cbxcolor, 3, 0, 1, 3)

        self.btGeneraCsv = QPushButton(self.tab_1)
        self.btGeneraCsv.setObjectName(u"btGeneraCsv")
        self.btGeneraCsv.setFont(font2)
        icon7 = QIcon()
        icon7.addFile(u":/img/res/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btGeneraCsv.setIcon(icon7)
        self.btGeneraCsv.setIconSize(QSize(48, 48))

        self.gridLayout_2.addWidget(self.btGeneraCsv, 4, 0, 1, 3)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_6 = QVBoxLayout(self.tab_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.push_origine = QPushButton(self.tab_2)
        self.push_origine.setObjectName(u"push_origine")
        font4 = QFont()
        font4.setFamily(u"Courier 10 Pitch")
        font4.setPointSize(14)
        font4.setBold(True)
        font4.setWeight(QFont.Weight.Bold)
        self.push_origine.setFont(font4)
        icon8 = QIcon()
        icon8.addFile(u":/img/res/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.push_origine.setIcon(icon8)
        self.push_origine.setIconSize(QSize(48, 48))

        self.verticalLayout_6.addWidget(self.push_origine)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_Y = QLineEdit(self.tab_2)
        self.lineEdit_Y.setObjectName(u"lineEdit_Y")
        font5 = QFont()
        font5.setFamily(u"Monospace")
        font5.setPointSize(20)
        font5.setBold(True)
        font5.setWeight(QFont.Weight.Bold)
        self.lineEdit_Y.setFont(font5)
        self.lineEdit_Y.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lineEdit_Y, 1, 1, 1, 1)

        self.lineEdit_X = QLineEdit(self.tab_2)
        self.lineEdit_X.setObjectName(u"lineEdit_X")
        self.lineEdit_X.setFont(font5)
        self.lineEdit_X.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lineEdit_X, 0, 1, 1, 1)

        self.label_Y = QLabel(self.tab_2)
        self.label_Y.setObjectName(u"label_Y")
        font6 = QFont()
        font6.setFamily(u"Courier 10 Pitch")
        font6.setPointSize(10)
        font6.setBold(True)
        font6.setWeight(QFont.Weight.Bold)
        self.label_Y.setFont(font6)
        self.label_Y.setStyleSheet(u"background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 255, 127);")
        self.label_Y.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_Y, 1, 0, 1, 1)

        self.label_X = QLabel(self.tab_2)
        self.label_X.setObjectName(u"label_X")
        self.label_X.setFont(font6)
        self.label_X.setStyleSheet(u"background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 255, 127);")
        self.label_X.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_X, 0, 0, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)

        self.verticalLayout_6.addLayout(self.gridLayout)

        self.push_move = QPushButton(self.tab_2)
        self.push_move.setObjectName(u"push_move")
        self.push_move.setFont(font4)
        self.push_move.setLayoutDirection(Qt.LeftToRight)
        icon9 = QIcon()
        icon9.addFile(u":/img/res/move-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.push_move.setIcon(icon9)
        self.push_move.setIconSize(QSize(48, 48))

        self.verticalLayout_6.addWidget(self.push_move)

        self.push_rotate = QPushButton(self.tab_2)
        self.push_rotate.setObjectName(u"push_rotate")
        self.push_rotate.setFont(font4)
        icon10 = QIcon()
        icon10.addFile(u":/img/res/update.png", QSize(), QIcon.Normal, QIcon.Off)
        self.push_rotate.setIcon(icon10)
        self.push_rotate.setIconSize(QSize(48, 48))

        self.verticalLayout_6.addWidget(self.push_rotate)

        self.push_invertX = QPushButton(self.tab_2)
        self.push_invertX.setObjectName(u"push_invertX")
        self.push_invertX.setFont(font4)
        icon11 = QIcon()
        icon11.addFile(u":/img/res/right-and-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.push_invertX.setIcon(icon11)
        self.push_invertX.setIconSize(QSize(48, 48))

        self.verticalLayout_6.addWidget(self.push_invertX)

        self.push_invertY = QPushButton(self.tab_2)
        self.push_invertY.setObjectName(u"push_invertY")
        self.push_invertY.setFont(font4)
        self.push_invertY.setIcon(icon2)
        self.push_invertY.setIconSize(QSize(48, 48))

        self.verticalLayout_6.addWidget(self.push_invertY)

        self.verticalSpacer = QSpacerItem(20, 243, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_4 = QVBoxLayout(self.tab_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.njstatus = NjStatus(self.tab_3)
        self.njstatus.setObjectName(u"njstatus")

        self.verticalLayout_4.addWidget(self.njstatus)

        self.verticalLayout_4.setStretch(0, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_5 = QVBoxLayout(self.tab_4)
        self.verticalLayout_5.setSpacing(12)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.axis_x = Axis(self.tab_4)
        self.axis_x.setObjectName(u"axis_x")
        self.axis_x.setMinimumSize(QSize(0, 150))
        self.axis_x.setFrameShape(QFrame.Panel)
        self.axis_x.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.axis_x)

        self.axis_y = Axis(self.tab_4)
        self.axis_y.setObjectName(u"axis_y")
        self.axis_y.setMinimumSize(QSize(0, 150))
        self.axis_y.setFrameShape(QFrame.Panel)
        self.axis_y.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.axis_y)

        self.axis_z = Axis(self.tab_4)
        self.axis_z.setObjectName(u"axis_z")
        self.axis_z.setMinimumSize(QSize(0, 150))
        self.axis_z.setFrameShape(QFrame.Panel)
        self.axis_z.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.axis_z)

        self.tabWidget.addTab(self.tab_4, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 25))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuFiles_Recenti = QMenu(self.menuFile)
        self.menuFiles_Recenti.setObjectName(u"menuFiles_Recenti")
        icon12 = QIcon()
        icon12.addFile(u":/img/res/document.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menuFiles_Recenti.setIcon(icon12)
        self.menuInfo = QMenu(self.menubar)
        self.menuInfo.setObjectName(u"menuInfo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
#if QT_CONFIG(shortcut)
        self.label_Y.setBuddy(self.lineEdit_Y)
        self.label_X.setBuddy(self.lineEdit_X)
#endif // QT_CONFIG(shortcut)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuInfo.menuAction())
        self.menuFile.addAction(self.actionAcquisisci_dxf)
        self.menuFile.addAction(self.menuFiles_Recenti.menuAction())
        self.menuFile.addAction(self.actionSimula_plotter)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionFine_lavoro)
        self.menuFiles_Recenti.addAction(self.actionAaaa)
        self.menuFiles_Recenti.addAction(self.actionFile2)
        self.menuInfo.addAction(self.actionImpostazioni)
        self.menuInfo.addAction(self.actionInformazioni)

        self.retranslateUi(MainWindow)
        self.actionFine_lavoro.triggered.connect(MainWindow.close)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"omronpy.m2", None))
        self.actionAcquisisci_dxf.setText(QCoreApplication.translate("MainWindow", u"Acquisisci dxf", None))
        self.actionFine_lavoro.setText(QCoreApplication.translate("MainWindow", u"Fine lavoro", None))
        self.actionStartMonitor.setText(QCoreApplication.translate("MainWindow", u"StartMonitor", None))
        self.actionStopMonitor.setText(QCoreApplication.translate("MainWindow", u"StopMonitor", None))
        self.actionSimula_plotter.setText(QCoreApplication.translate("MainWindow", u"Simula plotter", None))
        self.actionInformazioni.setText(QCoreApplication.translate("MainWindow", u"Informazioni", None))
        self.actionImpostazioni.setText(QCoreApplication.translate("MainWindow", u"Impostazioni", None))
        self.actionAaaa.setText(QCoreApplication.translate("MainWindow", u"file1", None))
        self.actionFile2.setText(QCoreApplication.translate("MainWindow", u"file2", None))
        ___qtablewidgetitem = self.tableWidget_layers.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"layer", None));
        ___qtablewidgetitem1 = self.tableWidget_layers.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"mostra", None));
        ___qtablewidgetitem2 = self.tableWidget_layers.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"genera", None));
        ___qtablewidgetitem3 = self.tableWidget_layers.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"inverti", None));
        ___qtablewidgetitem4 = self.tableWidget_colors.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"colore", None));
        ___qtablewidgetitem5 = self.tableWidget_colors.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"passo", None));
        ___qtablewidgetitem6 = self.tableWidget_colors.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"ordine", None));
        ___qtablewidgetitem7 = self.tableWidget_colors.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"genera", None));
        self.rbPenna.setText(QCoreApplication.translate("MainWindow", u"penna", None))
        self.rbLama.setText(QCoreApplication.translate("MainWindow", u"lama", None))
        self.rbRullo.setText(QCoreApplication.translate("MainWindow", u"rullo", None))
        self.cbxcolor.setText(QCoreApplication.translate("MainWindow", u"ordina segmenti per colore", None))
        self.btGeneraCsv.setText(QCoreApplication.translate("MainWindow", u"genera csv", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"livelli", None))
        self.push_origine.setText(QCoreApplication.translate("MainWindow", u"LEGGI XY", None))
        self.lineEdit_Y.setInputMask("")
        self.lineEdit_Y.setText(QCoreApplication.translate("MainWindow", u"0.000", None))
        self.lineEdit_X.setInputMask("")
        self.lineEdit_X.setText(QCoreApplication.translate("MainWindow", u"0.000", None))
        self.label_Y.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">Y</span> (metri)</p></body></html>", None))
        self.label_X.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">X</span> (metri)</p></body></html>", None))
        self.push_move.setText(QCoreApplication.translate("MainWindow", u"TRASLA XY", None))
        self.push_rotate.setText(QCoreApplication.translate("MainWindow", u"RUOTA 90'", None))
        self.push_invertX.setText(QCoreApplication.translate("MainWindow", u"ROVESCIA X", None))
        self.push_invertY.setText(QCoreApplication.translate("MainWindow", u"ROVESCIA Y", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"modifiche", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"driver", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"assi", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuFiles_Recenti.setTitle(QCoreApplication.translate("MainWindow", u"Files Recenti", None))
        self.menuInfo.setTitle(QCoreApplication.translate("MainWindow", u"Opzioni", None))
    # retranslateUi

