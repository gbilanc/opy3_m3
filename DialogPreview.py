from PySide6.QtCore import Slot
from PySide6.QtWidgets import QDialog

from ui.previewui import Ui_previewDialog


class DialogPreview(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_previewDialog()
        self.ui.setupUi(self)
        self.ui.ButtonStart.clicked.connect(self.do_preview)

    @Slot()
    def do_preview(self):
        self.ui.preview.draw_points()
