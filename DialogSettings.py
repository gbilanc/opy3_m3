# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from PySide6.QtCore import Qt
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QDialog
from PySide6.QtWidgets import QDialogButtonBox
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QSpinBox

from ccolorpref import CColorPref
from statics import get_qt_color
from statics import settings
from ui.settingsui import Ui_DialogSettings


def get_spinbox_widget(minimum, maximum, value):
    spin = QSpinBox()
    spin.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
    spin.setMinimum(minimum)
    spin.setMaximum(maximum)
    spin.setValue(value)
    return spin


def get_label_widget(colore):
    label = QLabel(str(colore))
    label.setAlignment(Qt.AlignCenter)
    label.setProperty("colore", colore)
    label.setStyleSheet("background-color: %s;" % get_qt_color(colore).name())
    return label


class DialogSettings(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_DialogSettings()
        self.ui.setupUi(self)
        self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Save).clicked.connect(self.save_settings)
        self.ui.lineEditUrlPlc.setText(settings.plcUrl)
        self.ui.spinBoxPortaPlc.setValue(settings.plcPort)
        self.ui.doubleSpinBoxScala.setValue(settings.scale_unit)
        self.ui.spinBoxOffsetLama.setValue(settings.offset_lama)
        self.ui.doubleSpinBoxRullo.setValue(settings.speed_rullo)
        self.ui.doubleSpinBoxPennaX.setValue(float(settings.pos_penna[0]))
        self.ui.doubleSpinBoxPennaY.setValue(float(settings.pos_penna[1]))
        self.ui.doubleSpinBoxCutterX.setValue(float(settings.pos_lama[0]))
        self.ui.doubleSpinBoxCutterY.setValue(float(settings.pos_lama[1]))
        self.ui.doubleSpinBoxRulloX.setValue(float(settings.pos_rullo[0]))
        self.ui.doubleSpinBoxRulloY.setValue(float(settings.pos_rullo[1]))
        self.ui.doubleSpinBox_maxx.setValue(float(settings.max_size[0]))
        self.ui.doubleSpinBox_maxy.setValue(float(settings.max_size[1]))
        self.ui.doubleSpinBox_stopx.setValue(float(settings.pos_end[0]))
        self.ui.doubleSpinBox_stopy.setValue(float(settings.pos_end[1]))
        self.build_colors_table()

    def save_settings(self):
        self.save_colors_table()
        settings.plcUrl = self.ui.lineEditUrlPlc.text()
        settings.plcPort = self.ui.spinBoxPortaPlc.value()
        settings.scale_unit = self.ui.doubleSpinBoxScala.value()
        settings.offset_lama = self.ui.spinBoxOffsetLama.value()
        settings.speed_rullo = self.ui.doubleSpinBoxRullo.value()
        settings.pos_penna[0] = self.ui.doubleSpinBoxPennaX.value()
        settings.pos_penna[1] = self.ui.doubleSpinBoxPennaY.value()
        settings.pos_lama[0] = self.ui.doubleSpinBoxCutterX.value()
        settings.pos_lama[1] = self.ui.doubleSpinBoxCutterY.value()
        settings.pos_rullo[0] = self.ui.doubleSpinBoxRulloX.value()
        settings.pos_rullo[1] = self.ui.doubleSpinBoxRulloY.value()
        settings.max_size[0] = self.ui.doubleSpinBox_maxx.value()
        settings.max_size[1] = self.ui.doubleSpinBox_maxy.value()
        settings.pos_end[0] = self.ui.doubleSpinBox_stopx.value()
        settings.pos_end[1] = self.ui.doubleSpinBox_stopy.value()
        settings.save()

    def build_colors_table(self):
        pref_colors = CColorPref.deserialize()
        self.ui.tableWidget_colorpref.setRowCount(len(pref_colors))
        for riga, pref in enumerate(pref_colors):
            self.ui.tableWidget_colorpref.setCellWidget(riga, 0,
                                                        get_label_widget(pref.colore))
            self.ui.tableWidget_colorpref.setCellWidget(riga, 1,
                                                        get_spinbox_widget(0, 100, pref.passo))
            self.ui.tableWidget_colorpref.setCellWidget(riga, 2,
                                                        get_spinbox_widget(0, 999, pref.ordine))
            self.ui.tableWidget_colorpref.setCellWidget(riga, 3,
                                                        self.get_checkbox_widget(True if pref.genera == 1 else
                                                                                 False))

    def save_colors_table(self):
        pref_colors = list()
        for riga in range(self.ui.tableWidget_colorpref.rowCount()):
            column0 = self.ui.tableWidget_colorpref.cellWidget(riga, 0)
            colore = int(column0.property("colore"))
            column1 = self.ui.tableWidget_colorpref.cellWidget(riga, 1)
            passo = int(column1.value())
            column2 = self.ui.tableWidget_colorpref.cellWidget(riga, 2)
            ordine = int(column2.value())
            column3 = self.ui.tableWidget_colorpref.cellWidget(riga, 3)
            genera = 1 if column3.isChecked() else 0
            pref_colors.append(CColorPref(colore, passo, ordine, genera))
        CColorPref.serialize(pref_colors)

    def get_checkbox_widget(self, checked):
        item = QPushButton()
        item.setCheckable(True)
        item.setText("SI" if checked else "NO")
        item.setChecked(checked)
        item.clicked.connect(lambda: self.handle_checkbox_checked(item))
        return item    

    @Slot()
    def handle_checkbox_checked(self, sender):
        sender.setText("SI" if sender.isChecked() else "NO")
