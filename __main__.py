# !/usr/bin/python3
# encoding: utf-8

import sys

from PySide6.QtWidgets import QApplication

from MainWindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MainWindow()
    myapp.showMaximized()
    sys.exit(app.exec())
