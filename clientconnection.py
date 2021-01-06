import socket

import connection


class ClientConnection(connection.Connection):
    def __init__(self, ip_address, port):
        self.ip_address = ip_address
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def open(self):
        self.socket.connect((self.ip_address, self.port))

    def close(self):
        self.socket.close()

