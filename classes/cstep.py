class CSTEP:
    riga = 0
    point: list
    degree: float
    passo: float
    off_onn: int

    def __init__(self, point: list, degree: float, passo: float, off_onn: int):
        self.riga = CSTEP.riga
        self.point = point
        self.degree = degree
        self.passo = passo
        self.off_onn = off_onn
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
