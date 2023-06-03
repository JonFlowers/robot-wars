import unittest
from robotwarapp.model.arena import Arena
from robotwarapp.model.robot import Robot


class TestRobot(unittest.TestCase):
    def setUp(self):
        self.arena = Arena()
        self.arena.set_x(10)
        self.arena.set_y(10)
        self.robot = Robot(1, 1, "N")

    def test_set_x(self):
        self.robot.set_x(4, self.arena)
        self.assertTrue(self.robot.x == 4)
