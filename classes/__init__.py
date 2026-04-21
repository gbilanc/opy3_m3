# encoding: utf-8

import csv
import math
from copy import deepcopy

from resources import *
from statics import Tools
from statics import settings
from .cpoint import CPOINT
from .cstep import CSTEP

tool_off = 0  # utensile sollevato
tool_onn = 1  # utensile abbassato


def get_penna_steps(plist):
    velo_max = 1.0  # velocità massima
    offset_x = float(settings.pos_penna[0]) / settings.scale_unit
    offset_y = float(settings.pos_penna[1]) / settings.scale_unit
    steps = list()
    CSTEP.riga = 0
    old_degree = settings.curr_degree
    for pt in plist:
        pt.point[0] += offset_x
        pt.point[1] += offset_y

        if pt.stato1 == pt.stato2 == tool_off:  # utensile sollevato
            steps.append(CSTEP(pt.point, old_degree, velo_max, tool_off))
            if pt.length > 0.1:  # 1 punto x esecuzione rampa
                steps.append(CSTEP(pt.point, old_degree, velo_max, tool_off))

        if pt.stato1 == pt.stato2 == tool_onn:  # utensile abbassato
            steps.append(CSTEP(pt.point, old_degree, pt.passo1, tool_onn))
            if abs(pt.degree_rel) > 10.0:  # 1 punti x cambio direzione
                steps.append(CSTEP(pt.point, old_degree, pt.passo1, tool_onn))
                if pt.length > 0.1:  # 1 punto x esecuzione rampa
                    steps.append(CSTEP(pt.point, old_degree, pt.passo1, tool_onn))
            if pt.passo1 != pt.passo2:  # 1 punti x cambio velocità
                steps.append(CSTEP(pt.point, old_degree, pt.passo1, tool_onn))

        if pt.stato1 == tool_off and pt.stato2 == tool_onn:  # abbassamento utensile
            steps.append(CSTEP(pt.point, old_degree, velo_max, tool_off))
            steps.append(CSTEP(pt.point, old_degree, velo_max, tool_onn))

        if pt.stato1 == tool_onn and pt.stato2 == tool_off:  # sollevamento utensile
            steps.append(CSTEP(pt.point, old_degree, pt.passo1, tool_onn))
            steps.append(CSTEP(pt.point, old_degree, pt.passo1, tool_off))

    steps.pop(0)  # eliminazione passo zero
    if steps[-1].off_onn == tool_onn:  # sollevamento utensile se abbassato
        steps.append(CSTEP(steps[-1].point, old_degree, steps[-1].passo, tool_off))
    # fine_x = float(settings.pos_end[0]) / settings.scale_unit
    # fine_y = float(settings.pos_end[1]) / settings.scale_unit
    # steps.append(CSTEP([fine_x, fine_y], old_degree, velo_max, tool_off))
    # steps.append(CSTEP([fine_x, fine_y], old_degree, velo_max, tool_off))
    return steps


def get_rullo_steps(plist):
    velo_max = 0.5  # velocità traslazione
    velo_max2 = settings.speed_rullo  # velocità rotazione
    offset_x = float(settings.pos_rullo[0]) / settings.scale_unit
    offset_y = float(settings.pos_rullo[1]) / settings.scale_unit
    steps = list()
    CSTEP.riga = 0
    remainder = math.fmod(settings.curr_degree, 360.0)
    if remainder > 180.0:
        remainder -= 360.0
    new_degree = settings.curr_degree + settings.perv_degree - remainder
    for current_point in plist:
        old_degree = new_degree
        new_degree += current_point.degree_rel
        current_point.point[0] += offset_x
        current_point.point[1] += offset_y

        if current_point.stato1 == current_point.stato2 == tool_off:  # movimento sollevato
            steps.append(CSTEP(current_point.point, old_degree, velo_max, tool_off))
            if current_point.length > 0.1:  # 10 cm punto rampa
                steps.append(CSTEP(current_point.point, old_degree, velo_max, tool_off))

        if current_point.stato1 == tool_off and current_point.stato2 == tool_onn:  # abbassamento iniziale
            steps.append(CSTEP(current_point.point, new_degree, velo_max, tool_off))  # punto iniziale
            steps.append(CSTEP(current_point.point, new_degree, velo_max, tool_off))  # ============== ( X HOLD )
            steps.append(CSTEP(current_point.point, new_degree, velo_max, tool_onn))  # abbassamento
            steps.append(CSTEP(current_point.point, new_degree, current_point.passo2, tool_onn))  # cambio passo

        if current_point.stato1 == current_point.stato2 == tool_onn:  # movimento abbassato
            steps.append(CSTEP(current_point.point, old_degree, current_point.passo1, tool_onn))
            if current_point.length > 0.1:  # 10cm punto rampa
                steps.append(CSTEP(current_point.point, old_degree, current_point.passo1, tool_onn))
            if abs(current_point.degree_rel) > 10.0:
                steps.append(CSTEP(current_point.point, old_degree, velo_max2, tool_onn))  # cambio passo
                steps.append(CSTEP(current_point.point, new_degree, velo_max2, tool_onn))  # cambio direzione
                steps.append(CSTEP(current_point.point, new_degree, velo_max2, tool_onn))  # ================
                steps.append(CSTEP(current_point.point, new_degree, current_point.passo2, tool_onn))  # cambio passo
            if current_point.passo1 != current_point.passo2:
                steps.append(CSTEP(current_point.point, new_degree, current_point.passo2, tool_onn))  # cambio passo

        if current_point.stato1 == tool_onn and current_point.stato2 == tool_off:  # sollevamento finale
            steps.append(CSTEP(current_point.point, old_degree, velo_max, tool_onn))
            steps.append(CSTEP(current_point.point, new_degree, velo_max, tool_off))

    # punto x stop fine percorso
    steps.append(CSTEP(steps[-1].point, steps[-1].degree, steps[-1].passo, tool_onn))

    steps.pop(0)  # eliminazione passo zero
    return steps


def get_laser_steps(plist):
    velo_max = 1.0
    offset_x = float(settings.pos_laser[0]) / settings.scale_unit
    offset_y = float(settings.pos_laser[1]) / settings.scale_unit
    steps = list()
    CSTEP.riga = 0
    old_degree = settings.curr_degree
    for pt in plist:
        pt.point[0] += offset_x
        pt.point[1] += offset_y

        if pt.stato1 == pt.stato2 == tool_off:
            steps.append(CSTEP(pt.point, old_degree, velo_max, tool_off))
            if pt.length > 0.1:
                steps.append(CSTEP(pt.point, old_degree, velo_max, tool_off))

        if pt.stato1 == pt.stato2 == tool_onn:
            steps.append(CSTEP(pt.point, old_degree, pt.passo1, tool_onn))
            if abs(pt.degree_rel) > 10.0:
                steps.append(CSTEP(pt.point, old_degree, pt.passo1, tool_onn))
                if pt.length > 0.1:
                    steps.append(CSTEP(pt.point, old_degree, pt.passo1, tool_onn))
            if pt.passo1 != pt.passo2:
                steps.append(CSTEP(pt.point, old_degree, pt.passo1, tool_onn))

        if pt.stato1 == tool_off and pt.stato2 == tool_onn:
            steps.append(CSTEP(pt.point, old_degree, velo_max, tool_off))
            steps.append(CSTEP(pt.point, old_degree, velo_max, tool_onn))

        if pt.stato1 == tool_onn and pt.stato2 == tool_off:
            steps.append(CSTEP(pt.point, old_degree, pt.passo1, tool_onn))
            steps.append(CSTEP(pt.point, old_degree, pt.passo1, tool_off))

    steps.pop(0)
    if steps[-1].off_onn == tool_onn:
        steps.append(CSTEP(steps[-1].point, old_degree, steps[-1].passo, tool_off))
    return steps


def myfile_from_csv(tool_id, start):
    plist = list()
    plist.append(CPOINT([0, 0], 1.0, 0, 0.0))
    with open("punti.csv", 'r') as f1:
        lines = f1.readlines()
        settings.perv_degree = float(lines[start - 1].split(";")[7])
        data = lines[start].split(";")
        data[4] = data[5] = 0  # UTENSILE SOLLEVATO
        data[7] = data[6]
        plist.append(CPOINT.deserialize(data))
        for item in lines[start:]:
            plist.append(CPOINT.deserialize(item.split(";")))
    return myfile_from_plist(tool_id, plist)


def myfile_from_plist(tool_id, plist):
    if tool_id == Tools.Laser.value:
        return create_myfile(get_laser_steps(deepcopy(plist)))
    elif tool_id == Tools.Rullo.value:
        for idx, current_point in enumerate(plist[2:-1]):  # analisi sollevamenti non consentiti
            if current_point.stato1 == 0 or current_point.stato2 == 0:
                return 2, MES11, current_point.point, plist[idx + 3].point
        return create_myfile(get_rullo_steps(deepcopy(plist)))
    else:
        return create_myfile(get_penna_steps(deepcopy(plist)))


def create_myfile(steps):
    with open('myfile.csv', 'w') as csvfile:
        sw = csv.writer(csvfile, delimiter=';')
        for step in steps:
            sw.writerow(step.serialize())
    if len(steps) > 32700:
        return 1, MES07
    else:
        return 0, MES08
