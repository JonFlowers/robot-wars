import unittest
from unittest.mock import MagicMock, Mock
from robotwarapp.controllers.robotwarcontroller import RobotWarController


class TestMultipleRobotWars(unittest.TestCase):
    def setUp(self):
        self.robot_war_app_one = RobotWarController(1)
        self.robot_war_app_one.handle_arena_input("2 2")
        self.robot_war_app_one.handle_robot_input("3 6 N")

        self.robot_war_app_two = RobotWarController(1)
        self.robot_war_app_two.handle_arena_input("4 4")
        self.robot_war_app_two.handle_robot_input("4 4 S")

    def test_no_of_robots(self):
        pass

    def tearDown(self):
        del self.robot_war_app_one
        del self.robot_war_app_two
