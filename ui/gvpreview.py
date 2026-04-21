import csv
import time

from PySide6.QtCore import QLineF
from PySide6.QtCore import QPointF
from PySide6.QtCore import QRectF
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter
from PySide6.QtGui import QPen
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QGraphicsScene
from PySide6.QtWidgets import QGraphicsView

from statics import settings


class GVPreview(QGraphicsView):
    
    def __init__(self, parent=None):
        QGraphicsView.__init__(self, parent)      
        self.setWindowTitle('anteprima')
        self.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.setRenderHint(QPainter.RenderHint.TextAntialiasing)
        self.setScene(QGraphicsScene(0, -float(settings.max_size[1]),
                      float(settings.max_size[0]), float(settings.max_size[1]),
                      self))
        self.alist = None
        self.point = None
        self.sel_rect = None
        self.read_csv()
        self.show()

    def read_csv(self):
        self.alist = list()
        with open('myfile.csv', 'r') as csvfile:
            spam_reader = csv.reader(csvfile, delimiter=';')
            for row in spam_reader:
                self.alist.append(row)
            
    def drawBackground(self, painter, rect):
        scene_rect = self.sceneRect().toRect()
        painter.drawRect(scene_rect)

    def wheelEvent(self, event):
        factor = 1.41 ** (+event.angleDelta().y() / 240.0)
        self.scale(factor, factor)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.point = self.mapToScene(event.pos())

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            try:
                self.scene().removeItem(self.sel_rect)
                self.sel_rect = None
            except RuntimeError:
                pass
            rect = QRectF(self.point, self.mapToScene(event.pos()))
            self.fitInView(rect, Qt.KeepAspectRatio)

    def mouseMoveEvent(self, event):
        try:
            self.scene().removeItem(self.sel_rect)
            self.sel_rect = None
        except RuntimeError:
            pass
        rect = QRectF(self.point, self.mapToScene(event.pos()))
        pen = QPen(Qt.red, 1, Qt.DashDotLine)
        self.sel_rect = self.scene().addRect(rect, pen)

    def draw_points(self):
        green_pen = QPen(Qt.darkGreen)
        gray_pen = QPen(Qt.red)
        gray_pen.setStyle(Qt.DashLine)
        off_onn = 0
        old_point = QPointF(0.0, 0.0)
        scene = self.scene()
        scene.clear()
        for row in self.alist:
            cur_point = QPointF(float(row[1]) / 10, -float(row[2]) / 10)
            if off_onn == 1:
                scene.addLine(QLineF(old_point, cur_point), green_pen)
            else:
                scene.addLine(QLineF(old_point, cur_point), gray_pen)
            old_point = cur_point
            off_onn = int(row[5])
            self.update()
            QApplication.processEvents()
            time.sleep(0.005)
