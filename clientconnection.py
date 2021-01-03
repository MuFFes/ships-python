import socket

import connection


class ClientConnection(connection.Connection):
    def __init__(self, ip_address, port):
        self.ip_address = ip_address
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.socket.connect((self.ip_address, self.port))


if __name__ == "__main__":
    connection = ClientConnection("192.168.0.14", 1233)
    connection.connect()
