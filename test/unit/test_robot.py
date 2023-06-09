import unittest
from robotwarapp.model.robotwar import RobotWar
from robotwarapp.model.arena import Arena
from robotwarapp.model.robot import Robot
from robotwarapp.exceptions import RobotOutOfBounds


class TestRobot(unittest.TestCase):
    def setUp(self):
        self.robot_war = RobotWar(2)
        self.robot_war.set_up_arena([10, 10])
        self.robot_war.add_robot_to_arena([1, 1, "N"])

    def test_set_x(self):
        self.robot_war.robots[0].set_x(4, self.robot_war.arena)
        self.assertTrue(self.robot_war.robots[0].x == 4)

    def test_set_x_out_of_bounds(self):
        with self.assertRaises(RobotOutOfBounds):
            self.robot_war.robots[0].set_x(12, self.robot_war.arena)

    def test_set_y(self):
        self.robot_war.robots[0].set_y(4, self.robot_war.arena)
        self.assertTrue(self.robot_war.robots[0].y == 4)

    def test_set_y_out_of_bounds(self):
        with self.assertRaises(RobotOutOfBounds):
            self.robot_war.robots[0].set_y(12, self.robot_war.arena)

    def test_set_dir(self):
        self.robot_war.robots[0].set_dir("N")
        self.assertTrue(self.robot_war.robots[0].dir == "N")

    def test_control(self):
        self.robot_war.robots[0].control(["M", "M", "R", "M"], self.robot_war)
        self.assertTrue(self.robot_war.robots[0].x == 2)
        self.assertTrue(self.robot_war.robots[0].y == 3)
        self.assertTrue(self.robot_war.robots[0].dir == "E")

    def test_control_two(self):
        self.robot_war.robots[0].control(["R", "M", "L", "M"], self.robot_war)
        self.assertTrue(self.robot_war.robots[0].x == 2)
        self.assertTrue(self.robot_war.robots[0].y == 2)
        self.assertTrue(self.robot_war.robots[0].dir == "N")

    def test_control_robot_attacked(self):
        self.robot_war.add_robot_to_arena([2, 2, "N"])
        self.robot_war.robots[0].control(["M", "R", "M", "M", "M"], self.robot_war)
        self.assertTrue(self.robot_war.robots[0].x == 2)
        self.assertTrue(self.robot_war.robots[0].y == 2)
        self.assertTrue(self.robot_war.robot_attacked)
