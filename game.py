import random


class Game:
    def __init__(self, connection, is_server):
        self.connection = connection
        self.is_server = is_server
        self.priority = random.randint(-32767, 32768)
        self.enemy_priority = None
        self.is_winner = None
        self.is_active = None
        self.ships_size = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        self.my_field = None
        self.enemy_field = None

    def start(self):
        self.connection.open()
        self.connection.send(self.priority)
        self.enemy_priority = int(self.connection.receive())

        if self.priority > self.enemy_priority or (self.priority == self.enemy_priority and self.is_server is True):
            self.is_active = True
        else:
            self.is_active = False
            self.wait_for_shot()

    def shoot(self):
        if self.is_active:
            pass

    def wait_for_shot(self):
        coords = self.connection.receive()

    def setup_fields(self):
        pass

    def step(self):
        pass

    def draw(self):
        pass

    def end(self):
        pass
