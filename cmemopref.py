# encoding: utf-8

from base64 import b64decode
from base64 import b64encode
from json import JSONEncoder
from json import dumps
from json import loads
from os import getcwd
from os import path

from ccolorpref import CColorPref


class MemoEncoder(JSONEncoder):

    def default(self, obj):
        if isinstance(obj, MemoHelper):
            return obj.__dict__
        if isinstance(obj, CColorPref):
            return obj.__dict__
        return JSONEncoder.default(self, obj)


class MemoHelper:
    """
    Oggetto utilizzato per memorizzare le opzioni dell'utente durante la generazione
    del file csv relativo a un singolo layer del progetto
    selected: nome del layer cui si riferiscono le impostazioni salvate
    visible: indica se il layer è visibile o meno
    reverse: indica e la sequenza delle istruzioni deve avvenire in ordine inverso rispetto al normale
    tool_id: indica lo strumento da utilizzare per eseguire il lavoro
    start_point: punto da cui iniziare l'esecuzione del lavoro
    sort_colors: indica se la generazione dei punti deve avvenire in ordine di colore 
    pref_colors: lista delle opzioni dell'utente relative a ogni colore
    """

    def __init__(self):
        self.selected = None
        self.filename = None
        self.exists = False
        self.visible = True
        self.reverse = False
        self.tool_id = 1  # Penna
        self.start_point = 0
        self.offsetX = 0.0
        self.offsetY = 0.0
        self.sort_colors = False
        self.pref_colors = list()

    def set_filename(self, filename):
        self.pref_colors = CColorPref.deserialize()
        self.filename = "%s/pickle/%s" % (getcwd(), b64encode(filename.encode("utf-8")))
        self.exists = path.isfile(self.filename)
        if self.exists:
            self.deserialize()

    def deserialize(self):
        with open(self.filename, 'r') as infile:
            decoded = b64decode(infile.read())
            json_data = loads(decoded)
            self.selected = json_data.get(u'selected', None)
            self.visible = json_data.get(u'visible', True)
            self.reverse = json_data.get(u'reverse', False)
            self.tool_id = json_data.get(u'tool_id', 1)
            self.start_point = json_data.get(u'start_point', 0)
            self.offsetX = json_data.get(u'offsetX', 0.0)
            self.offsetY = json_data.get(u'offsetY', 0.0)
            self.sort_colors = json_data.get(u'sort_colors', False)
            for item in json_data[u'pref_colors']:
                color_pref = self.get_color_pref(item[u'colore'])
                color_pref.passo = item[u'passo']
                color_pref.ordine = item[u'ordine']
                color_pref.genera = item[u'genera']

    def serialize(self):
        json_data = dumps(self, cls=MemoEncoder)
        with open(self.filename, 'wb') as outfile:
            data_bytes = json_data.encode("utf-8")
            outfile.write(b64encode(data_bytes))

    def get_color_pref(self, color):
        for item in self.pref_colors:
            if item.colore == color:
                return item
        newone = CColorPref(color, 20, 99, 1)
        self.pref_colors.append(newone)
        return newone
