# encoding: utf-8
import math
import os
from enum import Enum
from struct import pack
from struct import unpack

from PySide6.QtGui import QColor
from ezdxf import colors

from ccolorpref import CColorPref
from cmemopref import MemoHelper
from csettings import CSettings

settings = CSettings()
memo_helper = MemoHelper()


class ButtonBit(Enum):
    Automatic = 0
    Start = 1
    Manual = 2
    Homing = 3
    Reset = 4
    Hold = 5
    EntTranFile = 6
    Notify = 7
    TransMode = 8


class StatusBit(Enum):
    HomingInCorso = 0
    HomingEseguito = 1
    ErroreECT = 2
    ErroreMC = 3
    ErrorePLC = 4
    NJ_Active = 5
    ML_StartPath = 6
    ML_Done = 7
    FR_Done = 8
    FR_Busy = 9
    FR_Error = 10
    FR_EndReadFileData = 11
    NJ_Automatico = 12
    NJ_Manuale = 13
    NJ_Hold = 14
    NJ_Emergenza = 15
    NJ_Homing = 16
    ValvRULLO = 17
    ValvPENNA = 18
    ValvLASER = 19
    RichHomeCambioTool = 20
    NJ_Ready = 21
    NJ_Error = 22


class NjWrite(Enum):
    Buttons = (1, 0, 1)
    Override = (2, 2, 1)
    OffsetLaser = (3, 3, 1)
    OffsetLaserFloat = (3, 3, 4)
    NumeroPunti = (6, 6, 1)
    VelJog = (7, 7, 1)
    TipoUtensile = (8, 8, 1)


class NjRead(Enum):
    Override = (11, 2, 1)
    VelJog = (12, 7, 1)
    Nj_Status = (15, 50, 2)
    OverrideRunPoint = (19, 55, 1)
    RunningPoint_ML = (20, 59, 1)
    Axis0_Status = (21, 60, 20)
    Axis1_Status = (22, 100, 20)
    Axis2_Status = (23, 140, 20)


class Tools(Enum):
    Rullo = 0
    Penna = 1
    Laser = 2


def rounded(p):
    return round(p[0], 5), round(p[1], 5)  # precisione un 1/100 mm


def equals(a, b):
    return rounded(a) == rounded(b)


def swap_bytes(s):
    sw = bytes([c for t in zip(s[1::2], s[::2]) for c in t])
    return sw


def vector_length(pt1, pt2):
    """
    Restituisce la distanza tra due punti.
    Param pt1: punto di partenza.
    Param pt2: punto di arrivo.
    """
    if equals(pt1, pt2):
        return 0.0
    else:
        delta_x = pt2[0] - pt1[0]
        delta_y = pt2[1] - pt1[1]
        return math.sqrt(math.pow(delta_x, 2) + math.pow(delta_y, 2))


def get_vector_angle(pt1, pt2):
    """
    Restituisce l'angolazione di un vettore in 360 gradi.
    Param pt1 punto iniziale del vettore.
    Param pt2 punto finale del vettore.
    """
    if equals(pt1, pt2):
        return 0.0
    else:
        x1, y1 = pt1
        x2, y2 = pt2
        delta_x = x2 - x1
        delta_y = y2 - y1
        radianti = math.atan2(-delta_y, delta_x)
        radianti %= (2 * math.pi)
        gradi = math.degrees(radianti)
        return round(gradi, 6)


def int2bit(num):
    return '{:016b}'.format(num)[::-1]


def float_to_long_bits(value):
    return unpack('Q', pack('d', value))[0]


def long_bits_to_float(bits):
    return unpack('d', pack('Q', bits))[0]


def get_qt_color(color_code):
    return QColor(colors.DXF_DEFAULT_COLORS[color_code]) \
        if color_code in range(1, 257) \
        else QColor("white")


def get_color_pref(color):
    for item in memo_helper.pref_colors:
        if item.colore == color:
            return item
    newone = CColorPref(color, 20, 99, 1)
    memo_helper.pref_colors.append(newone)
    return newone


def ping_plotter(ipaddress):
    return os.system('ping -c 1 ' + ipaddress) == 0
