# encoding: utf-8

from math import cos
from math import sin

from PySide6.QtCore import QPointF
from PySide6.QtCore import QRectF
from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush
from PySide6.QtGui import QPainterPath
from PySide6.QtGui import QPen
from ezdxf.enums import ACI

from statics import equals
from statics import get_qt_color
from statics import settings
from statics import vector_length


def oriented_polyline(points):
    max_distance = 0.0
    index = 0
    for i in range(len(points)):
        distance = vector_length([0, 0], points[i])
        if distance > max_distance:
            max_distance = distance
            index = i
    return points[index:] + points[:index + 1]


class CPoliline(object):

    def __init__(self, entity, layer):
        self.color = layer.color if entity.dxf.color == ACI.BYLAYER else entity.dxf.color
        if entity.dxftype() == "LINE":
            self.points = [entity.dxf.start, entity.dxf.end]
        if entity.dxftype() == "POLYLINE":
            self.points = [p for p in entity.points()]
            if entity.is_closed and not equals(self.points[0], self.points[-1]):
                self.points.append(self.points[0])

    @property
    def start(self):
        return self.points[0]

    @property
    def end(self):
        return self.points[-1]

    @property
    def is_closed(self):
        return equals(self.points[0], self.points[-1])

    @property
    def points_count(self):
        return len(self.remove_duplicates()) - 1

    def remove_duplicates(self):
        result = list()
        return [result.append(p) for p in self.points if p not in result]

    def draw(self, qt_scene):
        pts = [QPointF(pt[0] * settings.scale_unit,
                       -pt[1] * settings.scale_unit) for pt in list(self.points)]
        path = QPainterPath()
        path.moveTo(pts[0])
        for i in range(1, len(pts)):
            path.lineTo(pts[i])
        pen = QPen(get_qt_color(self.color), 0.5, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
        qt_scene.addPath(path, pen)

    def draw_progressivo(self, qt_scene, counter, font):
        pen = QPen(Qt.black, 0.25, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
        brush = QBrush(Qt.red)
        # pt = self.center_point()
        pt = self.points[0]
        if counter == 0:  # # evidenzia punto iniziale
            rect = QRectF(
                pt[0] * settings.scale_unit - 1.0,
                -pt[1] * settings.scale_unit - 1.0, 2.0, 2.0)
            qt_scene.addEllipse(rect, pen, brush)
        else:
            rect = QRectF(
                pt[0] * settings.scale_unit - 0.5,
                -pt[1] * settings.scale_unit - 0.5, 1.0, 1.0)
            qt_scene.addEllipse(rect, pen, brush)
        qt_scene.addSimpleText(str(counter), font).setPos(rect.x() + 1, rect.y() - 1)

    def scale(self, fact):
        self.points = [[pt[0] * fact, pt[1] * fact] for pt in self.points]

    def translate(self, off_x, off_y):
        self.points = [[pt[0] + off_x, pt[1] + off_y] for pt in self.points]

    def rotate(self, radians, center):
        points = []
        for point in self.points:
            pt = point[0] - center[0], point[1] - center[1]
            pt = (pt[0] * cos(radians) - pt[1] * sin(radians),
                  pt[0] * sin(radians) + pt[1] * cos(radians))
            points.append([pt[0] + center[0], pt[1] + center[1]])
        self.points = points

    def flip(self, mode, center):
        if mode == 0:
            self.points = [[center[0] * 2 - pt[0], pt[1]] for pt in self.points]
        else:
            self.points = [[pt[0], center[1] * 2 - pt[1]] for pt in self.points]

    def reverse(self):
        self.points.reverse()

    def center_point(self):
        pt_min = (min([pt[0] for pt in self.points]),
                  min([pt[1] for pt in self.points]))
        pt_max = (max([pt[0] for pt in self.points]),
                  max([pt[1] for pt in self.points]))
        return [(pt_max[0] + pt_min[0]) / 2, (pt_max[1] + pt_min[1]) / 2, ]
