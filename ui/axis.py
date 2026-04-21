from struct import unpack

from PySide6.QtWidgets import QFrame

from resources import *
from statics import int2bit
from statics import swap_bytes
from .axisframe import Ui_axisframe


class Axis(QFrame):

    def __init__(self, parent=None):
        QFrame.__init__(self, parent)
        self.ui = Ui_axisframe()
        self.ui.setupUi(self)
        self.position = 0.0
        self.coppia = 0.0
        self.velocity = 0.0
        self.error1 = ''
        self.error2 = ''
        self.destination = 0.0
        self.drv_alarm = False
        self.main_power = False
        self.run = False
        self.neg_override = False
        self.pos_override = False
        self.home = False
        self.moving = False
        self.leds = (self.ui.led001, self.ui.led002, self.ui.led003,
                     self.ui.led004, self.ui.led005, self.ui.led006)
        self.labs = (self.ui.lab001, self.ui.lab002, self.ui.lab003,
                     self.ui.lab005, self.ui.lab006, self.ui.lab004)

    def set_title(self, value):
        self.ui.labtitle.setText(value)

    def show_status(self, value):
        swapped = swap_bytes(value)

        H001 = unpack('H', swapped[0:2])
        H002 = unpack('H', swapped[2:4])
        d001 = unpack('d', swapped[4:12])
        d002 = unpack('d', swapped[12:20])
        d003 = unpack('d', swapped[20:28])
        H003 = unpack('H', swapped[28:30])
        H004 = unpack('H', swapped[30:32])
        d004 = unpack('d', swapped[32:40])

        h001 = int2bit(H001[0])
        h002 = int2bit(H002[0])
        self.drv_alarm = h001[0] == '1'
        self.main_power = h001[1] == '1'
        self.run = h001[2] == '1'
        self.neg_override = h001[3] == '1'
        self.pos_override = h001[4] == '1'
        self.home = h001[5] == '1'
        self.error1 = hex(H003[0])
        self.error2 = hex(H004[0])
        self.position = d001
        self.coppia = d002
        self.velocity = d003
        self.destination = d004

        self.leds[0].setStyleSheet(LABELRED if self.drv_alarm else LABELGRAY)
        self.leds[1].setStyleSheet(LABELGREEN if self.main_power else LABELGRAY)
        self.leds[2].setStyleSheet(LABELGREEN if self.run else LABELGRAY)
        self.leds[3].setStyleSheet(LABELRED if self.neg_override else LABELGRAY)
        self.leds[4].setStyleSheet(LABELRED if self.pos_override else LABELGRAY)
        self.leds[5].setStyleSheet(LABELGREEN if self.home else LABELGRAY)
        self.labs[0].setText("%.02f" % self.position)
        self.labs[1].setText("%.02f" % self.coppia)
        self.labs[2].setText("%.02f" % self.velocity)
        self.labs[3].setText('%s' % self.error1)
        self.labs[4].setText('%s' % self.error2)
        self.labs[5].setText("%.02f" % self.destination)
