import socket

from Connection import connection


class ServerConnection(connection.Connection):
    def __init__(self, port):
        self.__port = port
        self.__serversocket = None
        self._socket = None
        self.__ip_address = None

    def open(self):
        self.__serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__serversocket.bind(("", self.__port))
        self.__serversocket.listen(1)
        (self._socket, self.__ip_address) = self.__serversocket.accept()

    def close(self):
        self._socket.close()
        self.__serversocket.close()
