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

    def execute_fins_command_frame(self, command):
        print ("sending: " + command)
        response = ''
        self.fins_socket.sendto(command, (self.ip_address, 9600))
        try:
            response = self.fins_socket.recv(self.BUFFER_SIZE)
        except Exception as err:
            print(err)
        return response

    def connect(self, address, port=9600):
        self.fins_port = port
        self.ip_address = address
        self.fins_socket.connect((address, port))
        self.fins_socket.settimeout(1.0)

    def __del__(self):
        self.fins_socket.close()
