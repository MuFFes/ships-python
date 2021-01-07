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


