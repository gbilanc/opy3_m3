from enum import Enum
from struct import pack


class MRC(Enum):
    ZERO = '\x00'
    MEM = '\x01'
    PAR = '\x02'


class SRC(Enum):
    ZERO = '\x00'
    READ = '\x01'
    WRITE = '\x02'
    FILL = '\x03'
    MULTIREAD = '\x04'
    TRANSFER = '\x05'


class MAC(Enum):
    CIO = '\xB0'
    WR = '\xB1'
    HR = '\xB2'
    AR = '\xB3'


class FinsConnection:

    def __init__(self):
        self.icf = '\x80'  # ICF (Information Control Field)
        self.rsv = '\x00'  # RSV (Reserved by system)
        self.gct = '\x02'  # GCT (Permissible Number of Gateways)
        self.dna = '\x00'  # DNA (Destination Network Address)
        self.da1 = '\x00'  # DA1 (Destination Node Address)
        self.da2 = '\x00'  # DA2 (Destination Unit Address)
        self.sna = '\x00'  # SNA (Source Network Address)
        self.sa1 = '\x00'  # SA1 (Source Node Address)
        self.sa2 = '\x00'  # SA2 (Source Unit Address)
        self.sid = '\x00'  # SID (Service ID)
        self.mrc = MRC.ZERO.value  # MRC (Main Request Code)
        self.src = SRC.ZERO.value  # SRC (Sub Request Code)
        self.mac = MAC.HR.value  # MAC (Memory Area Code)
        self.mfa = '\x00\x00'  # MFA (Main Final Address)
        self.sfa = '\x00'  # SFA (Sub Final Address)
        self.num = '\x00\x00'  # numero elementi da leggere/scrivere
        self.udata = ''

    @property
    def fins(self):
        cmd_bytes = self.icf + self.rsv + self.gct + self.dna + self.da1 + self.da2 + \
                   self.sna + self.sa1 + self.sa2 + self.sid + self.mrc + self.src + \
                   self.mac + self.mfa + self.sfa + self.num + self.udata
        return cmd_bytes.encode("latin1")

    def execute_fins_command_frame(self, command):
        pass

    def memory_area_read(self, params):
        self.mrc = MRC.MEM.value
        self.src = SRC.READ.value
        self.sid = pack('>B', params[0]).decode('latin1')
        self.mfa = pack('>H', params[1]).decode('latin1')
        self.sfa = pack('>B', 0).decode('latin1')
        self.num = pack('>H', params[2]).decode('latin1')
        self.udata = ''
        return self.execute_fins_command_frame(self.fins)

    def memory_area_write(self, params, _data=''):
        self.mrc = MRC.MEM.value
        self.src = SRC.WRITE.value
        self.sid = pack('>B', params[0]).decode('latin1')
        self.mfa = pack('>H', params[1]).decode('latin1')
        self.sfa = pack('>B', 0).decode('latin1')
        self.num = pack('>H', params[2]).decode('latin1')
        self.udata = _data
        return self.execute_fins_command_frame(self.fins)

    # def host_bit_write(self, _bit=0, stat=0):
    #     self.mrc = MRC.MEM
    #     self.src = SRC.WRITE
    #     self.sid = pack('>B', 0)
    #     self.mfa = pack('>H', 0)
    #     self.sfa = pack('>B', _bit)
    #     self.num = pack('>H', 0)
    #     self.udata = pack('>B', stat)  # \x00=off \x01=onn
    #     return self.execute_fins_command_frame(self.fins)
