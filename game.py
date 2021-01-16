import random
import enum
import field


class Orientation(enum.IntEnum):
    HORIZONTAL = 0
    VERTICAL = 1


class GamePhase(enum.IntEnum):
    WAIT_FOR_CONNECTION = 0
    SETUP_SHIPS = 1
    SETUP_WAIT = 2
    SHOOT = 3
    WAIT_FOR_SHOT = 4
    YOU_WON = 5
    YOU_LOST = 6


class Game:
    def __init__(self, connection, is_server):
        self.connection = connection
        self.is_server = is_server
        self.priority = random.randint(-32767, 32768)
        self.enemy_priority = None
        self.phase = GamePhase.WAIT_FOR_CONNECTION
        self.ships_size = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        self.ship_orientation = Orientation.HORIZONTAL
        self.my_field = field.Field()
        self.enemy_field = field.Field()
        self.update_pending = False

    def start(self, queue):
        try:
            self.connection.open()
            self.phase = GamePhase.SETUP_SHIPS
            self.update_pending = True
            self.connection.send(self.priority)
            self.enemy_priority = int(self.connection.receive())
        except (ConnectionRefusedError, ConnectionAbortedError):
            queue.put("Connection error")
            return
        queue.put("Task finished")

    def shoot(self, queue, x, y):
        tile_state = self.enemy_field.get_state(x, y)
        if tile_state is not ".":
            message = str(x) + str(y)
            self.connection.send(message)
            response = self.connection.receive()
            self.enemy_field.shots.append(field.Point(x, y))
            if response in ["X", "Z"]:
                self.enemy_field.ships.append(field.Point(x, y))
                if response == "Z":
                    self.enemy_field.drown(x, y)
                    if self.connection.receive() == "end":
                        self.phase = GamePhase.YOU_WON
            else:
                self.phase = GamePhase.WAIT_FOR_SHOT
                self.wait_for_shot()
            self.update_pending = True
        queue.put("Task finished")

    def wait_for_shot(self):
        self.update_pending = True
        if self.phase == GamePhase.WAIT_FOR_SHOT:
            coords = self.connection.receive()
            (x, y) = (int(coords[0]), int(coords[1]))
            self.my_field.shots.append(field.Point(x, y))
            state = self.my_field.get_state(x, y)
            if state == "X":
                if self.my_field.is_drowned(x, y):
                    self.my_field.drown(x, y)
                    state = "Z"
            self.connection.send(state)
            # Check if all ships are drowned
            if state == "Z":
                if all(s in self.my_field.shots for s in self.my_field.ships):
                    self.connection.send("end")
                    self.phase = GamePhase.YOU_LOST
                    self.update_pending = True
                else:
                    self.connection.send("continue")

            if state == "X" or state == "Z":
                self.wait_for_shot()
                if self.phase == GamePhase.YOU_LOST:
                    return
            self.phase = GamePhase.SHOOT
            self.update_pending = True

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
        return False

    def finish_setup(self, queue):
        self.connection.send("finished")
        if self.connection.receive() == "finished":
            if self.priority > self.enemy_priority or (self.priority == self.enemy_priority and self.is_server is True):
                self.phase = GamePhase.SHOOT
                self.update_pending = True
            else:
                self.phase = GamePhase.WAIT_FOR_SHOT
                self.wait_for_shot()
        queue.put("Task finished")
