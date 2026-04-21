# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preview.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from .gvpreview import GVPreview


class Ui_previewDialog(object):
    def setupUi(self, previewDialog):
        if not previewDialog.objectName():
            previewDialog.setObjectName(u"previewDialog")
        previewDialog.resize(900, 600)
        self.verticalLayout = QVBoxLayout(previewDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.preview = GVPreview(previewDialog)
        self.preview.setObjectName(u"preview")

        self.verticalLayout.addWidget(self.preview)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.ButtonStart = QPushButton(previewDialog)
        self.ButtonStart.setObjectName(u"ButtonStart")
        font = QFont()
        font.setFamily(u"Courier 10 Pitch")
        font.setPointSize(16)
        self.ButtonStart.setFont(font)
        icon = QIcon()
        icon.addFile(u":/img/res/preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ButtonStart.setIcon(icon)

        self.horizontalLayout.addWidget(self.ButtonStart)

        self.ButtonClose = QPushButton(previewDialog)
        self.ButtonClose.setObjectName(u"ButtonClose")
        self.ButtonClose.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/img/res/exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ButtonClose.setIcon(icon1)

        self.horizontalLayout.addWidget(self.ButtonClose)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(previewDialog)
        self.ButtonClose.clicked.connect(previewDialog.close)

        QMetaObject.connectSlotsByName(previewDialog)
    # setupUi

    def retranslateUi(self, previewDialog):
        previewDialog.setWindowTitle(QCoreApplication.translate("previewDialog", u"plotter preview", None))
        self.ButtonStart.setText(QCoreApplication.translate("previewDialog", u"Avvia", None))
        self.ButtonClose.setText(QCoreApplication.translate("previewDialog", u"Esci", None))
    # retranslateUi

