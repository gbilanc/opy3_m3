# encoding: utf-8

import ftplib
import time
from struct import pack
from struct import unpack

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QFrame
from PySide6.QtWidgets import QMessageBox

from resources import *
from statics import ButtonBit
from statics import NjWrite
from statics import StatusBit
from statics import Tools
from statics import float_to_long_bits
from statics import int2bit
from statics import settings
from .njstatusframe import Ui_statusframe


class NjStatus(QFrame):

    def __init__(self, parent=None):
        QFrame.__init__(self, parent)
        self.ui = Ui_statusframe()
        self.ui.setupUi(self)
        self.ui.csv_start_point.valueChanged.connect(self.handle_start_point_changed)
        self.ui.btCaricaCsv.clicked.connect(self.do_carica_csv)
        self.ui.btAUTO.clicked.connect(self.bt_auto_clicked)
        self.ui.btSTART.pressed.connect(self.bt_start_pressed)
        self.ui.btMANUAL.clicked.connect(self.bt_manual_clicked)
        self.ui.btHOMING.pressed.connect(self.bt_homing_pressed)
        self.ui.btRESET.pressed.connect(self.bt_reset_pressed)
        self.ui.btRESET.released.connect(self.bt_reset_released)
        self.ui.btHOLD.clicked.connect(self.bt_hold_clicked)
        self.ui.btMODE.clicked.connect(self.bt_mode_clicked)
        self.ui.SB01.valueChanged.connect(self._write_override1)
        self.ui.SB02.valueChanged.connect(self._write_override2)
        self.buttons_list = (self.ui.btAUTO, self.ui.btSTART, self.ui.btMANUAL,
                             self.ui.btHOMING, self.ui.btRESET, self.ui.btHOLD,
                             None, None, self.ui.btMODE)
        self.fins_instance = None
        self.button_state = list('0000000000000000')
        self.status_flags = '00000000000000000000000000000000'
        self.current_tool = Tools.Penna.value  # 1
        self.total_steps = 0
        self.callback = None
        self.hold_status_rullo = 0
        self.start_point_index = 0

    @property
    def homing_in_corso(self):
        return self.status_flags[StatusBit.HomingInCorso.value] == '1'

    @property
    def homing_eseguito(self):
        return self.status_flags[StatusBit.HomingEseguito.value] == '1'

    @property
    def error_ect(self):
        return self.status_flags[StatusBit.ErroreECT.value] == '1'

    @property
    def error_mc(self):
        return self.status_flags[StatusBit.ErroreMC.value] == '1'

    @property
    def error_plc(self):
        return self.status_flags[StatusBit.ErrorePLC.value] == '1'

    @property
    def nj_active(self):
        return self.status_flags[StatusBit.NJ_Active.value] == '1'

    @property
    def ml_start_path(self):
        return self.status_flags[StatusBit.ML_StartPath.value] == '1'

    @property
    def ml_done(self):
        return self.status_flags[StatusBit.ML_Done.value] == '1'

    @property
    def fr_done(self):
        return self.status_flags[StatusBit.FR_Done.value] == '1'

    @property
    def fr_busy(self):
        return self.status_flags[StatusBit.FR_Busy.value] == '1'

    @property
    def fr_error(self):
        return self.status_flags[StatusBit.FR_Error.value] == '1'

    @property
    def end_read_file(self):
        return self.status_flags[StatusBit.FR_EndReadFileData.value] == '1'

    @property
    def nj_automatico(self):
        return self.status_flags[StatusBit.NJ_Automatico.value] == '1'

    @property
    def nj_manuale(self):
        return self.status_flags[StatusBit.NJ_Manuale.value] == '1'

    @property
    def nj_hold(self):
        return self.status_flags[StatusBit.NJ_Hold.value] == '1'

    @property
    def nj_emergenza(self):
        return self.status_flags[StatusBit.NJ_Emergenza.value] == '1'

    @property
    def nj_homing(self):
        return self.status_flags[StatusBit.NJ_Homing.value] == '1'

    @property
    def valve_rullo(self):
        return self.status_flags[StatusBit.ValvRULLO.value] == '1'

    @property
    def valve_penna(self):
        return self.status_flags[StatusBit.ValvPENNA.value] == '1'

    @property
    def valve_lama(self):
        return self.status_flags[StatusBit.ValvLAMA.value] == '1'

    @property
    def tool_change(self):
        return self.status_flags[StatusBit.RichHomeCambioTool.value] == '1'

    @property
    def nj_ready(self):
        return self.status_flags[StatusBit.NJ_Ready.value] == '1'

    @property
    def nj_error(self):
        return self.status_flags[StatusBit.NJ_Error.value] == '1'

    @property
    def is_auto(self):
        return self.button_state[ButtonBit.Automatic.value] == '1'

    @property
    def is_start(self):
        return self.button_state[ButtonBit.Start.value] == '1'

    @property
    def is_manual(self):
        return self.button_state[ButtonBit.Manual.value] == '1'

    @property
    def is_homing(self):
        return self.button_state[ButtonBit.Homing.value] == '1'

    @property
    def is_reset(self):
        return self.button_state[ButtonBit.Reset.value] == '1'

    @property
    def is_hold(self):
        return self.button_state[ButtonBit.Hold.value] == '1'

    @property
    def end_trans_file(self):
        return self.button_state[ButtonBit.EntTranFile.value] == '1'

    @property
    def trans_mode(self):
        return self.button_state[ButtonBit.TransMode.value] == '1'

    def show_status(self, value):
        unpacked = unpack('>HH', value)
        self.status_flags = int2bit(unpacked[0]) + int2bit(unpacked[1])
        self.ui.lb_rullo.setStyleSheet(LABELGREEN if self.valve_rullo else LABELGRAY)
        self.ui.lb_penna.setStyleSheet(LABELGREEN if self.valve_penna else LABELGRAY)
        self.ui.lb_lama.setStyleSheet(LABELGREEN if self.valve_lama else LABELGRAY)
        self.ui.lb_emergenza.setStyleSheet(LABELRED if self.nj_emergenza else LABELGRAY)
        self.ui.lb_homing.setStyleSheet(LABELGREEN if self.homing_eseguito else LABELRED)
        self.ui.lb_ecterror.setStyleSheet(LABELRED if self.error_ect else LABELGRAY)
        self.ui.lb_mcerror.setStyleSheet(LABELRED if self.error_mc else LABELGRAY)
        self.ui.lb_plcerror.setStyleSheet(LABELRED if self.error_plc else LABELGRAY)
        self.ui.lb_endread.setStyleSheet(LABELGREEN if self.end_read_file else LABELRED)
        self.buttons_list[ButtonBit.Automatic.value].setStyleSheet(
            BUTTONGREEN if self.nj_automatico else BUTTONGRAY)
        self.buttons_list[ButtonBit.Start.value].setStyleSheet(
            BUTTONGREEN if self.ml_start_path else BUTTONGRAY)
        self.buttons_list[ButtonBit.Manual.value].setStyleSheet(
            BUTTONGREEN if self.nj_manuale else BUTTONGRAY)
        self.buttons_list[ButtonBit.Homing.value].setStyleSheet(
            BUTTONORANGE if self.homing_in_corso else BUTTONGRAY)
        self.buttons_list[ButtonBit.Reset.value].setStyleSheet(
            BUTTONRED if self.is_reset else BUTTONGRAY)
        self.buttons_list[ButtonBit.Hold.value].setStyleSheet(
            BUTTONRED if self.nj_hold else BUTTONGRAY)
        self.buttons_list[ButtonBit.TransMode.value].setStyleSheet(
            BUTTONORANGE if self.trans_mode else BUTTONGRAY)
        if self.ml_done:  # esecuzione plottaggio terminata
            self.bt_manual_clicked()
            self.callback("btManual_clicked")
        if self.end_trans_file and self.end_read_file:
            self._set_end_trans_file('0')  # HOST_EndTrasFile
            time.sleep(1.0)  # ritardo 1sec
            self.callback("fineLetturaCsv")
            if self.tool_change or not self.homing_eseguito:
                self.ui.btHOMING.setStyleSheet(BUTTONGREEN)  # evidenzia tasto HOMING
                QMessageBox.information(self, 'attenzione', MES05)
            else:
                self.hold_status_rullo = 0
                self.bt_auto_clicked()  # simula pressione del tasto auto
                time.sleep(1.0)  # ritardo 1sec
                self.bt_start_pressed()  # simula pressione del tasto start

    def show_axis_status(self, axis):
        self.ui.lb_xpos.setText("%.02f" % axis[0].position)  # asse X
        self.ui.lb_ypos.setText("%.02f" % axis[1].position)  # asse Y
        self.ui.lb_cpos.setText("%.02f" % axis[2].position)  # asse Z
        self.ui.lb_xrun.setText("ON" if axis[0].run else "OFF")
        self.ui.lb_xrun.setStyleSheet(LABELGREEN if axis[0].run else LABELRED)
        self.ui.lb_yrun.setText("ON" if axis[1].run else "OFF")
        self.ui.lb_yrun.setStyleSheet(LABELGREEN if axis[1].run else LABELRED)
        self.ui.lb_crun.setText("ON" if axis[2].run else "OFF")
        self.ui.lb_crun.setStyleSheet(LABELGREEN if axis[2].run else LABELRED)
        self.ui.lb_xalarm.setStyleSheet(LABELRED if axis[0].drv_alarm else LABELGRAY)
        self.ui.lb_yalarm.setStyleSheet(LABELRED if axis[1].drv_alarm else LABELGRAY)
        self.ui.lb_calarm.setStyleSheet(LABELRED if axis[2].drv_alarm else LABELGRAY)

    def set_start_point(self, value):
        self.ui.csv_start_point.setValue(value)

    def set_callback(self, value):
        self.callback = value

    def set_current_tool(self, value):
        self.current_tool = value

    def set_override1(self, value):
        unpacked = unpack('>H', value)
        self.ui.SB01.setValue(unpacked[0])

    def set_override2(self, value):
        unpacked = unpack('>H', value)
        self.ui.SB02.setValue(unpacked[0])

    def set_current_row(self, value):
        unpacked = unpack('>H', value)
        num_riga = unpacked[0]
        if self.current_tool == Tools.Rullo.value:
            if num_riga == 2 and self.hold_status_rullo == 0:
                self.hold_status_rullo = 1
                self.bt_hold_clicked()
            if num_riga == self.total_steps and self.hold_status_rullo == 1:
                self.hold_status_rullo = 2
                self.bt_hold_clicked()
        self.ui.lb_riga.setText('%06d' % num_riga)

    def do_carica_csv(self):
        if self.start_point_index > 0:
            self.callback("inviaCsvClicked", self.start_point_index)
        else:
            self.invia_csv()

    def invia_csv(self):
        ftp = ftplib.FTP(settings.plcUrl)
        ftp.login('VsP', '88888888')
        ftp.set_pasv(True)
        ftp.cwd('MEMCARD1')
        ftp.cwd('SMD_FileData')
        ftp.storbinary('STOR VsPFileRead_1.csv', open('myfile.csv', 'rb'))
        ftp.quit()
        self.bt_manual_clicked()
        self.total_steps = sum(1 for _ in open('myfile.csv'))
        self._write_num_lines(self.total_steps)  # invia numero di linee
        self._write_tool_id(self.current_tool)  # invia id utensile
        # if self.current_tool == Tools.Cutter.value:
        # self.set_trans_mode_on()  # forza Transition Mode On
        # else:
        # self.set_trans_mode_off()  # forza Transition Mode Off
        self._set_end_trans_file('1')  # HOST_EndTrasFile
        self.callback("inizLetturaCsv")

    @Slot()
    def bt_auto_clicked(self):
        if not self.is_auto:
            self.ui.btSTART.setEnabled(True)
            self.ui.btMODE.setEnabled(False)
            self.ui.btCaricaCsv.setEnabled(False)
            self.button_state[ButtonBit.Automatic.value] = '1'
            self.button_state[ButtonBit.Manual.value] = '0'
            self._write_button_state()

    @Slot()
    def bt_manual_clicked(self):
        if not self.is_manual:
            self.ui.btSTART.setEnabled(False)
            self.ui.btMODE.setEnabled(True)
            self.ui.btCaricaCsv.setEnabled(True)
            self.button_state[ButtonBit.Manual.value] = '1'
            self.button_state[ButtonBit.Automatic.value] = '0'
            self.button_state[ButtonBit.Hold.value] = '0'
            self._write_button_state()

    @Slot()
    def bt_start_pressed(self):
        if self.error_ect or self.error_mc or self.error_plc or self.nj_emergenza:
            QMessageBox.information(self, 'Ciclo Automatico', MES09)
            return
        reply = QMessageBox.question(self, 'Ciclo Automatico', MES02,
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.Yes)
        if reply == QMessageBox.StandardButton.Yes:
            self.button_state[ButtonBit.Start.value] = '1'
            self._write_button_state()
            time.sleep(2)
            self.button_state[ButtonBit.Start.value] = '0'
            self._write_button_state()
        else:  # QMessageBox.StandardButton.No
            self.bt_manual_clicked()
            self.callback("btManual_clicked")

    @Slot()
    def bt_homing_pressed(self):
        if self.error_ect or self.error_mc or self.error_plc or self.nj_emergenza:
            QMessageBox.information(self, 'Ciclo Homing', MES09)
            return
        reply = QMessageBox.question(self, 'Ricerca Homing', MES02,
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.Yes)
        if reply == QMessageBox.StandardButton.Yes:
            self._write_offset_lama(settings.offset_lama)
            self.button_state[ButtonBit.Homing.value] = '1'
            self._write_button_state()
            time.sleep(2)
            self.button_state[ButtonBit.Homing.value] = '0'
            self._write_button_state()

    @Slot()
    def bt_hold_clicked(self):
        if not self.is_hold:
            self.button_state[ButtonBit.Hold.value] = '1'
            self._write_button_state()
        else:
            reply = QMessageBox.question(self, 'Ciclo Holding', MES02,
                                         QMessageBox.StandardButton.Yes, QMessageBox.StandardButton.No)
            if reply == QMessageBox.StandardButton.Yes:
                self.button_state[ButtonBit.Hold.value] = '0'
                self._write_button_state()

    @Slot()
    def bt_mode_clicked(self):
        if not self.trans_mode:
            self.set_tm_on()
        else:
            self.set_tm_off()

    def set_tm_on(self):
        self.ui.btMODE.setText("TM_ON")
        self.button_state[ButtonBit.TransMode.value] = '1'
        self._write_button_state()

    def set_tm_off(self):
        self.ui.btMODE.setText("TM_OFF")
        self.button_state[ButtonBit.TransMode.value] = '0'
        self._write_button_state()

    @Slot()
    def bt_reset_pressed(self):
        self.buttons_list[ButtonBit.Reset.value].setStyleSheet(BUTTONRED)
        self.button_state[ButtonBit.Reset.value] = '1'
        self.button_state[ButtonBit.Start.value] = '0'
        self.button_state[ButtonBit.Homing.value] = '0'
        self.button_state[ButtonBit.EntTranFile.value] = '0'
        self._write_button_state()

    @Slot()
    def bt_reset_released(self):
        self.buttons_list[ButtonBit.Reset.value].setStyleSheet(BUTTONGRAY)
        self.button_state[ButtonBit.Reset.value] = '0'
        self._write_button_state()

    @Slot(int)
    def _write_override1(self, value):
        packed = pack('>H', value).decode('latin1')
        self.fins_instance.memory_area_write(NjWrite.Override.value, packed)

    @Slot(int)
    def _write_offset_lama(self, value):
        packed = pack('>h', value).decode('latin1')
        self.fins_instance.memory_area_write(NjWrite.OffsetLama.value, packed)

    @Slot(float)
    def _write_offset_lama_float(self, value):
        packed = pack('>f', float_to_long_bits(value)).decode('latin1')
        self.fins_instance.memory_area_write(NjWrite.OffsetLamaFloat.value, packed)

    @Slot(int)
    def _write_num_lines(self, value):
        packed = pack('>H', value).decode('latin1')
        self.fins_instance.memory_area_write(NjWrite.NumeroPunti.value, packed)

    @Slot(int)
    def _write_override2(self, value):
        packed = pack('>H', value).decode('latin1')
        self.fins_instance.memory_area_write(NjWrite.VelJog.value, packed)

    @Slot(int)
    def _write_tool_id(self, value):
        packed = pack('>H', value).decode('latin1')
        self.fins_instance.memory_area_write(NjWrite.TipoUtensile.value, packed)

    @Slot()
    def handle_start_point_changed(self):
        position = self.ui.csv_start_point.value()
        if position < len(settings.raccordo):
            self.start_point_index = settings.raccordo[position]
            with open('punti.csv', 'r') as f1:
                lines = f1.readlines()
                if self.start_point_index < len(lines):
                    punto = lines[self.start_point_index].split(";")
                    self.callback("startPointChanged", punto)
        else:
            self.callback("startPointOverflow", position)

    def _set_end_trans_file(self, value):
        self.button_state[ButtonBit.EntTranFile.value] = value
        self._write_button_state()

    def _write_button_state(self):
        reversed_list = list(reversed(self.button_state))
        packed = pack('>H', int(''.join(reversed_list), 2)).decode('latin1')
        self.fins_instance.memory_area_write(NjWrite.Buttons.value, packed)
