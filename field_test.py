import unittest
import parameterized

import field


class FieldTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.field = field.Field()
        cls.field.shots = [
            field.Point(2, 1),
            field.Point(7, 2),
            field.Point(7, 3),
            field.Point(5, 5),
        ]
        cls.field.ships = [
            # Ship 1
            field.Point(1, 1),
            field.Point(2, 1),
            field.Point(3, 1),
            # Ship 2
            field.Point(4, 5),
            field.Point(4, 6),
            field.Point(4, 7),
            field.Point(4, 8),
            # Ship 3
            field.Point(7, 2),
            field.Point(7, 3),
        ]

    def test_get_state(self):
        self.assertEqual(self.field.get_state(0, 1), "")
        self.assertEqual(self.field.get_state(1, 1), " ")
        self.assertEqual(self.field.get_state(2, 1), "X")
        self.assertEqual(self.field.get_state(5, 5), ".")

    @parameterized.parameterized.expand([
        [(3, 3), False],
        [(4, 3), False],
        [(0, 0), True],
        [(0, 1), True],
        [(2, 6), False],
        [(3, 6), True],
        [(4, 6), True],
        [(5, 6), True],
        [(6, 6), False],
    ])
    def test_check_collision(self, input_value, expected_value):
        (x, y) = input_value
        self.assertEqual(self.field.check_collision(x, y), expected_value)

    @parameterized.parameterized.expand([
        [(4, 6), [(4, 5), (4, 6), (4, 7), (4, 8)]],
        [(4, 4), []],
        [(3, 1), [(1, 1), (2, 1), (3, 1)]],
    ])
    def test_get_ship(self, input_value, expected_value):
        (x, y) = input_value
        ship = self.field.get_ship(x, y)
        self.assertEqual(len(ship), len(expected_value))
        for point in self.field.get_ship(x, y):
            self.assertIn((point.x, point.y), expected_value)

    @parameterized.parameterized.expand([
        [(7, 2), True],
        [(2, 1), False],
        [(4, 6), False],
        [(8, 8), False],
    ])
    def test_is_drowned(self, input_value, expected_value):
        (x, y) = input_value
        self.assertEqual(self.field.is_drowned(x, y), expected_value)

    def test_drown(self):
        self.field.drown(7, 2)
        for x in range(6, 9):
            for y in range(1, 5):
                self.assertIn((x, y), self.field.shots)


if __name__ == "__main__":
    unittest.main()
