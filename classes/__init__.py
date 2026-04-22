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
    """
    Genera una sequenza di step lineari per utensili a movimento semplice (penna e laser).

    La funzione trasforma i punti di percorso (CPOINT) in comandi per il PLC (CSTEP),
    gestendo l'abbassamento/sollevamento dell'utensile, i cambi di direzione
    (tramite DEGREE_THRESHOLD) e le rampe di accelerazione (tramite LENGTH_THRESHOLD).

    Args:
        plist (list[CPOINT]): Lista di punti di percorso da elaborare.
        offset_x (float): Offset di coordinata X da applicare a ogni punto.
        offset_y (float): Offset di coordinata Y da applicare a ogni punto.
        velo_max (float): Velocità massima di spostamento per l'utensile.

    Returns:
        list[CSTEP]: Lista di step pronti per la serializzazione in CSV.
    """
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
        # abbassamento utensile
        elif pt.stato1 == TOOL_OFF and pt.stato2 == TOOL_ONN:
            steps.append(CSTEP(pt.point, old_degree, velo_max, TOOL_OFF))
            steps.append(CSTEP(pt.point, old_degree, velo_max, TOOL_ONN))
        # sollevamento utensile
        elif pt.stato1 == TOOL_ONN and pt.stato2 == TOOL_OFF:
            steps.append(CSTEP(pt.point, old_degree, pt.passo1, TOOL_ONN))
            steps.append(CSTEP(pt.point, old_degree, pt.passo1, TOOL_OFF))
        # elimina il primo step (passo zero) appena generato
        if first and steps:
            steps.pop(0)
            first = False

    # sollevamento utensile se abbassato
    if steps and steps[-1].off_onn == TOOL_ONN:
        steps.append(CSTEP(steps[-1].point, old_degree, steps[-1].passo, TOOL_OFF))

    # 1. Aggiungi la copia (senza preoccuparti della riga ora)
    if steps:
        steps.insert(0, deepcopy(steps[0]))

    # 2. Ricalcola TUTTE le righe per garantire la progressione 0, 1, 2...
    for i, step in enumerate(steps):
        step.riga = i

    return steps


def _get_penna_steps(plist):
    """
    Genera la lista di CSTEP specifica per l'utensile penna.

    Calcola l'offset di posizione della penna basandosi sulle impostazioni globali
    e delega la generazione della sequenza a _get_linear_steps.

    Args:
        plist (list[CPOINT]): Lista di punti di percorso.

    Returns:
        list[CSTEP]: Sequenza di step configurata per la penna.
    """
    offset_x = float(settings.pos_penna[0]) / settings.scale_unit
    offset_y = float(settings.pos_penna[1]) / settings.scale_unit
    return _get_linear_steps(plist, offset_x, offset_y, VELO_MAX_PENNA)


def _get_rullo_steps(plist):
    """
    Genera la lista di CSTEP specifica per l'utensile rullo, gestendo la rotazione.

    A differenza degli utensili lineari, il rullo richiede la gestione dell'angolo
    di rotazione dell'asse C. La funzione calcola l'incremento del grado basandosi
    sulla direzione del movimento e inserisce step di hold per i cambi di direzione.

    Args:
        plist (list[CPOINT]): Lista di punti di percorso.

    Returns:
        list[CSTEP]: Sequenza di step configurata per il rullo con rotazione asse C.
    """
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


def _get_laser_steps(plist):
    """
    Genera la lista di CSTEP specifica per l'utensile laser.

    Calcola l'offset di posizione del laser basandosi sulle impostazioni globali
    e delega la generazione della sequenza a _get_linear_steps.

    Args:
        plist (list[CPOINT]): Lista di punti di percorso.

    Returns:
        list[CSTEP]: Sequenza di step configurata per il laser.
    """
    offset_x = float(settings.pos_laser[0]) / settings.scale_unit
    offset_y = float(settings.pos_laser[1]) / settings.scale_unit
    return _get_linear_steps(plist, offset_x, offset_y, VELO_MAX_LASER)


def _validate_rullo_plist(plist):
    """
    Verifica l'integrità del percorso per l'utensile rullo.

    Il rullo non supporta sollevamenti dell'utensile intermedi durante l'esecuzione
    del tracciato (solo all'inizio e alla fine). Questa funzione scansiona il
    percorso per identificare eventuali stati TOOL_OFF non validi.

    Args:
        plist (list[CPOINT]): Lista di punti di percorso da validare.

    Returns:
        tuple | None: Ritorna una tupla (indice, messaggio_errore, punto_inizio, punto_fine)
                      se viene trovato un errore, altrimenti None.
    """
    for idx, pt in enumerate(plist[2:-1], start=2):
        if pt.stato1 == TOOL_OFF or pt.stato2 == TOOL_OFF:
            return 2, MES11, pt.point, plist[idx + 1].point
    return None


def _create_myfile(steps):
    """
    Serializza la lista di CSTEP nel file fisico 'myfile.csv'.

    Scrive ogni step nel file utilizzando il separatore ';' e verifica che il
    numero totale di step non superi il limite massimo supportato dal PLC (32700).

    Args:
        steps (list[CSTEP]): Lista di step da scrivere su disco.

    Returns:
        tuple: Una tupla (codice_errore, messaggio_risorsa) dove il codice 0
               indica successo e 1 indica superamento del limite di righe.
    """
    with open("myfile.csv", mode="w", encoding="utf-8") as csvfile:
        sw = csv.writer(csvfile, delimiter=";")
        for step in steps:
            sw.writerow(step.serialize())
    if len(steps) > 32700:
        return 1, MES07
    else:
        return 0, MES08


def myfile_from_csv(tool_id, start):
    """
    Processo completo di generazione file partendo da un file CSV di punti.

    Legge 'punti.csv', recupera l'angolazione di partenza, crea un punto di approccio
    con utensile sollevato e genera la sequenza finale di step.

    Args:
        tool_id (int): Identificativo dell'utensile selezionato (da Tools.value).
        start (int): Indice di riga nel CSV da cui iniziare l'estrazione del percorso.

    Returns:
        tuple: Risultato della creazione del file (codice, messaggio) o errore
                di validazione per il rullo.
    """
    plist = [CPOINT([0, 0], 1.0, 0, 0.0)]
    with open("punti.csv", mode="r", encoding="utf-8") as csvfile:
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


def myfile_from_plist(tool_id, plist):
    """
    Interfaccia di alto livello per generare il file di output da una lista di punti.

    In base al tool_id, seleziona l'algoritmo di generazione step appropriato
    (Laser, Penna o Rullo) e, nel caso del rullo, esegue la validazione preventiva.

    Args:
        tool_id (int): Identificativo dell'utensile (Tools.value).
        plist (list[CPOINT]): Lista di punti di percorso.

    Returns:
        tuple: Risultato della creazione del file (codice, messaggio) o errore
                di validazione per il rullo.
    """
    if tool_id == Tools.Laser.value:
        return _create_myfile(_get_laser_steps(deepcopy(plist)))
    if tool_id == Tools.Penna.value:
        return _create_myfile(_get_penna_steps(deepcopy(plist)))
    # tool_id == Tools.Rullo.value:
    error = _validate_rullo_plist(plist)
    if error is not None:
        return error
    return _create_myfile(_get_rullo_steps(deepcopy(plist)))
