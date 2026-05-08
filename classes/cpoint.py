# encoding: utf-8


class CPOINT:
    point: list
    passo1: float
    stato1: int
    degree1: float
    passo2: float
    stato2: int
    degree2: float
    length: float

    def __init__(self, point: list, passo: float, stato: int, degree: float):
        self.point = point
        self.passo1 = passo
        self.stato1 = stato
        self.degree1 = degree
        self.passo2 = passo
        self.stato2 = stato
        self.degree2 = degree
        self.length = 0.0

    def __repr__(self):
        return "[ {0:.4f}:{1:.4f} ]".format(self.point[0], self.point[1])

    @property
    def degree_rel(self):
        """
        Calcola la differenza angolare relativa tra l'arrivo e la ripartenza.

        La funzione normalizza la differenza per restituire l'angolo più breve
        nel range [-180, 180] gradi.

        Returns:
            float: Delta angolare relativo.
        """
        diff = self.degree2 - self.degree1
        if diff == 0:
            return diff
        elif diff > 0:
            return diff if diff < 180.0 else diff - 360
        else:
            return diff if diff > -180 else diff + 360

    def serialize(self):
        """
        Converte l'oggetto in una lista di stringhe formattate per la scrittura su CSV.

        Returns:
            list[str]: Rappresentazione testuale dei parametri del punto.
        """
        return [
            "%.09f" % self.point[0],
            "%.09f" % self.point[1],
            "%.02f" % self.passo1,
            "%.02f" % self.passo2,
            "%d" % self.stato1,
            "%d" % self.stato2,
            "%.02f" % self.degree1,
            "%.02f" % self.degree2,
            "%.02f" % self.degree_rel,
            "%.05f" % self.length,
        ]

    @staticmethod
    def deserialize(data):
        """
        Crea un'istanza di CPOINT a partire da una riga di dati (lista di stringhe).

        Args:
            data (list[str]): Riga di dati proveniente da un file CSV.
                              Si assume che l'ordine dei campi sia quello definito in serialize().

        Returns:
            CPOINT: Oggetto punto ricostruito dai dati.
        """
        point = CPOINT(
            [float(data[0]), float(data[1])],
            float(data[2]),
            int(data[4]),
            float(data[6]),
        )
        point.passo2 = float(data[3])
        point.stato2 = int(data[5])
        point.degree2 = float(data[7])
        point.length = float(data[9])
        return point
