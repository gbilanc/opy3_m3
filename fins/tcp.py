import socket

from fins import FinsConnection
from statics import settings


class TCPFinsConnection(FinsConnection):

    def __init__(self):
        FinsConnection.__init__(self)
        self.BUFFER_SIZE = 4096
        self.fins_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip_address = settings.plcUrl
        self.fins_port = settings.plcPort
        self._connected = False

    def execute_fins_command_frame(self, command: bytes) -> tuple:
        if not self._connected:
            return b'\xff', "Non connesso"
        print("sending: " + str(command))
        response = b''
        try:
            self.fins_socket.sendall(command)
            response = self.fins_socket.recv(self.BUFFER_SIZE)
        except Exception as err:
            print(err)
            return b'\xff', str(err)
        return response[9], response[14:]

    def connect(self, address: str, port: int = 9600) -> None:
        self.fins_port = port
        self.ip_address = address
        self.fins_socket.connect((address, port))
        self.fins_socket.settimeout(1.0)
        self._connected = True

    def disconnect(self) -> None:
        self._connected = False
        try:
            self.fins_socket.close()
        except Exception:
            pass

    def __del__(self):
        self.disconnect()
