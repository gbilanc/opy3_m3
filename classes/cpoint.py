# encoding: utf-8


class CPOINT(object):

    def __init__(self, *args):
        self.point = args[0]  # coordinate X, Y del punto
        self.passo1 = args[1]  # velocità interpolazione all'arrivo
        self.stato1 = args[2]  # position strumento all'arrivo
        self.degree1 = args[3]  # angolazione strumento all'arrivo
        self.passo2 = args[1]  # velocità interpolazione alla ripartenza
        self.stato2 = args[2]  # position strumento alla ripartenza
        self.degree2 = args[3]  # angolazione strumento alla ripartenza
        self.length = 0.0

    def __repr__(self):
        return "[ {0:.4f}:{1:.4f} ]".format(self.point[0], self.point[1])

    @property
    def degree_rel(self):
        diff = self.degree2 - self.degree1
        if diff == 0:
            return diff
        elif diff > 0:
            return diff if diff < 180.0 else diff - 360
        else:
            return diff if diff > -180 else diff + 360

    def serialize(self):
        return [
            "%.09f" % self.point[0], "%.09f" % self.point[1],
            "%.02f" % self.passo1, "%.02f" % self.passo2,
            "%d" % self.stato1, "%d" % self.stato2,
            "%.02f" % self.degree1, "%.02f" % self.degree2,
            "%.02f" % self.degree_rel, "%.05f" % self.length]

    @staticmethod
    def deserialize(data):
        point = CPOINT([float(data[0]), float(data[1])],
                       float(data[2]), int(data[4]), float(data[6]))
        point.passo2 = float(data[3])
        point.stato2 = int(data[5])
        point.degree2 = float(data[7])
        point.length = float(data[9])
        return point
