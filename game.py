import random
import enum

import field


class Orientation(enum.Enum):
    HORIZONTAL = 0
    VERTICAL = 1


class GamePhase(enum.Enum):
    SETUP_SHIPS = 0
    SHOOT = 1
    WAIT_FOR_SHOT = 2
    YOU_WON = 3
    YOU_LOST = 4


class Game:
    def __init__(self, connection, is_server):
        self.connection = connection
        self.is_server = is_server
        self.priority = random.randint(-32767, 32768)
        self.enemy_priority = None
        self.phase = GamePhase.SETUP_SHIPS
        self.ships_size = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        self.ship_orientation = Orientation.HORIZONTAL
        self.my_field = field.Field()
        self.enemy_field = field.Field()

    def start(self):
        self.connection.open()
        self.connection.send(self.priority)
        self.enemy_priority = int(self.connection.receive())

        # if self.priority > self.enemy_priority or (self.priority == self.enemy_priority and self.is_server is True):
        #     self.is_active = True
        # else:
        #     self.is_active = False
        #     self.wait_for_shot()

    def shoot(self, x, y):
        tile_state = self.enemy_field.get_state(x, y)
        if tile_state == 0:
            pass


    def wait_for_shot(self):
        coords = self.connection.receive()

    def place_ship(self, x, y):
        pass


    def step(self):
        pass

    def draw(self):
        pass

    def end(self):
        pass
