# encoding: utf-8

HTML = u"<html><head/><body><h3>{0}</h3></body></html>"
HTMLRED = u"<html><head/><body><h3 style=""color:red;"">{0}</h3></body></html>"
HTMLGRE = u"<html><head/><body><h3 style=""color:green;"">{0}</h3></body></html>"

MES01 = HTML.format("<p style=""color:green"">omronpy.m2 ver. 2022.10</p>&#169; GiBiSoft 2015-2022")
MES02 = HTMLRED.format("Questa operazione comporta l'avvio dei motori!<br/>Confermi l'avvio?")
MES03 = HTMLGRE.format("Non è stato selezionato alcun layer da generare")
MES04 = HTMLGRE.format("Impossibile inviare il file Csv quando il controller è in modalità AUTO")
MES05 = HTMLGRE.format("Per procedere è necessario eseguire l'Homing")
MES06 = HTMLGRE.format("Il layer selezionato è vuoto!")
MES07 = HTMLRED.format("Il numero dei punti eccede il limite consentito!")
MES08 = HTMLGRE.format("Generazione file CSV termitata!")
MES09 = HTMLGRE.format("Resettare gli allarmi prima di avviare il ciclo automatico")
MES10 = HTMLRED.format("Il punto {0} non è presente nel disegno")
MES11 = HTMLRED.format("Il disegno contiene interruzioni non consentite!")
MES12 = HTMLRED.format("Il controller non è connesso<br/>all'indirizzo {0}")
MES13 = "acquisizione {0} in corso..."
MES14 = "generazione file CSV in corso..."
MES15 = "lettura file CSV in corso..."
MES16 = "lettura file CSV terminata!"

LABELGREEN = "QLabel{background-color: rgb(0, 255, 0);color: rgb(0, 32, 0);border-radius: 10px;}"
LABELRED = "QLabel{background-color: rgb(255, 0, 0);color: rgb(32, 0, 0);border-radius: 10px;}"
LABELGRAY = "QLabel{background-color: rgb(192, 192, 192);color: rgb(255, 255, 255);border-radius: 10px;}"
BUTTONORANGE = "QPushButton{background-color: rgb(255, 153, 0);}"
BUTTONGREEN = "QPushButton{background-color: rgb(0, 255, 0);}"
BUTTONRED = "QPushButton{background-color: rgb(255, 0, 0);}"
BUTTONGRAY = "QPushButton{background-color: rgb(200, 200, 200);}"
