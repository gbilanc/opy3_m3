# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QDoubleSpinBox, QGridLayout, QGroupBox, QHeaderView,
    QLabel, QLineEdit, QSizePolicy, QSpacerItem,
    QSpinBox, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_DialogSettings(object):
    def setupUi(self, DialogSettings):
        if not DialogSettings.objectName():
            DialogSettings.setObjectName(u"DialogSettings")
        DialogSettings.resize(600, 600)
        self.verticalLayout_3 = QVBoxLayout(DialogSettings)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tabWidget = QTabWidget(DialogSettings)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.verticalLayout = QVBoxLayout(self.tab_1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_4 = QGroupBox(self.tab_1)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_2 = QGridLayout(self.groupBox_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.groupBox_4)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Courier 10 Pitch"])
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 255, 127);")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.lineEditUrlPlc = QLineEdit(self.groupBox_4)
        self.lineEditUrlPlc.setObjectName(u"lineEditUrlPlc")
        self.lineEditUrlPlc.setFont(font)

        self.gridLayout_2.addWidget(self.lineEditUrlPlc, 1, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 255, 127);")

        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)

        self.spinBoxPortaPlc = QSpinBox(self.groupBox_4)
        self.spinBoxPortaPlc.setObjectName(u"spinBoxPortaPlc")
        self.spinBoxPortaPlc.setFont(font)
        self.spinBoxPortaPlc.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBoxPortaPlc.setMaximum(32000)
        self.spinBoxPortaPlc.setValue(9600)

        self.gridLayout_2.addWidget(self.spinBoxPortaPlc, 1, 1, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 2)
        self.gridLayout_2.setColumnStretch(1, 1)

        self.verticalLayout.addWidget(self.groupBox_4)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.groupBox_5 = QGroupBox(self.tab_1)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_5 = QGridLayout(self.groupBox_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_9 = QLabel(self.groupBox_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 255, 127);")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_9, 0, 0, 1, 1)

        self.doubleSpinBox_maxx = QDoubleSpinBox(self.groupBox_5)
        self.doubleSpinBox_maxx.setObjectName(u"doubleSpinBox_maxx")
        self.doubleSpinBox_maxx.setFont(font)
        self.doubleSpinBox_maxx.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_maxx.setMaximum(99999.000000000000000)
        self.doubleSpinBox_maxx.setValue(1500.000000000000000)

        self.gridLayout_5.addWidget(self.doubleSpinBox_maxx, 0, 1, 2, 1)

        self.label_14 = QLabel(self.groupBox_5)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(u"background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 255, 127);")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_14, 0, 2, 1, 1)

        self.doubleSpinBox_maxy = QDoubleSpinBox(self.groupBox_5)
        self.doubleSpinBox_maxy.setObjectName(u"doubleSpinBox_maxy")
        self.doubleSpinBox_maxy.setFont(font)
        self.doubleSpinBox_maxy.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_maxy.setMaximum(99999.000000000000000)
        self.doubleSpinBox_maxy.setValue(600.000000000000000)

        self.gridLayout_5.addWidget(self.doubleSpinBox_maxy, 0, 3, 1, 1)

        self.doubleSpinBoxScala = QDoubleSpinBox(self.groupBox_5)
        self.doubleSpinBoxScala.setObjectName(u"doubleSpinBoxScala")
        self.doubleSpinBoxScala.setFont(font)
        self.doubleSpinBoxScala.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBoxScala.setMinimum(1.000000000000000)
        self.doubleSpinBoxScala.setMaximum(1000.000000000000000)
        self.doubleSpinBoxScala.setValue(100.000000000000000)

        self.gridLayout_5.addWidget(self.doubleSpinBoxScala, 1, 2, 2, 2)

        self.label_4 = QLabel(self.groupBox_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 255, 127);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_4, 2, 0, 1, 2)

        self.gridLayout_5.setColumnStretch(0, 1)
        self.gridLayout_5.setColumnStretch(1, 2)
        self.gridLayout_5.setColumnStretch(2, 1)
        self.gridLayout_5.setColumnStretch(3, 2)

        self.verticalLayout.addWidget(self.groupBox_5)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.groupBox_6 = QGroupBox(self.tab_1)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_6 = QGridLayout(self.groupBox_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_10 = QLabel(self.groupBox_6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 255, 127);")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_10, 0, 0, 1, 1)

        self.doubleSpinBox_stopx = QDoubleSpinBox(self.groupBox_6)
        self.doubleSpinBox_stopx.setObjectName(u"doubleSpinBox_stopx")
        self.doubleSpinBox_stopx.setFont(font)
        self.doubleSpinBox_stopx.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_stopx.setMaximum(99999.000000000000000)

        self.gridLayout_6.addWidget(self.doubleSpinBox_stopx, 0, 1, 1, 1)

        self.label_15 = QLabel(self.groupBox_6)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)
        self.label_15.setStyleSheet(u"background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 255, 127);")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_15, 0, 2, 1, 1)

        self.doubleSpinBox_stopy = QDoubleSpinBox(self.groupBox_6)
        self.doubleSpinBox_stopy.setObjectName(u"doubleSpinBox_stopy")
        self.doubleSpinBox_stopy.setFont(font)
        self.doubleSpinBox_stopy.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_stopy.setMaximum(99999.000000000000000)

        self.gridLayout_6.addWidget(self.doubleSpinBox_stopy, 0, 3, 1, 1)

        self.gridLayout_6.setColumnStretch(0, 1)
        self.gridLayout_6.setColumnStretch(2, 1)

        self.verticalLayout.addWidget(self.groupBox_6)

        self.verticalSpacer = QSpacerItem(20, 93, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_4 = QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox = QGroupBox(self.tab_2)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 255, 127);")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setMargin(0)

        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)

        self.doubleSpinBoxPennaX = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBoxPennaX.setObjectName(u"doubleSpinBoxPennaX")
        self.doubleSpinBoxPennaX.setFont(font)
        self.doubleSpinBoxPennaX.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBoxPennaX.setDecimals(2)
        self.doubleSpinBoxPennaX.setMinimum(-500.000000000000000)
        self.doubleSpinBoxPennaX.setMaximum(500.000000000000000)
        self.doubleSpinBoxPennaX.setValue(0.000000000000000)

        self.gridLayout.addWidget(self.doubleSpinBoxPennaX, 0, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 255, 127);")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setMargin(0)

        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)

        self.doubleSpinBoxPennaY = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBoxPennaY.setObjectName(u"doubleSpinBoxPennaY")
        self.doubleSpinBoxPennaY.setFont(font)
        self.doubleSpinBoxPennaY.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBoxPennaY.setDecimals(2)
        self.doubleSpinBoxPennaY.setMinimum(-500.000000000000000)
        self.doubleSpinBoxPennaY.setMaximum(500.000000000000000)
        self.doubleSpinBoxPennaY.setValue(0.000000000000000)

        self.gridLayout.addWidget(self.doubleSpinBoxPennaY, 0, 3, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 2)

        self.verticalLayout_4.addWidget(self.groupBox)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_5)

        self.groupBox_2 = QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 255, 127);")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setMargin(0)

        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)

        self.doubleSpinBoxLaserX = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBoxLaserX.setObjectName(u"doubleSpinBoxLaserX")
        self.doubleSpinBoxLaserX.setFont(font)
        self.doubleSpinBoxLaserX.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBoxLaserX.setDecimals(2)
        self.doubleSpinBoxLaserX.setMinimum(-500.000000000000000)
        self.doubleSpinBoxLaserX.setMaximum(500.000000000000000)
        self.doubleSpinBoxLaserX.setValue(0.000000000000000)

        self.gridLayout_3.addWidget(self.doubleSpinBoxLaserX, 0, 1, 1, 1)

        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(u"background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 255, 127);")
        self.label_11.setAlignment(Qt.AlignCenter)
        self.label_11.setMargin(0)

        self.gridLayout_3.addWidget(self.label_11, 0, 2, 1, 1)

        self.doubleSpinBoxLaserY = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBoxLaserY.setObjectName(u"doubleSpinBoxLaserY")
        self.doubleSpinBoxLaserY.setFont(font)
        self.doubleSpinBoxLaserY.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBoxLaserY.setDecimals(2)
        self.doubleSpinBoxLaserY.setMinimum(-500.000000000000000)
        self.doubleSpinBoxLaserY.setMaximum(500.000000000000000)
        self.doubleSpinBoxLaserY.setValue(0.000000000000000)

        self.gridLayout_3.addWidget(self.doubleSpinBoxLaserY, 0, 3, 1, 1)

        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(1, 2)
        self.gridLayout_3.setColumnStretch(2, 1)
        self.gridLayout_3.setColumnStretch(3, 2)

        self.verticalLayout_4.addWidget(self.groupBox_2)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_6)

        self.groupBox_3 = QGroupBox(self.tab_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_4 = QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.doubleSpinBoxRullo = QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBoxRullo.setObjectName(u"doubleSpinBoxRullo")
        self.doubleSpinBoxRullo.setFont(font)
        self.doubleSpinBoxRullo.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBoxRullo.setMaximum(1.000000000000000)
        self.doubleSpinBoxRullo.setSingleStep(0.010000000000000)
        self.doubleSpinBoxRullo.setValue(0.100000000000000)

        self.gridLayout_4.addWidget(self.doubleSpinBoxRullo, 2, 0, 1, 2)

        self.label_12 = QLabel(self.groupBox_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(u"background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 255, 127);")
        self.label_12.setAlignment(Qt.AlignCenter)
        self.label_12.setMargin(0)

        self.gridLayout_4.addWidget(self.label_12, 0, 0, 1, 1)

        self.doubleSpinBoxRulloX = QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBoxRulloX.setObjectName(u"doubleSpinBoxRulloX")
        self.doubleSpinBoxRulloX.setFont(font)
        self.doubleSpinBoxRulloX.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBoxRulloX.setDecimals(2)
        self.doubleSpinBoxRulloX.setMinimum(-500.000000000000000)
        self.doubleSpinBoxRulloX.setMaximum(500.000000000000000)
        self.doubleSpinBoxRulloX.setValue(0.000000000000000)

        self.gridLayout_4.addWidget(self.doubleSpinBoxRulloX, 0, 1, 1, 1)

        self.label_13 = QLabel(self.groupBox_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(u"background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 255, 127);")
        self.label_13.setAlignment(Qt.AlignCenter)
        self.label_13.setMargin(0)

        self.gridLayout_4.addWidget(self.label_13, 0, 2, 1, 1)

        self.doubleSpinBoxRulloY = QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBoxRulloY.setObjectName(u"doubleSpinBoxRulloY")
        self.doubleSpinBoxRulloY.setFont(font)
        self.doubleSpinBoxRulloY.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBoxRulloY.setDecimals(2)
        self.doubleSpinBoxRulloY.setMinimum(-500.000000000000000)
        self.doubleSpinBoxRulloY.setMaximum(500.000000000000000)
        self.doubleSpinBoxRulloY.setValue(0.000000000000000)

        self.gridLayout_4.addWidget(self.doubleSpinBoxRulloY, 0, 3, 1, 1)

        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 255, 127);")
        self.label_8.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout_4.addWidget(self.label_8, 1, 0, 1, 2)

        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 255, 127);")
        self.label_3.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout_4.addWidget(self.label_3, 1, 2, 1, 2)

        self.spinBoxOffsetLaser = QSpinBox(self.groupBox_3)
        self.spinBoxOffsetLaser.setObjectName(u"spinBoxOffsetLaser")
        self.spinBoxOffsetLaser.setFont(font)
        self.spinBoxOffsetLaser.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBoxOffsetLaser.setMinimum(-180)
        self.spinBoxOffsetLaser.setMaximum(180)
        self.spinBoxOffsetLaser.setValue(-123)

        self.gridLayout_4.addWidget(self.spinBoxOffsetLaser, 2, 2, 1, 2)

        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout_4.setColumnStretch(1, 2)
        self.gridLayout_4.setColumnStretch(2, 1)
        self.gridLayout_4.setColumnStretch(3, 2)

        self.verticalLayout_4.addWidget(self.groupBox_3)

        self.verticalSpacer_2 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_2 = QVBoxLayout(self.tab_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tableWidget_colorpref = QTableWidget(self.tab_3)
        if (self.tableWidget_colorpref.columnCount() < 4):
            self.tableWidget_colorpref.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_colorpref.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_colorpref.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_colorpref.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_colorpref.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget_colorpref.setObjectName(u"tableWidget_colorpref")

        self.verticalLayout_2.addWidget(self.tableWidget_colorpref)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout_3.addWidget(self.tabWidget)

        self.buttonBox = QDialogButtonBox(DialogSettings)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close|QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout_3.addWidget(self.buttonBox)

#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.lineEditUrlPlc)
        self.label_2.setBuddy(self.spinBoxPortaPlc)
        self.label_4.setBuddy(self.doubleSpinBoxScala)
        self.label_3.setBuddy(self.spinBoxOffsetLaser)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.lineEditUrlPlc, self.doubleSpinBoxPennaX)
        QWidget.setTabOrder(self.doubleSpinBoxPennaX, self.doubleSpinBoxPennaY)
        QWidget.setTabOrder(self.doubleSpinBoxPennaY, self.doubleSpinBoxLaserX)
        QWidget.setTabOrder(self.doubleSpinBoxLaserX, self.doubleSpinBoxLaserY)
        QWidget.setTabOrder(self.doubleSpinBoxLaserY, self.doubleSpinBoxRulloX)
        QWidget.setTabOrder(self.doubleSpinBoxRulloX, self.doubleSpinBoxRulloY)
        QWidget.setTabOrder(self.doubleSpinBoxRulloY, self.buttonBox)

        self.retranslateUi(DialogSettings)
        self.buttonBox.accepted.connect(DialogSettings.accept)
        self.buttonBox.rejected.connect(DialogSettings.reject)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(DialogSettings)
    # setupUi

    def retranslateUi(self, DialogSettings):
        DialogSettings.setWindowTitle(QCoreApplication.translate("DialogSettings", u"impostazioni", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("DialogSettings", u"COORDINATE RETE", None))
        self.label.setText(QCoreApplication.translate("DialogSettings", u"indirizzo controller", None))
        self.lineEditUrlPlc.setText(QCoreApplication.translate("DialogSettings", u"192.168.0.21", None))
        self.label_2.setText(QCoreApplication.translate("DialogSettings", u"porta", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("DialogSettings", u"DIMENSIONE PIANO (cm)", None))
        self.label_9.setText(QCoreApplication.translate("DialogSettings", u"X =", None))
        self.label_14.setText(QCoreApplication.translate("DialogSettings", u"Y =", None))
        self.label_4.setText(QCoreApplication.translate("DialogSettings", u"offset scala", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("DialogSettings", u"POSIZIONE FINALE (cm)", None))
        self.label_10.setText(QCoreApplication.translate("DialogSettings", u"X =", None))
        self.label_15.setText(QCoreApplication.translate("DialogSettings", u"Y =", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("DialogSettings", u"generali", None))
        self.groupBox.setTitle(QCoreApplication.translate("DialogSettings", u"SPOSTAMENTO PENNA (cm)", None))
        self.label_5.setText(QCoreApplication.translate("DialogSettings", u"X =", None))
        self.label_6.setText(QCoreApplication.translate("DialogSettings", u"Y =", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("DialogSettings", u"SPOSTAMENTO LASER (cm)", None))
        self.label_7.setText(QCoreApplication.translate("DialogSettings", u"X =", None))
        self.label_11.setText(QCoreApplication.translate("DialogSettings", u"Y =", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("DialogSettings", u"SPOSTAMENTO RULLO (cm)", None))
        self.label_12.setText(QCoreApplication.translate("DialogSettings", u"X =", None))
        self.label_13.setText(QCoreApplication.translate("DialogSettings", u"Y =", None))
        self.label_8.setText(QCoreApplication.translate("DialogSettings", u"override rotazione", None))
        self.label_3.setText(QCoreApplication.translate("DialogSettings", u"offset gradi", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("DialogSettings", u"posizioni", None))
        ___qtablewidgetitem = self.tableWidget_colorpref.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("DialogSettings", u"colore", None));
        ___qtablewidgetitem1 = self.tableWidget_colorpref.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("DialogSettings", u"passo", None));
        ___qtablewidgetitem2 = self.tableWidget_colorpref.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("DialogSettings", u"ordine", None));
        ___qtablewidgetitem3 = self.tableWidget_colorpref.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("DialogSettings", u"genera", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("DialogSettings", u"preferenze", None))
    # retranslateUi

