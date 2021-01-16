from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])


class Field:
    def __init__(self):
        self.shots = []
        self.ships = []

    def get_state(self, x, y):
        if Point(x, y) in self.ships:
            if Point(x, y) in self.shots:
                return "X"
            return " "
        if Point(x, y) in self.shots:
            return "."
        return ""

    def check_collision(self, x, y):
        if x > 9 or y > 9:
            return True
        for dx in range(-1, 2, 1):
            for dy in range(-1, 2, 1):
                if Point(x + dx, y + dy) in self.ships:
                    return True
        return False

    def get_ship(self, x, y, ship=None):
        if ship is None:
            ship = []
        if Point(x, y) in self.ships:
            if Point(x, y) not in ship:
                ship.append(Point(x, y))

                for point in ship:
                    self.get_ship(point.x - 1, point.y, ship)
                    self.get_ship(point.x + 1, point.y, ship)
                    self.get_ship(point.x, point.y - 1, ship)
                    self.get_ship(point.x, point.y + 1, ship)
        return ship

    def is_drowned(self, x, y) -> bool:
        if any(s not in self.shots for s in self.get_ship(x, y)):
            return False
        return True

    def drown(self, x, y):
        for point in self.get_ship(x, y):
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    if Point(point.x + i, point.y + j) not in self.shots:
                        if Point(point.x + i, point.y + j) not in self.ships:
                            self.shots.append(Point(point.x + i, point.y + j))
