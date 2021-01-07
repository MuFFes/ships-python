import socket

from Connection import connection


class ClientConnection(connection.Connection):
    def __init__(self, ip_address, port):
        self.__ip_address = ip_address
        self.__port = port
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def open(self):
        self._socket.connect((self.__ip_address, self.__port))

    def close(self):
        self._socket.close()

