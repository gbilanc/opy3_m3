# encoding: utf-8

import csv

from PySide6.QtCore import QPointF
from PySide6.QtCore import QRectF
from PySide6.QtCore import QSizeF
from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush
from PySide6.QtGui import QFont
from PySide6.QtGui import QPainter
from PySide6.QtGui import QPainterPath
from PySide6.QtGui import QPen
from PySide6.QtWidgets import QGraphicsScene
from PySide6.QtWidgets import QGraphicsView

from statics import settings


class GVPlotter(QGraphicsView):

    def __init__(self, parent=None):
        QGraphicsView.__init__(self, parent)
        self.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.setRenderHint(QPainter.RenderHint.TextAntialiasing)
        self.setScene(QGraphicsScene(0, -float(settings.max_size[1]),
                                     float(settings.max_size[0]),
                                     float(settings.max_size[1]), self))
        self.__plot_points = list()
        self.__start_point = None
        self.point = None
        self.rectangle = None
        self.workspace = None
        self.selected_layer = None

    def drawBackground(self, painter, rect):
        """
        Disegna il background del plotter e traccia linee di riferimento
        param painter:
        param rect:
        return:
        """
        scene_rect = self.sceneRect().toRect()
        painter.fillRect(scene_rect, QBrush(Qt.white))
        green_pen = QPen(Qt.darkGreen)
        painter.setPen(green_pen)
        painter.drawRect(scene_rect)
        gray_pen = QPen(Qt.gray)
        gray_pen.setStyle(Qt.DashLine)
        painter.setPen(gray_pen)
        painter.setFont(QFont("Roman", 8, QFont.Weight.Bold))
        for x in range(0, scene_rect.width(), 100):
            painter.drawLine(x, -scene_rect.height(), x, 0)
            painter.drawText(x - 10, 10, 20, 10, Qt.AlignCenter, "%d" % (x / 100))
        for y in range(0, scene_rect.height(), 100):
            painter.drawLine(0, -y, scene_rect.width(), -y)

    def wheelEvent(self, event):
        """
        Scala la vista con la rotella del mouse
        param event:
        """
        factor = 1.41 ** (+event.angleDelta().y() / 240.0)
        self.scale(factor, factor)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.point = self.mapToScene(event.pos())

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            try:
                self.scene().removeItem(self.rectangle)
                self.rectangle = None
            except RuntimeError:
                pass
            rect = QRectF(self.point, self.mapToScene(event.pos()))
            self.fitInView(rect, Qt.KeepAspectRatio)

    def mouseMoveEvent(self, event):
        try:
            self.scene().removeItem(self.rectangle)
            self.rectangle = None
        except RuntimeError:
            pass
        rect = QRectF(self.point, self.mapToScene(event.pos()))
        pen = QPen(Qt.red, 1, Qt.DashDotLine)
        self.rectangle = self.scene().addRect(rect, pen)

    def enterEvent(self, event):
        self.setCursor(Qt.CrossCursor)

    def leaveEvent(self, event):
        self.setCursor(Qt.ArrowCursor)

    def translate_workspace(self, off_x, off_y):
        if self.workspace is not None:
            self.workspace.translate(off_x, off_y)
            self.invalidate()

    def rotate_workspace(self, radians):
        if self.workspace is not None:
            self.workspace.rotate(radians)
            self.invalidate()

    def flip_workspace(self, mode):
        if self.workspace is not None:
            self.workspace.flip(mode)
            self.invalidate()

    def select_layer_with_name(self, layer_name):
        """
        Imposta il layer selezionato dall'utente
        param layer_name: nome del layer selezionato
        """
        self.selected_layer = self.workspace.select_layer_with_name(layer_name)
        self.invalidate()

    def set_start_point(self, value):
        """
        Imposta il punto iniziale da cui iniziare la generazione
        del file myfile.csv da inviare al controller
        param value: coordinate del punto iniziale
        """
        self.__start_point = value
        self.invalidate(True)

    def invalidate(self, curr_only=False):
        """
        Disegna gli elementi nella scena
        param curr_only: se true disegna solo gli elementi del layer selezionato
        """
        scene = self.scene()
        scene.clear()
        if self.workspace is not None:
            if curr_only:
                if self.selected_layer is not None:
                    self.selected_layer.draw(scene)
            else:
                for layer in self.workspace.layers:
                    layer.draw(scene)
            if self.__start_point is not None:
                qpoint = QPointF(float(self.__start_point[0]) * settings.scale_unit - 1.5,
                                 -float(self.__start_point[1]) * settings.scale_unit - 1.5)
                qsize = QSizeF(3.0, 3.0)
                scene.addEllipse(QRectF(qpoint, qsize), QPen(Qt.black), Qt.blue)
            self.update()

    def clear_plot_points(self):
        del self.__plot_points[:]

    def draw_plot_points(self, num_riga, offset):
        """
        Anteprima del plottaggio in corso
        param num_riga: riga corrente
        """
        if len(self.__plot_points) == 0:
            with open('myfile.csv', 'r') as csv_file:
                spam_reader = csv.reader(csv_file, delimiter=';')
                for i in spam_reader:
                    self.__plot_points.append(i)
        counter = 0
        path = QPainterPath()
        path.moveTo(0, 0)
        for item in self.__plot_points:
            qpoint = QPointF(float(item[1]) / 10, -float(item[2]) / 10)
            path.lineTo(qpoint) if item[5] == '1' else path.moveTo(qpoint)
            counter += 1
            if counter > num_riga:
                break
        path.translate(-float(offset[0]), float(offset[1]))
        self.scene().addPath(path, QPen(Qt.darkCyan))

    def draw_error_segment(self, from_point, to_point):
        path = QPainterPath()
        path.moveTo(QPointF(from_point[0] * 100, -from_point[1] * 100))
        path.lineTo(QPointF(to_point[0] * 100, -to_point[1] * 100))
        self.scene().addPath(path, QPen(Qt.red))
