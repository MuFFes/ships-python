from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])


class Field:
    def __init__(self):
        self.shots = [
            Point(x=0, y=3),
            Point(x=0, y=5),
            Point(x=5, y=5),
        ]
        self.ships = [
            Point(x=0, y=3),
            Point(x=1, y=1),
            Point(x=0, y=1),
        ]

    def get_state(self, x, y):
        if Point(x=x, y=y) in self.ships:
            if Point(x=x, y=y) in self.shots:
                return "X"
            return " "
        if Point(x=x, y=y) in self.shots:
            return "."
        return ""

    def check_collision(self, x, y):
        if x > 9 or y > 9:
            return True
        for dx in range(-1, 2, 1):
            for dy in range(-1, 2, 1):
                if Point(x=x+dx, y=y+dy) in self.ships:
                    return True
        return False


