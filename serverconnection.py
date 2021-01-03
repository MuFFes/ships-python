import socket

import connection


class ServerConnection(connection.Connection):
    def __init__(self, port):
        self.port = port
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket = None
        self.ip_address = None

    def open(self):
        self.serversocket.bind(("", self.port))
        self.serversocket.listen(1)
        print("listenning")
        (self.socket, self.ip_address) = self.serversocket.accept()
