"# encoding: utf-8


class CPOINT(object):
    """
    Rappresenta un punto di percorso in un file di definizione plotter.

    Questa classe funge da modello dati per i punti importati dai file CSV/DXF.
    Ogni istanza contiene non solo le coordinate spaziali, ma anche i parametri
    di stato (velocità, posizione strumento e angolazione) sia per l'arrivo 
    al punto che per la ripartenza verso il punto successivo.

    Attributes:
        point (list[float]): Coordinate [X, Y] del punto.
        passo1 (float): Velocità di interpolazione all'arrivo al punto.
        stato1 (int): Stato dell'utensile all'arrivo (es. 0=OFF, 1=ONN).
        degree1 (float): Angolazione dello strumento all'arrivo.
        passo2 (float): Velocità di interpolazione alla ripartenza dal punto.
        stato2 (int): Stato dell'utensile alla ripartenza.
        degree2 (float): Angolazione dello strumento alla ripartenza.
        length (float): Lunghezza del segmento che porta a questo punto.
    """

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
            "%.09f" % self.point[0], "%.09f" % self.point[1],
            "%.02f" % self.passo1, "%.02f" % self.passo2,
            "%d" % self.stato1, "%d" % self.stato2,
            "%.02f" % self.degree1, "%.02f" % self.degree2,
            "%.02f" % self.degree_rel, "%.05f" % self.length]

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
        point = CPOINT([float(data[0]), float(data[1])],
                       float(data[2]), int(data[4]), float(data[6]))
        point.passo2 = float(data[3])
        point.stato2 = int(data[5])
        point.degree2 = float(data[7])
        point.length = float(data[9])
        return point
