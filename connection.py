import abc
import struct


class Connection(abc.ABC):
    @abc.abstractmethod
    def open(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def close(self):
        raise NotImplementedError()

    def send(self, message):
        message = str(message)
        message = message.encode(encoding="utf-8")
        message = struct.pack('>I', len(message)) + message
        self.socket.sendall(message)

    def receive(self):
        raw_message_length = self.__recv(4)
        if not raw_message_length:
            return None
        message_length = struct.unpack('>I', raw_message_length)[0]
        return self.__recv(message_length).decode(encoding="utf-8")

    def __recv(self, message_length):
        data = bytearray()
        while len(data) < message_length:
            packet = self.socket.recv(message_length - len(data))
            if not packet:
                return None
            data.extend(packet)
        return data
