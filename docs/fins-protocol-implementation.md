# Implementazione protocollo FINS Omron

## Configurazione di base

File: `MainWindow.py:36-41`

```python
fins_instance = UDPFinsConnection()
fins_instance.connect(settings.plcUrl, settings.plcPort)
fins_instance.icf = '\x80'  # command + response_required
fins_instance.da1 = '\x15'  # NJ 192.168.0.21  = hex(21)
fins_instance.sa1 = '\x6E'  # PC 192.168.0.110 = hex(110)
fins_instance.mac = '\xB2'  # Memory Area Code (HOLDING_RELAY)
```

| Parametro | Valore | Descrizione |
|-----------|--------|-------------|
| Trasporto | UDP | porta `9600` |
| ICF | `0x80` | Command + response required |
| DA1 | `0x15` | Destinazione NJ (node 21 = 192.168.0.21) |
| SA1 | `0x6E` | Sorgente PC (node 110 = 192.168.0.110) |
| MAC | `0xB2` | Holding Relay Area (HR) |

## Struttura della libreria

```
fins/
├── __init__.py    # Core: enum MRC/SRC/MAC, classe base FinsConnection
├── tcp.py         # TCPFinsConnection (non usato)
├── udp.py         # UDPFinsConnection (usato in produzione)
└── usb.py         # USBFinsConnection (non usato)
```

## Memory Area Code (MAC) supportati

| MAC | Area |
|-----|------|
| `0xB0` | CIO (I/O area) |
| `0xB1` | WR (Work area) |
| `0xB2` | **HR** (Holding Relay) — **usato in produzione** |
| `0xB3` | AR (Auxiliary Relay) |

## Codici comando FINS (MRC/SRC)

| MRC | SRC | Nome | Descrizione |
|-----|-----|------|-------------|
| `0x01` | `0x01` | `MEMORY AREA READ` | Lettura area memoria |
| `0x01` | `0x02` | `MEMORY AREA WRITE` | Scrittura area memoria |
| `0x01` | `0x02` | `HOST BIT WRITE` | Scrittura bit (commentato, non usato) |

## Formato del frame FINS

```
ICF(1) + RSV(1) + GCT(1) + DNA(1) + DA1(1) + DA2(1) +
SNA(1) + SA1(1) + SA2(1) + SID(1) +
MRC(1) + SRC(1) + MAC(1) + MFA(2) + SFA(1) + NUM(2) +
UDATA(n)
```

| Campo | Byte | Descrizione |
|-------|------|-------------|
| ICF | 1 | Information Control Field (`0x80`) |
| RSV | 1 | Reserved (`0x00`) |
| GCT | 1 | Gateway count (`0x02`) |
| DNA | 1 | Destination Network Address (`0x00`) |
| DA1 | 1 | Destination Node Address |
| DA2 | 1 | Destination Unit Address (`0x00`) |
| SNA | 1 | Source Network Address (`0x00`) |
| SA1 | 1 | Source Node Address |
| SA2 | 1 | Source Unit Address (`0x00`) |
| SID | 1 | Service ID (identificativo richiesta) |
| MRC | 1 | Main Request Code |
| SRC | 1 | Sub Request Code |
| MAC | 1 | Memory Area Code |
| MFA | 2 | Main Final Address (indirizzo word) — big-endian |
| SFA | 1 | Sub Final Address (bit offset, solito `0x00`) |
| NUM | 2 | Numero elementi — big-endian |
| UDATA | n | Dati (solo per scrittura) |

---

## Operazioni di Lettura

Definite in `statics.py:67-76` (`NjRead`) e chiamate in `MainWindow.py:354-361`.

Parametri: `(SID, MFA, NUM)` — rispettivamente Service ID, indirizzo word, numero word.

| Nome | SID | MFA | NUM | Descrizione |
|------|-----|------|-----|-------------|
| `Override` | 11 | 2 | 1 | Lettura override velocità |
| `VelJog` | 12 | 7 | 1 | Lettura velocità JOG |
| `Nj_Status` | 15 | 50 | 2 | Stato NJ (bitmap 32 bit) |
| `OverrideRunPoint` | 19 | 55 | 1 | Override run point |
| `RunningPoint_ML` | 20 | 59 | 1 | Punto corrente nel file traiettoria |
| `Axis0_Status` | 21 | 60 | 20 | Stato asse X (20 word) |
| `Axis1_Status` | 22 | 100 | 20 | Stato asse Y (20 word) |
| `Axis2_Status` | 23 | 140 | 20 | Stato asse C/rotazione (20 word) |

Le letture sono eseguite ciclicamente ogni **250 ms** via QTimer (`MainWindow.py:460-468`).

### Interpretazione risposte

In `MainWindow.py:372-388` (`_handle_response`), ogni risposta è smistata in base al SID:

- `Override` → `set_override1()` (widget velocità)
- `VelJog` → `set_override2()` (widget JOG)
- `Nj_Status` → `show_status()` (decodifica bitmap stato NJ)
- `RunningPoint_ML` → `show_current_row()` (aggiorna riga corrente file)
- `Axis0/1/2_Status` → `show_status()` sull'asse corrispondente (posizione, velocity, ecc.)

### Stato NJ (`Nj_Status`) — bitmap a 16 bit

Definito in `statics.py:31-54` (`StatusBit`):

| Bit | Nome | Descrizione |
|-----|------|-------------|
| 0 | `HomingInCorso` | Homing in corso |
| 1 | `HomingEseguito` | Homing eseguito |
| 2 | `ErroreECT` | Errore ECT |
| 3 | `ErroreMC` | Errore MC |
| 4 | `ErrorePLC` | Errore PLC |
| 5 | `NJ_Active` | NJ attivo |
| 6 | `ML_StartPath` | MotionList start path |
| 7 | `ML_Done` | MotionList completato |
| 8 | `FR_Done` | File read completato |
| 9 | `FR_Busy` | File read in corso |
| 10 | `FR_Error` | File read errore |
| 11 | `FR_EndReadFileData` | File read fine dati |
| 12 | `NJ_Automatico` | Modo automatico |
| 13 | `NJ_Manuale` | Modo manuale |
| 14 | `NJ_Hold` | Hold attivo |
| 15 | `NJ_Emergenza` | Emergenza attiva |
| 16 | `NJ_Homing` | Homing richiesto |
| 17 | `ValvRULLO` | Valvola rullo |
| 18 | `ValvPENNA` | Valvola penna |
| 19 | `ValvLAMA` | Valvola lama |
| 20 | `RichHomeCambioTool` | Richiesta homing cambio tool |
| 21 | `NJ_Ready` | NJ pronto |
| 22 | `NJ_Error` | NJ in errore |

---

## Operazioni di Scrittura

Definite in `statics.py:57-65` (`NjWrite`) e chiamate in `ui/njstatus.py:385-434`.

Parametri: `(SID, MFA, NUM)` più `_data` (dati impacchettati con `struct.pack`).

| Nome | SID | MFA | NUM | Dati (pack) | Descrizione |
|------|-----|------|-----|-------------|-------------|
| `Buttons` | 1 | 0 | 1 | `pack('>H', bitmap_9bit)` | Scrive i 9 bit pulsanti come word a 16 bit |
| `Override` | 2 | 2 | 1 | `pack('>H', value)` | Override velocità (unsigned 16-bit) |
| `OffsetLama` | 3 | 3 | 1 | `pack('>h', value)` | Offset lama (signed 16-bit) |
| `OffsetLamaFloat` | 3 | 3 | 4 | `pack('>f', float_value)` | Offset lama come float32 IEEE 754 (occupa 4 word) |
| `NumeroPunti` | 6 | 6 | 1 | `pack('>H', value)` | Numero punti traiettoria |
| `VelJog` | 7 | 7 | 1 | `pack('>H', value)` | Velocità JOG |
| `TipoUtensile` | 8 | 8 | 1 | `pack('>H', value)` | Tipo utensile |

### Pulsanti (Button) — bitmap 9 bit

Definito in `statics.py:19-28` (`ButtonBit`):

| Bit | Nome | Descrizione |
|-----|------|-------------|
| 0 | `Automatic` | Modo automatico |
| 1 | `Start` | Avvio ciclo |
| 2 | `Manual` | Modo manuale |
| 3 | `Homing` | Homing |
| 4 | `Reset` | Reset allarmi |
| 5 | `Hold` | Hold/pausa |
| 6 | `EntTranFile` | Invia file traiettoria |
| 7 | `Notify` | Notifica |
| 8 | `TransMode` | Modalità trasferimento |

I 9 bit sono assemblati in una word a 16 bit (`pack('>H', bitmap)`) invertendo l'ordine della lista: `_write_button_state()` in `njstatus.py:431-434`.

### Tipi utensile

Definito in `statics.py:78-81` (`Tools`):

| ID | Utensile |
|----|----------|
| 0 | Rullo |
| 1 | Penna |
| 2 | Cutter |

---

## Connessione UDP e risposta

In `fins/udp.py:42-55` (`execute_fins_command_frame`):

1. Invia frame FINS via UDP a `ip:9600`
2. Riceve risposta (timeout 10s)
3. Valida con `check_resp()`:
   - Lunghezza ≥ 14 byte
   - Coerenza DA1/DA2/SA2 tra richiesta e risposta
   - Coerenza SID tra richiesta e risposta
   - MRC/SRC (`response[12]`, `response[13]`):
     - `0x00 0x00` → completamento normale
     - `0x00 0x01` → servizio cancellato
     - altro → codice errore
4. Se OK → ritorna `(SID, response[14:])` (dati letti)
5. Se errore → ritorna `(b'\xff', messaggio_errore)`

## Codice FINS commentato (non attivo)

In `fins/__init__.py:78-86` è presente `host_bit_write()` commentato:

```python
# def host_bit_write(self, _bit=0, stat=0):
#     self.mrc = MRC.MEM
#     self.src = SRC.WRITE
#     self.sid = pack('>B', 0)
#     self.mfa = pack('>H', 0)
#     self.sfa = pack('>B', _bit)    # bit offset
#     self.num = pack('>H', 0)
#     self.udata = pack('>B', stat)  # \x00=off, \x01=on
```

Operazione di scrittura bit singolo: usa `SFA` per specificare il bit e scrive 1 byte (`0x00`=off, `0x01`=on). Attualmente non utilizzata.
