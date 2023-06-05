import unittest
from unittest.mock import MagicMock, Mock
from robotwarapp.controllers.robotwarcontroller import RobotWarController


class TestRobotWarController(unittest.TestCase):
    def setUp(self):
        self.app = RobotWarController(2)

    def test_handle_arena_input(self):
        inputs = [
            "5 5",
            "12 4",
            "2 2"
        ]
        coords = [
            (5, 5),
            (12, 4),
            (2, 2)
        ]
        for i in range(len(inputs)):
            self.app.handle_arena_input(inputs[i])
            self.assertTrue(self.app.robot_war.arena.x == coords[i][0])
            self.assertTrue(self.app.robot_war.arena.y == coords[i][1])

    def test_handle_arena_input_with_invalid_input(self):
        inputs = [
            "-2 -2",
            "-4 4",
            "0 0",
            "6 0",
            "3 e",
            "36",
            "3624",
            "23hg654hn"
        ]
        for input in inputs:
            self.assertTrue(
                self.app.handle_arena_input(input) == "invalid_arena_input"
                )

    def test_handle_robot_input(self):
        self.app.handle_arena_input("5 5")
        inputs = [
            "3 6 N",
            "4 4 S"
        ]
        for input in inputs:
            self.app.handle_robot_input(input)
            # self.assertTrue(self.app.robot_war.robots[input])

    def test_handle_robot_input_with_invalid_input(self):
        inputs = [
            "23N",
            "2 4",
            "8 8e R",
            "6 6 K"
        ]
        for input in inputs:
            self.assertTrue(
                self.app.handle_robot_input(input) == "invalid_robot_input"
                )

    def test_robot_moved_to_occupied_location(self):
        self.app.handle_arena_input("5 5")
        self.app.handle_robot_input("1 1 N")
        self.app.handle_robot_input("2 2 N")
        self.assertTrue(
            self.app.handle_move_robot_input(0, "MRM") == "robot_attacked"
        )

    def tearDown(self):
        del self.app
