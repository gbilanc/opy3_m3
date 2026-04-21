# omronpy-m2

Applicazione di controllo per macchina plotter (2 assi + utensile) con comunicazione verso PLC Omron NJ tramite protocollo FINS/UDP.

## Funzionalità

- Importazione percorsi di lavorazione da file **DXF**
- Comunicazione con PLC **Omron NJ** via **FINS over UDP** (porta 9600)
- Monitoraggio in tempo reale di stato PLC e stato assi (X, Y, C)
- Supporto a tre utensili: **Rullo**, **Penna**, **Cutter (lama)**
- Anteprima grafica del percorso prima dell'invio
- Configurazione parametri macchina tramite dialog impostazioni
- Persistenza configurazione su file `settings.ini`

## Requisiti

- Python ≥ 3.13
- PySide6
- [ezdxf](https://ezdxf.readthedocs.io/) ≥ 1.4.3
- usb ≥ 0.0.83.dev0

## Installazione

```bash
pip install -r requirements.txt
```

oppure con [uv](https://github.com/astral-sh/uv):

```bash
uv sync
```

## Avvio

```bash
python -m opy3_m3
```

oppure direttamente:

```bash
python __main__.py
```

## Configurazione

Le impostazioni vengono salvate in `settings.ini`. I parametri principali:

| Chiave | Default | Descrizione |
|---|---|---|
| `plcUrl` | `192.168.0.21` | Indirizzo IP del PLC |
| `plcPort` | `9600` | Porta FINS UDP |
| `scale_unit` | `100.0` | Fattore di scala unità |
| `offset_lama` | `-123` | Offset cutter (lama) |
| `speed_rullo` | `0.10` | Velocità rullo |
| `max_size` | `1500 × 600` | Dimensione massima area di lavoro (mm) |

## Struttura del progetto

```
opy3_m3/
├── __main__.py          # Entry point
├── MainWindow.py        # Finestra principale
├── DialogPreview.py     # Anteprima percorso DXF
├── DialogSettings.py    # Dialog impostazioni macchina
├── statics.py           # Enum, costanti e funzioni di utilità
├── csettings.py         # Gestione settings.ini
├── ccolorpref.py        # Preferenze colore layer DXF
├── cmemopref.py         # Helper memorizzazione preferenze
├── classes/             # Modelli dati (punti, polilinee, layer, workspace)
├── fins/                # Implementazione protocollo FINS (UDP, TCP, USB)
├── ui/                  # Form Qt generati da Qt Designer
└── resources.py         # Risorse embedded (icone, ecc.)
```

## Licenza

Vedere [LICENSE](LICENSE).

