# encoding: utf-8
"""
Modulo per la gestione dei layer di un file DXF.
Contiene la classe CLayer per l'organizzazione delle entità geometriche,
la gestione dei colori, le trasformazioni spaziali e la generazione
di percorsi di plottaggio per il PLC.
"""

import csv

from PySide6.QtGui import QFont
from PySide6.QtWidgets import QGraphicsItem

from statics import equals
from statics import get_color_pref
from statics import get_vector_angle
from statics import memo_helper
from statics import settings
from statics import vector_length
from .cpoint import CPOINT
from .cpoliline import CPoliline
from .unitize import unitize


def first_line(lines):
    points = [line.start for line in lines]
    points.extend([line.end for line in lines if not line.is_closed])
    for line in lines:
        if line.start in points:
            return line
        if line.end in points:
            line.reverse()
            return line
    return None


def next_line(lines, checkline):
    for line in lines:
        if equals(checkline.end, line.start):
            return line
        if equals(checkline.end, line.end):
            line.reverse()
            return line
    return None


class CLayer(QGraphicsItem):
    """
    Rappresenta un layer grafico composto da diverse polilinee.
    Gestisce la visibilità, la selezione, l'orientamento e l'elaborazione 
    geometrica delle linee per la generazione del percorso di lavoro.
    """

    def __init__(self, layer, entities):
        """
        Inizializza un layer con nome, entità geometriche e colori.
        
        Args:
            layer: Oggetto layer del file DXF.
            entities: Lista di entità geometriche da convertire in CPoliline.
        """
        QGraphicsItem.__init__(self)
        self.name = layer.dxf.name
        self.lines = [CPoliline(entity, layer) for entity in entities]
        self.color = layer.color
        self.colors = list(set([line.color for line in self.lines]))
        self.visible = True
        self.selected = False
        self.reverse = False
        self.join_lines()
        self.visible_lines = list()
        self.elem_count = 0
        self.unitized = False

    def __str__(self):
        """Ritorna una stringa riassuntiva del contenuto del layer (elementi, polilinee e punti totali)."""
        total_points = sum([len(line.points) for line in self.lines])
        return """%d elementi, %d poli linee, %d punti totali""" % (self.elem_count, len(self.lines), total_points)

    @property
    def bounds(self):
        """Ritorna i limiti (minX, minY, maxX, maxY) di tutte le linee del layer."""
        points = list()
        points.extend(line.points for line in self.lines)
        return (min([pt[0] for pt in points[0]]),
                min([pt[1] for pt in points[0]]),
                max([pt[0] for pt in points[0]]),
                max([pt[1] for pt in points[0]]))

    @property
    def center(self):
        bounds = self.bounds
        return (bounds[0] + bounds[2]) / 2, (bounds[1] + bounds[3]) / 2

    @property
    def is_laser(self):
        return self.name.startswith("TAGLIO")

    @property
    def is_penna(self):
        if self.name.isnumeric():
            return int(self.name) < 1000
        else:
            return False

    def draw(self, qt_scene):
        """
        Disegna il layer sulla scena Qt.
        Se il layer è selezionato, disegna anche l'indicatore di progresso
        numerato per ogni segmento.
        """
        if not self.unitized:
            self.unitize_lines()

        font = QFont("Lucida", 1, QFont.Weight.Light)
        # font.setPointSizeF(1.0)
        font.setStretch(QFont.Stretch.UltraCondensed)
        del settings.raccordo[:]
        if self.visible and len(self.visible_lines) > 0:
            counter = 0
            total_points = 1
            for item in self.visible_lines:
                item.draw(qt_scene)
                if self.selected:
                    item.draw_progressivo(qt_scene, counter, font)
                    settings.raccordo.append(total_points)
                    total_points += item.points_count
                    counter += 1

    def unitize_lines(self):
        """
        Organizza le linee del layer in una sequenza logica di plottaggio
        basata sulle preferenze di colore e sulla modalità di ordinamento.
        """
        sorted_colors = sorted(memo_helper.pref_colors, key=lambda p: p.ordine)
        selected_colors = [item.colore for item in sorted_colors if item.genera == 1]
        if settings.sort_by_color:
            self.sort_lines_by_color(selected_colors)
        else:
            result = [line for line in self.lines if line.color in selected_colors]
            if len(result) > 0:
                self.visible_lines, self.elem_count = unitize(result, self.reverse)
                self.unitized = True

    def translate(self, off_x, off_y):
        """Sposto tutte le linee del layer di un offset X e Y."""
        for item in self.lines:
            item.translate(off_x, off_y)

    def scale(self, fact):
        """Applica un fattore di scala a tutte le linee del layer."""
        for item in self.lines:
            item.scale(fact)

    def rotate(self, radians, center):
        """Ruota tutte le linee del layer attorno a un centro dato."""
        for item in self.lines:
            item.rotate(radians, center)

    def flip(self, mode, center):
        """Specchia tutte le linee del layer rispetto all'asse specificato (mode)."""
        for item in self.lines:
            item.flip(mode, center)

    def do_visible(self, value):
        self.visible = value

    def do_selected(self, value):
        self.selected = value

    def do_reverse(self, value):
        self.reverse = value

    def set_forma_inizio(self, index):
        old_lines = self.visible_lines[:]
        self.visible_lines = old_lines[index:]
        self.visible_lines.extend(old_lines[:index])

    def get_points(self):
        """ Estrae la lista dei punti dai segmenti del layer
        esclude punti doppi o troppo vicini (< 1/10 mm)
        assegna position strumento arrivo e partenza
        assegna velocità di esecuzione arrivo e partenza
        calcola angolazione su punti precedente e successivo
        """
        plist = list()
        if len(self.visible_lines) > 0:
            plist.append(CPOINT([0, 0], 1.0, 0, 0.0))  # azzeramento macchina
            plist.append(CPOINT(self.visible_lines[0].points[0], 1.0, 0, 0.0))  # punto partenza
            plist[-1].length = vector_length(plist[-2].point, plist[-1].point)
            for line in self.visible_lines:
                color_pref = get_color_pref(line.color)
                if not equals(plist[-1].point, line.points[0]):
                    plist[-1].stato2 = 0  # utensile sollevato
                    plist[-1].passo2 = float(color_pref.passo) / 100
                else:
                    plist[-1].stato2 = 1  # utensile abbassato
                    plist[-1].passo2 = float(color_pref.passo) / 100
                for point in line.points:
                    if not equals(plist[-1].point, point):  # << esclusione punti doppi
                        plist.append(CPOINT(point, float(color_pref.passo) / 100, 1, 0.0))
                        plist[-1].stato1 = plist[-2].stato2
                        plist[-1].length = vector_length(plist[-2].point, point)
                        degree = get_vector_angle(plist[-2].point, point)
                        plist[-2].degree2 = plist[-1].degree1 = degree
            plist[-1].degree2 = plist[-1].degree1
            # serializzazione punti
            with open("punti.csv", 'w') as csvfile:
                sw = csv.writer(csvfile, delimiter=';')
                for pt in plist:
                    sw.writerow(pt.serialize())
        return plist

    """ 
    seleziona le linee per colore, estrae le sole linee senza margini
    congruenti con altre linee, seleziona tra le linee restati quelle con
    margini congruenti e le unisce in una unica linea che aggiunge alla lista
    finché la lista delle linee restanti non è vuota
    """

    def join_lines(self):
        """
        Unisce segmenti di linea adiacenti dello stesso colore in polilinee
        continue per ottimizzare il percorso di plottaggio.
        """
        unique_lines = list()
        for color in self.colors:
            all_lines = [line for line in self.lines if line.color == color]
            points = [line.start for line in all_lines]
            points.extend([line.end for line in all_lines if not line.is_closed])
            points = [pt for pt in points if points.count(pt) == 1]
            for line in all_lines:
                if line.start in points and line.end in points:
                    unique_lines.append(line)
            res_lines = [line for line in all_lines if line not in unique_lines]
            while res_lines:
                line = first_line(res_lines)
                res_lines.remove(line)
                nextline = next_line(res_lines, line)
                while nextline:
                    line.points.extend(nextline.points)
                    res_lines.remove(nextline)
                    nextline = next_line(res_lines, nextline)

                unique_lines.append(line)
        self.lines = unique_lines

    def sort_lines_by_color(self, selected_colors):
        result = list()
        for color in selected_colors:
            lines = [line for line in self.lines if line.color == color]
            ordered, counter = unitize(lines, self.reverse)
            result.extend(ordered)
        self.visible_lines = result
        self.elem_count = len(result)
        self.unitized = True
