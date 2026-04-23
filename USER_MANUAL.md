# Manuale Utente - omronpy-m2

## 1. Introduzione
**omronpy-m2** è un'applicazione software progettata per il controllo di una macchina plotter a 2 assi (X, Y) dotata di un terzo asse per l'utensile (C). Il software permette di importare disegni in formato DXF, elaborare i percorsi di lavoro e inviarli a un PLC Omron NJ tramite il protocollo FINS/UDP.

## 2. Installazione e Avvio

### Requisiti
- Python ≥ 3.13
- PySide6, ezdxf, usb

### Avvio
1. Installare le dipendenze: `pip install -r requirements.txt`
2. Avviare l'applicazione: `python __main__.py`

## 3. Guida all'Interfaccia

### 3.1 Importazione e Visualizzazione
- **Apertura File**: Utilizzare il menu per acquisire un file `.dxf`. Il software caricherà automaticamente i layer presenti nel file.
- **Area di Visualizzazione**: Il disegno viene mostrato in una vista grafica. È possibile navigare tra i layer selezionandoli nella tabella dedicata.

### 3.2 Gestione dei Layer
Per ogni layer importato, è possibile configurare:
- **Visibilità**: Attivare/disattivare la visualizzazione del layer nel grafico.
- **Selezione**: Selezionare il layer che si desidera processare per l'invio al PLC.
- **Inversione**: Invertire la direzione del percorso di lavorazione.

### 3.3 Trasformazioni Geometriche
Sulla finestra principale è possibile applicare modifiche globali al workspace:
- **Traslazione**: Inserire valori in `X` e `Y` e cliccare su **Sposta** per spostare l'intero disegno.
- **Rotazione**: Ruotare il disegno di 90 gradi in senso antiorario.
- **Inversione Assi**: Specchiare il disegno rispetto all'asse X o Y.
- **Origine**: Caricare la posizione attuale della penna come offset.

### 3.4 Gestione Colori e Priorità
Quando un layer è selezionato, compare la tabella dei colori:
- **Ordine**: Definisce la sequenza di plottaggio dei segmenti in base al colore.
- **Passo**: Parametro di precisione per il segmento del colore specifico.
- **Genera**: Abilitare o disabilitare l'inclusione di quel colore nel file finale.
- **Ordina per colore**: Se attivato, il software organizzerà i movimenti raggruppando i segmenti dello stesso colore per ottimizzare i tempi di lavoro.

### 3.5 Selezione Utensile
È possibile scegliere tra tre diversi utensili:
- **Rullo**
- **Penna**
- **Laser** (Sostituisce il Cutter/Lama in alcune versioni)

La scelta dell'utensile influenza l'offset di posizione e i parametri di generazione del CSV.

## 4. Comunicazione con il PLC

### 4.1 Monitoraggio
L'applicazione comunica costantemente con il PLC Omron NJ:
- **Stato PLC**: Viene mostrato lo stato operativo del PLC e l'eventuale allarme.
- **Driver Assi**: In tempo reale vengono visualizzate le posizioni e lo stato dei driver X, Y e C.
- **Barra di Progresso**: Durante l'invio dei dati, una barra indica l'avanzamento della lettura/invio del CSV.

### 4.2 Invio Percorsi
1. Selezionare il layer desiderato.
2. Configurare l'ordine dei colori e l'utensile.
3. Cliccare su **Genera CSV**.
4. Se il PLC è in modalità manuale (o configurata per l'invio), l'applicazione invierà i comandi di movimento.

## 5. Impostazioni (Dialog Settings)
Dal menu Impostazioni è possibile configurare i parametri critici:
- **PLC URL/Port**: Indirizzo IP e porta del PLC (default 192.168.0.21:9600).
- **Scale Unit**: Fattore di scala per convertire le unità DXF in unità macchina.
- **Offset Lama**: Offset specifico per l'utensile cutter.
- **Velocità Rullo**: Impostazione della velocità di avanzamento per l'utensile rullo.
- **Area di Lavoro**: Definizione delle dimensioni massime (mm) per evitare collisioni.

## 6. Flusso di Lavoro Consigliato
1. **Aprire** il file DXF.
2. **Configurare** l'offset e l'orientamento del disegno tramite i pulsanti di traslazione/rotazione.
3. **Selezionare** l'utensile appropriato.
4. **Scegliere** il layer da lavorare e definire l'ordine di plottaggio dei colori.
5. **Verificare** l'anteprima tramite il comando **Simula Plotter**.
6. **Inviare** il lavoro al PLC tramite **Genera CSV**.
