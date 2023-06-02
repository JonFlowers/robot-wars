import unittest
from unittest.mock import MagicMock, Mock
from robotwarapp.model.robotwar import Arena


class TestArena(unittest.TestCase):
    def setUp(self):
        self.arena = Arena()

    def test_set_x(self):
        self.arena.set_x(6)
        self.assertTrue(self.arena.x == 6)

    def test_set_y(self):
        self.arena.set_y(6)
        self.assertTrue(self.arena.y == 6)

    def tearDown(self):
        del self.arena
