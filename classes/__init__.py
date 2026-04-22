# encoding: utf-8

import csv
import math
from copy import deepcopy

from resources import MES07, MES08, MES11
from statics import Tools, settings

from .cpoint import CPOINT
from .cstep import CSTEP

TOOL_OFF = 0  # utensile sollevato
TOOL_ONN = 1  # utensile abbassato

LENGTH_THRESHOLD = 0.1
DEGREE_THRESHOLD = 10.0
EPSILON = 1e-9
VELO_MAX_PENNA = 1.0
VELO_MAX_LASER = 1.0
VELO_MAX_RULLO = 0.5


def _get_linear_steps(plist, offset_x, offset_y, velo_max):
    """Logica comune per utensili lineari (penna e laser)."""
    steps = []
    CSTEP.riga = 0
    old_degree = settings.curr_degree
    first = True

    for pt in plist:
        pt.point[0] += offset_x
        pt.point[1] += offset_y

        if pt.stato1 == pt.stato2 == TOOL_OFF:  # utensile sollevato
            steps.append(CSTEP(pt.point, old_degree, velo_max, TOOL_OFF))
            if pt.length > LENGTH_THRESHOLD:  # punto per esecuzione rampa
                steps.append(CSTEP(pt.point, old_degree, velo_max, TOOL_OFF))

        elif pt.stato1 == pt.stato2 == TOOL_ONN:  # utensile abbassato
            steps.append(CSTEP(pt.point, old_degree, pt.passo1, TOOL_ONN))
            if abs(pt.degree_rel) > DEGREE_THRESHOLD:  # cambio direzione
                steps.append(CSTEP(pt.point, old_degree, pt.passo1, TOOL_ONN))
                if pt.length > LENGTH_THRESHOLD:  # punto per esecuzione rampa
                    steps.append(CSTEP(pt.point, old_degree, pt.passo1, TOOL_ONN))
            if abs(pt.passo1 - pt.passo2) > EPSILON:  # cambio velocità
                steps.append(CSTEP(pt.point, old_degree, pt.passo1, TOOL_ONN))

        elif pt.stato1 == TOOL_OFF and pt.stato2 == TOOL_ONN:  # abbassamento utensile
            steps.append(CSTEP(pt.point, old_degree, velo_max, TOOL_OFF))
            steps.append(CSTEP(pt.point, old_degree, velo_max, TOOL_ONN))

        elif pt.stato1 == TOOL_ONN and pt.stato2 == TOOL_OFF:  # sollevamento utensile
            steps.append(CSTEP(pt.point, old_degree, pt.passo1, TOOL_ONN))
            steps.append(CSTEP(pt.point, old_degree, pt.passo1, TOOL_OFF))

        # elimina il primo step (passo zero) appena generato
        if first and steps:
            steps.pop(0)
            first = False

    if steps and steps[-1].off_onn == TOOL_ONN:  # sollevamento utensile se abbassato
        steps.append(CSTEP(steps[-1].point, old_degree, steps[-1].passo, TOOL_OFF))

    return steps


def get_penna_steps(plist):
    """Genera la lista di CSTEP per l'utensile penna.

    Applica l'offset della posizione penna e delega a _get_linear_steps.

    Args:
        plist: lista di CPOINT che descrivono il percorso.

    Returns:
        Lista di CSTEP pronti per la serializzazione.
    """
    offset_x = float(settings.pos_penna[0]) / settings.scale_unit
    offset_y = float(settings.pos_penna[1]) / settings.scale_unit
    return _get_linear_steps(plist, offset_x, offset_y, VELO_MAX_PENNA)


def get_rullo_steps(plist):
    """Generazione step per utensile rullo (con rotazione)."""
    velo_rot = settings.speed_rullo  # velocità rotazione
    offset_x = float(settings.pos_rullo[0]) / settings.scale_unit
    offset_y = float(settings.pos_rullo[1]) / settings.scale_unit
    steps = []
    CSTEP.riga = 0
    first = True
    remainder = math.fmod(settings.curr_degree, 360.0)
    if remainder > 180.0:
        remainder -= 360.0
    new_degree = settings.curr_degree + settings.perv_degree - remainder

    for pt in plist:
        old_degree = new_degree
        new_degree += pt.degree_rel
        pt.point[0] += offset_x
        pt.point[1] += offset_y

        if pt.stato1 == pt.stato2 == TOOL_OFF:  # movimento sollevato
            steps.append(CSTEP(pt.point, old_degree, VELO_MAX_RULLO, TOOL_OFF))
            if pt.length > LENGTH_THRESHOLD:  # punto rampa
                steps.append(CSTEP(pt.point, old_degree, VELO_MAX_RULLO, TOOL_OFF))

        elif pt.stato1 == TOOL_OFF and pt.stato2 == TOOL_ONN:  # abbassamento iniziale
            steps.append(
                CSTEP(pt.point, new_degree, VELO_MAX_RULLO, TOOL_OFF)
            )  # punto iniziale
            steps.append(CSTEP(pt.point, new_degree, VELO_MAX_RULLO, TOOL_OFF))  # hold
            steps.append(
                CSTEP(pt.point, new_degree, VELO_MAX_RULLO, TOOL_ONN)
            )  # abbassamento
            steps.append(
                CSTEP(pt.point, new_degree, pt.passo2, TOOL_ONN)
            )  # cambio passo

        elif pt.stato1 == pt.stato2 == TOOL_ONN:  # movimento abbassato
            steps.append(CSTEP(pt.point, old_degree, pt.passo1, TOOL_ONN))
            if pt.length > LENGTH_THRESHOLD:  # punto rampa
                steps.append(CSTEP(pt.point, old_degree, pt.passo1, TOOL_ONN))
            if abs(pt.degree_rel) > DEGREE_THRESHOLD:  # cambio direzione
                steps.append(
                    CSTEP(pt.point, old_degree, velo_rot, TOOL_ONN)
                )  # cambio passo
                steps.append(
                    CSTEP(pt.point, new_degree, velo_rot, TOOL_ONN)
                )  # cambio direzione
                steps.append(CSTEP(pt.point, new_degree, velo_rot, TOOL_ONN))  # hold
                steps.append(
                    CSTEP(pt.point, new_degree, pt.passo2, TOOL_ONN)
                )  # cambio passo
            if abs(pt.passo1 - pt.passo2) > EPSILON:  # cambio velocità
                steps.append(CSTEP(pt.point, new_degree, pt.passo2, TOOL_ONN))

        elif pt.stato1 == TOOL_ONN and pt.stato2 == TOOL_OFF:  # sollevamento finale
            steps.append(CSTEP(pt.point, old_degree, VELO_MAX_RULLO, TOOL_ONN))
            steps.append(CSTEP(pt.point, new_degree, VELO_MAX_RULLO, TOOL_OFF))

        # elimina il primo step (passo zero) appena generato
        if first and steps:
            steps.pop(0)
            first = False

    # punto per stop fine percorso
    if steps:
        steps.append(
            CSTEP(steps[-1].point, steps[-1].degree, steps[-1].passo, TOOL_ONN)
        )

    return steps


def get_laser_steps(plist):
    """Genera la lista di CSTEP per l'utensile laser.

    Applica l'offset della posizione laser e delega a _get_linear_steps.

    Args:
        plist: lista di CPOINT che descrivono il percorso.

    Returns:
        Lista di CSTEP pronti per la serializzazione.
    """
    offset_x = float(settings.pos_laser[0]) / settings.scale_unit
    offset_y = float(settings.pos_laser[1]) / settings.scale_unit
    return _get_linear_steps(plist, offset_x, offset_y, VELO_MAX_LASER)


def myfile_from_csv(tool_id, start):
    """Legge il percorso da punti.csv e genera il file myfile.csv.

    Costruisce la lista di CPOINT a partire dalla riga 'start' del CSV,
    inserendo un punto origine e un punto di approccio con utensile
    sollevato, poi delega a myfile_from_plist per la generazione.

    Args:
        tool_id: identificativo dell'utensile (Tools.value).
        start: indice di riga nel CSV da cui iniziare il percorso.

    Returns:
        Tupla (codice, messaggio) da create_myfile, oppure
        tupla (2, MES11, punto, punto) se il rullo ha sollevamenti invalidi.
    """
    plist = [CPOINT([0, 0], 1.0, 0, 0.0)]
    with open("punti.csv", "r") as csvfile:
        reader = list(csv.reader(csvfile, delimiter=";"))
        # angolazione di partenza dalla riga precedente
        settings.perv_degree = float(reader[start - 1][7])
        # punto di approccio: stessa posizione di start ma con utensile sollevato
        approach = list(reader[start])
        approach[4] = approach[5] = "0"  # forza stato1=stato2=TOOL_OFF
        approach[7] = approach[6]  # forza degree2=degree1
        plist.append(CPOINT.deserialize(approach))
        # punti originali dal punto start in poi
        for row in reader[start:]:
            plist.append(CPOINT.deserialize(row))
    return myfile_from_plist(tool_id, plist)


def _validate_rullo_plist(plist):
    """Verifica che il percorso rullo non contenga sollevamenti intermedi.

    Analizza i punti dal terzo al penultimo (il percorso effettivo,
    escludendo approccio iniziale e uscita finale).
    Restituisce la tupla di errore se trova un sollevamento, None altrimenti.
    """
    for idx, pt in enumerate(plist[2:-1], start=2):
        if pt.stato1 == TOOL_OFF or pt.stato2 == TOOL_OFF:
            return 2, MES11, pt.point, plist[idx + 1].point
    return None


def myfile_from_plist(tool_id, plist):
    """Genera myfile.csv dalla lista di CPOINT per l'utensile specificato.

    Seleziona la funzione di generazione step appropriata in base a tool_id.
    Per il rullo, esegue prima la validazione dei sollevamenti intermedi.

    Args:
        tool_id: identificativo dell'utensile (Tools.value).
        plist: lista di CPOINT che descrivono il percorso.

    Returns:
        Tupla (codice, messaggio) da create_myfile, oppure
        tupla (2, MES11, punto, punto) se il rullo ha sollevamenti invalidi.
    """
    if tool_id == Tools.Laser.value:
        return create_myfile(get_laser_steps(deepcopy(plist)))
    elif tool_id == Tools.Rullo.value:
        error = _validate_rullo_plist(plist)
        if error is not None:
            return error
        return create_myfile(get_rullo_steps(deepcopy(plist)))
    else:
        return create_myfile(get_penna_steps(deepcopy(plist)))


def create_myfile(steps):
    """Serializza la lista di CSTEP nel file myfile.csv.

    Args:
        steps: lista di CSTEP da scrivere.

    Returns:
        Tupla (1, MES07) se il numero di step supera 32700,
        tupla (0, MES08) altrimenti.
    """
    with open("myfile.csv", "w") as csvfile:
        sw = csv.writer(csvfile, delimiter=";")
        for step in steps:
            sw.writerow(step.serialize())
    if len(steps) > 32700:
        return 1, MES07
    else:
        return 0, MES08
