import socket

import connection


class ServerConnection(connection.Connection):
    def __init__(self, port):
        self.port = port
        self.serversocket = None
        self.socket = None
        self.ip_address = None

    def open(self):
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serversocket.bind(("", self.port))
        self.serversocket.listen(1)
        print("listenning")
        (self.socket, self.ip_address) = self.serversocket.accept()

    def close(self):
        self.socket.close()
        self.serversocket.close()
