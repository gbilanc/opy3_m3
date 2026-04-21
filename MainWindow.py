# !/usr/bin/python
# encoding: utf-8

from math import pi
from struct import unpack

from PySide6.QtCore import QRectF
from PySide6.QtCore import QTimer
from PySide6.QtCore import Qt
from PySide6.QtCore import Slot
from PySide6.QtGui import QDoubleValidator
from PySide6.QtWidgets import QDialog
from PySide6.QtWidgets import QDoubleSpinBox
from PySide6.QtWidgets import QFileDialog
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QSpinBox

from DialogPreview import DialogPreview
from DialogSettings import DialogSettings
from classes import myfile_from_csv
from classes import myfile_from_plist
from classes.cworkspace import CWorkspace
from fins.udp import UDPFinsConnection
from resources import *
from statics import NjRead, ping_plotter
from statics import Tools
from statics import get_qt_color
from statics import get_color_pref
from statics import memo_helper
from statics import settings
from ui.mainapp import Ui_MainWindow

fins_instance = UDPFinsConnection()
fins_instance.connect(settings.plcUrl, settings.plcPort)
fins_instance.icf = '\x80'  # command+response_required
fins_instance.da1 = '\x15'  # NJ 192.168.0.21  = hex(21)
fins_instance.sa1 = '\x6E'  # PC 192.168.0.110 = hex(110)
fins_instance.mac = '\xB2'  # Memory Area Code (HOLDING_WORD)


def get_label_widget(texto, value, tooltip=None, bg=None):
    label = QLabel(texto)
    label.setAlignment(Qt.AlignCenter)
    label.setProperty('intcolore', value)
    label.setToolTip(tooltip)
    label.setStyleSheet("background-color: %s;" % ("white" if bg is None else bg.name()))
    return label


def get_double_spinbox_widget(minimum, maximum, value):
    spin = QDoubleSpinBox()
    spin.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
    spin.setMinimum(minimum)
    spin.setMaximum(maximum)
    spin.setValue(value)
    return spin


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.recent_files = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.njstatus.fins_instance = fins_instance
        self.ui.axis_x.set_title("driver X")
        self.ui.axis_y.set_title("driver Y")
        self.ui.axis_z.set_title("driver C")
        self.ui.plotter.status = self.ui.statusbar
        self.ui.lineEdit_X.setValidator(QDoubleValidator(-9.0, 9.0, 3, self.ui.lineEdit_X))
        self.ui.lineEdit_Y.setValidator(QDoubleValidator(-9.0, 9.0, 3, self.ui.lineEdit_Y))
        self.ui.lineEdit_X.setInputMask('0.000')
        self.ui.lineEdit_Y.setInputMask('0.000')
        self.ui.actionAcquisisci_dxf.triggered.connect(self.do_open_dxf)
        self.ui.actionSimula_plotter.triggered.connect(self.do_plotter)
        self.ui.actionInformazioni.triggered.connect(self.do_info)
        self.ui.actionImpostazioni.triggered.connect(self.do_settings)
        self.ui.btGeneraCsv.clicked.connect(self.do_genera_csv)
        self.ui.tabWidget.currentChanged.connect(self.change_cur_tab_widget)
        self.ui.rbRullo.clicked.connect(lambda: self.change_current_tool(Tools.Rullo.value))
        self.ui.rbPenna.clicked.connect(lambda: self.change_current_tool(Tools.Penna.value))
        self.ui.rbLama.clicked.connect(lambda: self.change_current_tool(Tools.Cutter.value))
        self.ui.push_move.clicked.connect(self.translate_layer)
        self.ui.push_rotate.clicked.connect(self.rotate_layer)
        self.ui.push_invertX.clicked.connect(lambda: self.flip_layer(0))
        self.ui.push_invertY.clicked.connect(lambda: self.flip_layer(1))
        self.ui.push_origine.clicked.connect(self.load_position)
        self.ui.cbxcolor.stateChanged.connect(self.handle_cbx_color_changed)
        self.axis_list = [self.ui.axis_x, self.ui.axis_y, self.ui.axis_z]
        self.cur_tool_id = Tools.Penna.value
        self.worker2 = None
        self.worker1 = QTimer(self)
        self.worker1.setInterval(200)
        self.worker1.timeout.connect(self.update_scrollbar)
        self.ui.njstatus.set_callback(self.handle_njstatus_events)
        self.plotter = self.ui.plotter
        self.update_recent_files_menu()
        if ping_plotter(settings.plcUrl):
            self.read_status()
        else:
            QMessageBox.information(self, 'Attenzione', MES12.format(settings.plcUrl))

    def update_recent_files_menu(self):
        self.ui.menuFiles_Recenti.clear()
        self.recent_files = settings.recent_files
        for item in self.recent_files:
            entry = self.ui.menuFiles_Recenti.addAction(item)
            entry.triggered.connect(lambda *args, arg1=item: self.open_file(arg1))
            self.ui.menuFiles_Recenti.addAction(entry)

    def update_recent_files_list(self, filename):
        if filename in self.recent_files:
            self.recent_files.remove(filename)
        if len(self.recent_files) > 10:
            self.recent_files.pop()
        self.recent_files.insert(0, filename)
        settings.set_recent_files(self.recent_files)
        self.update_recent_files_menu()

    @Slot()
    def do_open_dxf(self):
        file_dialog = QFileDialog(self)
        file_dialog.setWindowTitle('Apertura File dxf')
        file_dialog.setNameFilter('autocad dxf (*.dxf)')
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        if file_dialog.exec() == QDialog.DialogCode.Accepted:
            filename = file_dialog.selectedFiles()[0]
            self.open_file(filename)

    def open_file(self, filename):
        self.ui.statusbar.showMessage(MES13.format(filename))
        self.update_recent_files_list(filename)
        self.setCursor(Qt.WaitCursor)
        self.plotter.workspace = CWorkspace(filename)
        self.plotter.update()
        self.plotter.selected_layer = None
        bounds = self.plotter.workspace.bounds
        self.plotter.fitInView(QRectF(0, 0,
                                      bounds[2] * settings.scale_unit,
                                      bounds[3] * settings.scale_unit),
                               Qt.KeepAspectRatio)
        self.build_layers_table()
        self.ui.njstatus.set_start_point(0)
        self.setWindowTitle(filename)
        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.rbPenna.click()
        self.plotter.invalidate()
        memo_helper.set_filename(filename)
        if memo_helper.exists:
            self.open_memo()
        self.setCursor(Qt.ArrowCursor)

    @Slot()
    def do_genera_csv(self):
        if self.plotter.selected_layer is None:
            QMessageBox.information(self, 'Attenzione', MES03)
        else:
            self.ui.statusbar.showMessage(MES14)
            memo_helper.selected = self.plotter.selected_layer.name
            memo_helper.visible = self.plotter.selected_layer.visible
            memo_helper.reverse = self.plotter.selected_layer.reverse
            memo_helper.tool_id = self.cur_tool_id
            memo_helper.sort_colors = self.ui.cbxcolor.isChecked()
            self.update_preference()
            plist = self.plotter.selected_layer.get_points()
            settings.perv_degree = 0.0
            if len(plist) > 0:
                result = myfile_from_plist(self.cur_tool_id, plist)
                if result[0] == 0:  # generazione csv eseguita
                    memo_helper.serialize()
                    self.avvio_movimenti(result[1])
                elif result[0] == 1:
                    QMessageBox.information(self, 'Attenzione', result[1])
                else:  # generazione csv fallita
                    QMessageBox.information(self, 'Attenzione', result[1])
                    self.plotter.draw_error_segment(result[2], result[3])
            else:
                QMessageBox.information(self, 'Attenzione', MES06)

    def update_preference(self):
        for riga in range(self.ui.tableWidget_colors.rowCount()):
            column0 = self.ui.tableWidget_colors.cellWidget(riga, 0)
            color_pref = get_color_pref(column0.property("intcolore"))
            column1 = self.ui.tableWidget_colors.cellWidget(riga, 1)
            color_pref.passo = int(column1.value())
            column2 = self.ui.tableWidget_colors.cellWidget(riga, 2)
            color_pref.ordine = int(column2.value())
            column3 = self.ui.tableWidget_colors.cellWidget(riga, 3)
            color_pref.genera = 1 if column3.isChecked() else 0

    def avvio_movimenti(self, message):
        message_box = QMessageBox(self)
        message_box.setWindowTitle("omronpy_info")
        message_box.setText(message)
        QTimer.singleShot(500, message_box.accept)
        message_box.exec()
        if self.ui.njstatus.nj_manuale:
            self.ui.tabWidget.setCurrentIndex(2)
            self.plotter.clear_plot_points()
            self.ui.njstatus.invia_csv()
        else:  # impossibile inviare csv in modalità auto
            QMessageBox.information(self, 'Attenzione', MES04)

    @Slot()
    def do_plotter(self):
        dialog = DialogPreview()
        dialog.showFullScreen()
        dialog.exec()

    @Slot()
    def do_info(self):
        QMessageBox.information(self, 'Informazioni', MES01)

    @Slot()
    def do_settings(self):
        dialog = DialogSettings()
        dialog.exec()

    def get_spinbox_widget(self, minimum, maximum, value, label):
        spin = QSpinBox()
        spin.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        spin.setMinimum(minimum)
        spin.setMaximum(maximum)
        spin.setValue(value)
        spin.valueChanged.connect(lambda: self.handle_spinbox_changed(spin, label))
        return spin

    def get_checkbox_widget(self, checked, index, label):
        item = QPushButton()
        item.setCheckable(True)
        item.setText("SI" if checked else "NO")
        item.setChecked(checked)
        item.clicked.connect(lambda: self.handle_checkbox_checked(item, index, label))
        return item

    def build_layers_table(self):
        self.ui.tableWidget_layers.setRowCount(len(self.plotter.workspace.layers))
        for riga, item in enumerate(self.plotter.workspace.layers):
            self.ui.tableWidget_layers.setCellWidget(riga, 0, get_label_widget(item.name, None, str(item)))
            self.ui.tableWidget_layers.setCellWidget(riga, 1, self.get_checkbox_widget(
                True if item.visible else False, riga, "visible"))
            self.ui.tableWidget_layers.setCellWidget(riga, 2, self.get_checkbox_widget(
                True if item.selected else False, riga, "selected"))
            self.ui.tableWidget_layers.setCellWidget(riga, 3, self.get_checkbox_widget(
                True if item.reverse else False, riga, "reverse"))

    def build_colors_table(self):
        if self.plotter.selected_layer is None:
            self.ui.tableWidget_colors.setRowCount(0)
        else:
            self.ui.tableWidget_colors.setRowCount(len(self.plotter.selected_layer.colors))
            for riga, colore in enumerate(self.plotter.selected_layer.colors):
                color_pref = get_color_pref(colore)
                self.ui.tableWidget_colors.setCellWidget(riga, 0, get_label_widget(str(colore), colore, None,
                                                                                   get_qt_color(colore)))
                self.ui.tableWidget_colors.setCellWidget(riga, 1,
                                                         self.get_spinbox_widget(0, 100, color_pref.passo, "passo"))
                self.ui.tableWidget_colors.setCellWidget(riga, 2,
                                                         self.get_spinbox_widget(0, 999, color_pref.ordine, "ordine"))
                self.ui.tableWidget_colors.setCellWidget(riga, 3, self.get_checkbox_widget(
                    True if color_pref.genera == 1 else False, 0, "genera"))

    def select_layer_with_index(self, index):
        lx = self.plotter.workspace.layers[index]
        if (self.plotter.selected_layer is None or
                self.plotter.selected_layer.name != lx.name):
            self.plotter.select_layer_with_name(lx.name)
        self.ui.statusbar.showMessage("layer %s selected!" % lx.name)
        self.ui.cbxcolor.setEnabled(len(self.plotter.selected_layer.colors) > 1)
        self.build_colors_table()
        if lx.is_lama:
            self.ui.rbLama.click()
        elif lx.is_penna:
            self.ui.rbPenna.click()
        else:
            self.ui.rbRullo.click()
        self.plotter.invalidate()

    def change_current_tool(self, value):
        self.ui.cbxcolor.setEnabled(value != Tools.Rullo.value)
        self.ui.cbxcolor.setChecked(value == Tools.Cutter.value)
        self.cur_tool_id = value
        self.ui.njstatus.set_current_tool(value)

    def change_cur_tab_widget(self, index):
        if index in (0, 1):
            self.plotter.invalidate()
        else:
            self.plotter.invalidate(True)

    @Slot()
    def handle_cbx_color_changed(self):
        settings.sort_by_color = self.ui.cbxcolor.isChecked()
        if self.plotter.selected_layer is not None:
            self.plotter.selected_layer.unitized = False
            self.plotter.invalidate()

    @Slot()
    def handle_checkbox_checked(self, sender, index, label):
        sender.setText("SI" if sender.isChecked() else "NO")
        if label == "genera":
            self.update_preference()
            lx = self.plotter.selected_layer
            lx.unitized = False
            self.plotter.invalidate()
        if label == "visible":
            lx = self.plotter.workspace.layers[index]
            lx.do_visible(not lx.visible)
            self.build_layers_table()
            self.plotter.invalidate()
        if label == "reverse":
            lx = self.plotter.workspace.layers[index]
            lx.do_reverse(not lx.reverse)
            lx.unitized = False
            self.plotter.invalidate()
        if label == "selected":
            self.select_layer_with_index(index)
            self.build_layers_table()

    @Slot()
    def handle_spinbox_changed(self, sender, label):
        if label == "ordine":
            self.update_preference()
            lx = self.plotter.selected_layer
            lx.unitized = False
            self.plotter.invalidate()

    @Slot()
    def translate_layer(self):
        memo_helper.offsetX = float(self.ui.lineEdit_X.text())
        memo_helper.offsetY = float(self.ui.lineEdit_Y.text())
        self.plotter.translate_workspace(memo_helper.offsetX, memo_helper.offsetY)

    @Slot()
    def rotate_layer(self):
        self.plotter.rotate_workspace(-pi / 2)

    @Slot(int)
    def flip_layer(self, mode):
        self.plotter.flip_workspace(mode)

    @Slot()
    def load_position(self):
        ox = float(settings.pos_penna[0]) / settings.scale_unit
        oy = float(settings.pos_penna[1]) / settings.scale_unit
        self.ui.lineEdit_X.setText("%.03f" % (settings.curr_pos_x / 1000 - ox))
        self.ui.lineEdit_Y.setText("%.03f" % (settings.curr_pos_y / 1000 - oy))

    @Slot()
    def _read_status(self):
        self._handle_response(fins_instance.memory_area_read(NjRead.Override.value))
        self._handle_response(fins_instance.memory_area_read(NjRead.VelJog.value))
        self._handle_response(fins_instance.memory_area_read(NjRead.Nj_Status.value))
        self._handle_response(fins_instance.memory_area_read(NjRead.RunningPoint_ML.value))
        self._handle_response(fins_instance.memory_area_read(NjRead.Axis0_Status.value))
        self._handle_response(fins_instance.memory_area_read(NjRead.Axis1_Status.value))
        self._handle_response(fins_instance.memory_area_read(NjRead.Axis2_Status.value))
        self.ui.njstatus.show_axis_status(self.axis_list)
        settings.curr_pos_x = self.axis_list[0].position[0]
        settings.curr_pos_y = self.axis_list[1].position[0]
        settings.curr_degree = self.axis_list[2].position[0]

    @Slot()
    def update_scrollbar(self):
        value = self.ui.progBar1.value() + 1
        self.ui.progBar1.setValue(0 if value > 100 else value)

    def _handle_response(self, values):
        if values[0] == NjRead.Override.value[0]:
            self.ui.njstatus.set_override1(values[1])
        elif values[0] == NjRead.VelJog.value[0]:
            self.ui.njstatus.set_override2(values[1])
        elif values[0] == NjRead.Nj_Status.value[0]:
            self.ui.njstatus.show_status(values[1])
        elif values[0] == NjRead.RunningPoint_ML.value[0]:
            self.show_current_row(values[1])
        elif values[0] == NjRead.Axis0_Status.value[0]:
            self.ui.axis_x.show_status(values[1])
        elif values[0] == NjRead.Axis1_Status.value[0]:
            self.ui.axis_y.show_status(values[1])
        elif values[0] == NjRead.Axis2_Status.value[0]:
            self.ui.axis_z.show_status(values[1])
        else:
            self.ui.statusbar.showMessage(values[1])

    def show_current_row(self, value):
        self.ui.njstatus.set_current_row(value)
        offset = settings.pos_penna
        if self.cur_tool_id == Tools.Cutter.value:
            offset = settings.self.pos_lama
        if self.cur_tool_id == Tools.Rullo.value:
            offset = settings.pos_rullo
        if self.ui.tabWidget.currentIndex() > 1:
            if self.ui.njstatus.ml_start_path:  # plottaggio in corso
                unpacked = unpack('>H', value)
                self.plotter.draw_plot_points(unpacked[0], offset)

    def handle_njstatus_events(self, event, params=None):
        if event == "btManual_clicked":
            if self.ui.tabWidget.currentIndex() > 0:
                self.ui.tabWidget.setCurrentIndex(0)
        if event == "inizLetturaCsv":
            self.ui.progBar1.setValue(0)
            self.ui.statusbar.showMessage(MES15)
            self.worker1.start()
        if event == "fineLetturaCsv":
            self.worker1.stop()
            self.ui.progBar1.setValue(0)
            self.ui.statusbar.showMessage(MES16)
        if event == "startPointChanged":
            self.plotter.set_start_point(params)
        if event == "startPointOverflow":
            QMessageBox.information(self, 'Attenzione', MES10.format(params))
        if event == "inviaCsvClicked":
            result = myfile_from_csv(self.cur_tool_id, params)
            if result[0] == 0:  # generazione csv eseguita
                self.avvio_movimenti(result[1])
            elif result[0] == 1:
                QMessageBox.information(self, 'Attenzione', result[1])
            else:  # generazione csv fallita
                QMessageBox.information(self, 'Attenzione', result[1])
                self.plotter.draw_error_segment(result[2], result[3])

    def open_memo(self):
        for i in range(len(self.plotter.workspace.layers)):
            item = self.plotter.workspace.layers[i]
            if item.name == memo_helper.selected:
                item.do_selected(True)
                item.do_visible(memo_helper.visible)
                if memo_helper.reverse:
                    item.do_reverse(True)
                break

        self.build_layers_table()
        self.plotter.select_layer_with_name(memo_helper.selected)
        self.build_colors_table()

        self.plotter.translate_workspace(memo_helper.offsetX, memo_helper.offsetY)
        self.ui.lineEdit_X.setText("%.03f" % memo_helper.offsetX)
        self.ui.lineEdit_Y.setText("%.03f" % memo_helper.offsetY)

        if memo_helper.tool_id == Tools.Penna.value:
            self.ui.rbPenna.click()
        elif memo_helper.tool_id == Tools.Rullo.value:
            self.ui.rbRullo.click()
        elif memo_helper.tool_id == Tools.Cutter.value:
            self.ui.rbLama.click()

        if self.plotter.selected_layer:
            self.ui.cbxcolor.setEnabled(len(self.plotter.selected_layer.colors) > 1)
            self.ui.cbxcolor.setChecked(memo_helper.sort_colors)
            self.update_preference()
            self.plotter.invalidate()
            self.ui.njstatus.set_start_point(0)

    def read_status(self):
        self.worker2 = QTimer(self)
        self.worker2.setInterval(250)
        self.worker2.timeout.connect(self._read_status)
        self._handle_response(fins_instance.memory_area_read(NjRead.Override.value))
        self._handle_response(fins_instance.memory_area_read(NjRead.VelJog.value))
        self.ui.njstatus.set_callback(self.handle_njstatus_events)
        self.ui.njstatus.bt_manual_clicked()
        self.worker2.start()
