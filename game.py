import random
import enum

import field


class Orientation(enum.IntEnum):
    HORIZONTAL = 0
    VERTICAL = 1


class GamePhase(enum.IntEnum):
    SETUP_SHIPS = 0
    SETUP_WAIT = 1
    SHOOT = 2
    WAIT_FOR_SHOT = 3
    YOU_WON = 4
    YOU_LOST = 5


class Game:
    def __init__(self, connection, is_server):
        self.connection = connection
        self.is_server = is_server
        self.priority = random.randint(-32767, 32768)
        self.enemy_priority = None
        self.phase = GamePhase.SETUP_SHIPS
        self.ships_size = [4, 3, 2, 1]#[4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        self.ship_orientation = Orientation.HORIZONTAL
        self.my_field = field.Field()
        self.enemy_field = field.Field()

    def start(self):
        self.connection.open()
        self.connection.send(self.priority)
        self.enemy_priority = int(self.connection.receive())

    def shoot(self, x, y):
        tile_state = self.enemy_field.get_state(x, y)
        if tile_state == 0:
            pass

    def wait_for_shot(self):
        coords = self.connection.receive()

    def validate_ship_position(self, x, y) -> bool:
        for i in range(self.ships_size[0]):
            if self.ship_orientation == Orientation.HORIZONTAL:
                if self.my_field.check_collision(x + i, y):
                    return False
            if self.ship_orientation == Orientation.VERTICAL:
                if self.my_field.check_collision(x, y + i):
                    return False
        return True

    def place_ship(self, x, y):
        if self.validate_ship_position(x, y):
            for i in range(self.ships_size.pop(0)):
                if self.ship_orientation == Orientation.HORIZONTAL:
                    self.my_field.ships.append(field.Point(x + i, y))
                if self.ship_orientation == Orientation.VERTICAL:
                    self.my_field.ships.append(field.Point(x, y + i))
            # Change state if all ships are already placed
            if len(self.ships_size) == 0:
                self.phase = GamePhase.SETUP_WAIT
            return True
        else:
            return False

    def finish_setup(self):
        self.connection.send("finished")
        if self.connection.receive() == "finished":
            if self.priority > self.enemy_priority or (self.priority == self.enemy_priority and self.is_server is True):
                self.phase = GamePhase.SHOOT
            else:
                self.phase = GamePhase.WAIT_FOR_SHOT

    def step(self):
        pass

    def draw(self):
        pass

    def end(self):
        pass
