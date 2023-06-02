import unittest
from unittest.mock import MagicMock, Mock
from robotwarapp.model.robotwar import *


class TestRobotWar(unittest.TestCase):
    def setUp(self):
        self.robot_war = RobotWar(1)

    def test_set_up_arena(self):
        self.robot_war.set_up_arena((5, 5))
        self.assertTrue(self.robot_war.arena.x == 5)
        self.assertTrue(self.robot_war.arena.y == 5)

    def test_add_robot(self):
        self.robot_war.set_up_arena((5, 5))
        self.robot_war.add_robot_to_arena((5, 5, "W"))
        print(self.robot_war.robots[0].dir)
        self.assertTrue(self.robot_war.robots[0].x == 5)
        self.assertTrue(self.robot_war.robots[0].y == 5)
        self.assertTrue(self.robot_war.robots[0].dir == "W")

    def tearDown(self):
        del self.robot_war
