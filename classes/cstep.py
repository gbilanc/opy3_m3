# encoding: utf-8


class CSTEP(object):
    riga = 0

    def __init__(self, *args):
        self.riga = CSTEP.riga  # numero di riga
        self.point = args[0]  # coordinate X,Y
        self.degree = args[1]  # angolazione assoluta su asse X
        self.passo = args[2]  # velocità interpolazione/rotazione
        self.off_onn = args[3]  # stato utensile (off=0, onn=1)
        CSTEP.riga += 1

    def __str__(self):
        return "%06d, point=[%s], degree=%.02f, passo=%.02f,off_onn=%d" % (
            self.riga,
            self.point,
            self.degree,
            self.passo,
            self.off_onn,
        )

    def serialize(self):
        return [
            "%06d" % self.riga,
            "%.06f" % (self.point[0] * 1000),
            "%.06f" % (self.point[1] * 1000),
            "%.02f" % self.degree,
            "%.02f" % self.passo,
            "%d" % self.off_onn,
        ]

    def clone(self):
        return CSTEP(self.point, self.degree, self.passo, self.off_onn)
