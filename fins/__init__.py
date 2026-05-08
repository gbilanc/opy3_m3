from enum import Enum
from struct import pack


class MRC(Enum):
    ZERO = b'\x00'
    MEM = b'\x01'
    PAR = b'\x02'


class SRC(Enum):
    ZERO = b'\x00'
    READ = b'\x01'
    WRITE = b'\x02'
    FILL = b'\x03'
    MULTIREAD = b'\x04'
    TRANSFER = b'\x05'


class MAC(Enum):
    CIO = b'\xB0'
    WR = b'\xB1'
    HR = b'\xB2'
    AR = b'\xB3'


class FinsConnection:

    def __init__(self):
        self.icf: bytes = b'\x80'
        self.rsv: bytes = b'\x00'
        self.gct: bytes = b'\x02'
        self.dna: bytes = b'\x00'
        self.da1: bytes = b'\x00'
        self.da2: bytes = b'\x00'
        self.sna: bytes = b'\x00'
        self.sa1: bytes = b'\x00'
        self.sa2: bytes = b'\x00'
        self.sid: bytes = b'\x00'
        self.mrc: bytes = MRC.ZERO.value
        self.src: bytes = SRC.ZERO.value
        self.mac: bytes = MAC.HR.value
        self.mfa: bytes = b'\x00\x00'
        self.sfa: bytes = b'\x00'
        self.num: bytes = b'\x00\x00'
        self.udata: bytes = b''

    @property
    def fins(self) -> bytes:
        return (self.icf + self.rsv + self.gct + self.dna + self.da1 + self.da2 +
                self.sna + self.sa1 + self.sa2 + self.sid + self.mrc + self.src +
                self.mac + self.mfa + self.sfa + self.num + self.udata)

    def execute_fins_command_frame(self, command: bytes) -> tuple:
        raise NotImplementedError

    def memory_area_read(self, params: tuple) -> tuple:
        self.mrc = MRC.MEM.value
        self.src = SRC.READ.value
        self.sid = pack('>B', params[0])
        self.mfa = pack('>H', params[1])
        self.sfa = pack('>B', 0)
        self.num = pack('>H', params[2])
        self.udata = b''
        return self.execute_fins_command_frame(self.fins)

    def memory_area_write(self, params: tuple, _data: bytes = b'') -> tuple:
        self.mrc = MRC.MEM.value
        self.src = SRC.WRITE.value
        self.sid = pack('>B', params[0])
        self.mfa = pack('>H', params[1])
        self.sfa = pack('>B', 0)
        self.num = pack('>H', params[2])
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
