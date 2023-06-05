import unittest
from unittest.mock import MagicMock, Mock
from robotwarapp.model.robotwar import *


class TestRobotWar(unittest.TestCase):
    def setUp(self):
        self.robot_war = RobotWar(2)

    def test_set_up_arena(self):
        self.robot_war.set_up_arena((5, 5))
        self.assertTrue(self.robot_war.arena.x == 5)
        self.assertTrue(self.robot_war.arena.y == 5)

    def test_add_robot(self):
        self.robot_war.set_up_arena((5, 5))
        self.robot_war.add_robot_to_arena((5, 5, "W"))
        self.assertTrue(self.robot_war.robots[0].x == 5)
        self.assertTrue(self.robot_war.robots[0].y == 5)
        self.assertTrue(self.robot_war.robots[0].dir == "W")

    def test_is_location_occupied_true(self):
        self.robot_war.set_up_arena((5, 5))
        self.robot_war.add_robot_to_arena((1, 1, "N"))
        self.robot_war.add_robot_to_arena((2, 2, "N"))
        self.robot_war.robots[0].control("MRM", self.robot_war)
        self.assertTrue(self.robot_war.robot_attacked)
        self.assertTrue(self.robot_war.robots[0].x == self.robot_war.robots[1].x)
        self.assertTrue(self.robot_war.robots[0].y == self.robot_war.robots[1].y)

    def tearDown(self):
        del self.robot_war
