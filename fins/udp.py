import socket

from fins import FinsConnection
from statics import settings

MS01 = "Normal completion"
MS02 = "Service cancelled"
ER01 = "Lunghezza FINS errata!"
ER02 = "IP di provenienza errato!"
ER03 = "ID del servizio errato!"
ER04 = "Errore {0} {1}!"


def check_resp(command, response):
    if len(response) < 14:
        return 1, ER01
    if not (response[6] == command[3] and response[7] == command[4] and response[8] == command[5]):
        return 2, ER02
    if not response[9] == command[9]:
        return 3, ER03
    if response[12] == 0:
        if response[13] == 0:
            return 0, MS01
        elif response[13] == 1:
            return 4, MS02
        else:
            return 0, ER04.format(response[12], str(response[13]))
    else:
        return 6, ER04.format(response[12], str(response[13]))


class UDPFinsConnection(FinsConnection):

    def __init__(self):
        FinsConnection.__init__(self)
        self.BUFFER_SIZE = 4096
        self.fins_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.fins_socket.settimeout(10)
        self.ip_address = settings.plcUrl
        self.fins_port = None

    def execute_fins_command_frame(self, command):
        response = ''
        self.fins_socket.sendto(command, (self.ip_address, 9600))
        try:
            response = self.fins_socket.recv(self.BUFFER_SIZE)
        except Exception as err:
            print(err)
        # print(binascii.hexlify(command))
        # print(binascii.hexlify(response))
        check = check_resp(command, response)
        if check[0] == 0:
            return response[9], response[14:]
        else:
            return b'\xff', check[1]

    def connect(self, address, port=9600):
        self.fins_port = port
        self.ip_address = address
        self.fins_socket.bind(('', port))
        self.fins_socket.settimeout(3.0)

    def __del__(self):
        self.fins_socket.close()
