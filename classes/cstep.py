class CSTEP(object):
    """
    Rappresenta un singolo comando di movimento (step) per il PLC.

    A differenza di CPOINT, CSTEP è l'unità atomica che viene scritta nel file
    di output. Ogni istanza rappresenta un'azione specifica: spostamento a una
    coordinata, rotazione dell'asse C o cambio di stato dell'utensile.

    Attributes:
        riga (int): Numero di sequenza dello step (gestito globalmente dalla classe).
        point (list[float]): Coordinate [X, Y] di destinazione.
        degree (float): Angolazione assoluta rispetto all'asse X.
        passo (float): Velocità di interpolazione o di rotazione.
        off_onn (int): Stato finale dell'utensile (0 = sollevato, 1 = abbassato).
    """

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
        """
        Converte l'oggetto in una lista di stringhe formattate per il PLC.

        Le coordinate X e Y vengono moltiplicate per 1000 per convertire le
        unità in micron (o l'unità richiesta dal PLC) prima della scrittura.

        Returns:
            list[str]: Rappresentazione testuale dello step con formattazione a zero per la riga.
        """
        return [
            "%06d" % self.riga,
            "%.06f" % (self.point[0] * 1000),
            "%.06f" % (self.point[1] * 1000),
            "%.02f" % self.degree,
            "%.02f" % self.passo,
            "%d" % self.off_onn,
        ]

    def clone(self):
        """
        Crea una copia dell'oggetto CSTEP.

        Nota: La creazione di un clone incrementerà il valore globale di CSTEP.riga,
        assegnando al clone un numero di riga successivo a quello dell'originale.

        Returns:
            CSTEP: Nuova istanza con gli stessi parametri di movimento.
        """
        return CSTEP(self.point, self.degree, self.passo, self.off_onn)
