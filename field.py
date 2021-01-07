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
