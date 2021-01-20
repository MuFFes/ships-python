import unittest
import random
from unittest import mock
import queue

import game
from Connection import connection


class GameTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.game = game.Game(None, None)

    def test_start_connection_refused(self):
        self.game.connection = mock.MagicMock(connection.Connection)
        self.game.connection.receive.side_effect = ConnectionRefusedError
        message_queue = queue.Queue()
        self.game.start(message_queue)
        self.assertEqual(message_queue.qsize(), 1)
        self.assertEqual(message_queue.get(True), "Connection error")

    def test_start_successful(self):
        self.game.connection = mock.MagicMock(connection.Connection)
        self.game.connection.receive.return_value = random.randint(-32767, 32768)
        message_queue = queue.Queue()
        self.game.start(message_queue)
        self.assertEqual(message_queue.qsize(), 1)
        self.assertEqual(message_queue.get(True), "Task finished")
        self.assertTrue(self.game.enemy_priority >= -32767)
        self.assertTrue(self.game.enemy_priority < 32768)


if __name__ == "__main__":
    unittest.main()
