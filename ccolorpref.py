# encoding: utf-8
from base64 import b64decode
from base64 import b64encode
from json import JSONEncoder
from json import dumps
from json import loads
from os import getcwd
from os import path

FILENAME = "%s/pickle/ColorPref.json" % getcwd()


class ColorPrefEncoder(JSONEncoder):

    def default(self, obj):
        if isinstance(obj, CColorPref):
            return obj.__dict__
        return JSONEncoder.default(self, obj)


class CColorPref(object):
    """
    Oggetto utilizzato nella fase di generazione dei segmenti dal file dxf;
    ogni segmento viene contrassegnato con
    colore: serve per raggruppare i segmenti in fase di ordinamento,
    segmenti dello stesso colore vengono generati in sequenza
    passo: indica la velocità di esecuzione del segmento in percentuale
    rispetto alla velocità massima consentita dal controller
    ordine: indica la priorità di esecuzione del segmento, più basso è
    il valore prima viene inserito nella sequenza
    genera: indica se il segmento deve essere eseguito o meno,
    il segmento viene generato solo se genera == 1
    """

    def __init__(self, colore=0, passo=0, ordine=0, genera=1):
        """
        Param colore, gruppo di appartenenza del segmento
        param passo, velocità di esecuzione
        param ordine, priorità di esecuzione
        param genera, includi nell'esecuzione
        """
        self.colore = colore
        self.passo = passo
        self.ordine = ordine
        self.genera = genera

    def __str__(self):
        mask = "colore=%d, passo=%f, ordine=%d, genera=%d"
        return mask % (self.colore, self.passo / 100, self.ordine, self.genera)

    @staticmethod
    def serialize(values):
        json_data = dumps(values, cls=ColorPrefEncoder)
        with open(FILENAME, 'wb') as outfile:
            data_bytes = json_data.encode("utf-8")
            outfile.write(b64encode(data_bytes))

    @staticmethod
    def deserialize():
        result = list()
        if path.isfile(FILENAME):
            with open(FILENAME, 'r') as infile:
                decoded = b64decode(infile.read())
                json_data = loads(decoded)
                for item in json_data:
                    result.append(CColorPref(
                        item[u'colore'],
                        item[u'passo'],
                        item[u'ordine'],
                        item[u'genera']
                    ))
        for idx in range(len(result) + 1, 255):
            result.append(CColorPref(idx, 20, idx, 1))
        return result
