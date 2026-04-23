# encoding: utf-8
from PySide6.QtCore import QSettings


class CSettings:
    sort_by_color = False
    curr_pos_x = 0.0
    curr_pos_y = 0.0
    curr_degree = 0.0
    raccordo = list()

    def __init__(self):
        self.settings = QSettings('settings.ini', QSettings.IniFormat)
        self.settings.setFallbacksEnabled(False)
        self.plcUrl = self.settings.value("plcUrl", "192.168.0.21")
        self.plcPort = int(self.settings.value("plcPort", 9600))
        self.scale_unit = float(self.settings.value("scale_unit", 100.0))
        self.offset_gradi = int(self.settings.value("offset_gradi", -123))
        self.speed_rullo = float(self.settings.value("speed_rullo", 0.10))
        self.pos_penna = self.settings.value("pos_penna", (0.0, 0.0))
        self.pos_laser = self.settings.value("pos_laser", (0.0, 0.0))
        self.pos_rullo = self.settings.value("pos_rullo", (0.0, 0.0))
        self.max_size = self.settings.value("max_size", (1500.0, 600.0))
        self.pos_end = self.settings.value("pos_end", (0.0, 0.0))

    def save(self):
        self.settings.setValue("plcUrl", self.plcUrl)
        self.settings.setValue("plcPort", self.plcPort)
        self.settings.setValue("scale_unit", self.scale_unit)
        self.settings.setValue("offset_gradi", self.offset_gradi)
        self.settings.setValue("speed_rullo", self.speed_rullo)
        self.settings.setValue("pos_penna", self.pos_penna)
        self.settings.setValue("pos_laser", self.pos_laser)
        self.settings.setValue("pos_rullo", self.pos_rullo)
        self.settings.setValue("max_size", self.max_size)
        self.settings.setValue("pos_end", self.pos_end)

    @property
    def recent_files(self):
        return self.settings.value("recent_files", "").split("|")

    def set_recent_files(self, recent_files):
        self.settings.setValue("recent_files", "|".join(recent_files))
