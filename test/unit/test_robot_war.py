import unittest
from robotwarapp.exceptions import RobotOutOfBounds, ArenaNotSetUp, RobotNotAttacked, InvalidStrategy
from unittest.mock import MagicMock, Mock
from robotwarapp.model.robotwar import *


class TestRobotWar(unittest.TestCase):
    def setUp(self):
        self.robot_war = RobotWar(2)

    def test_set_up_arena(self):
        self.robot_war.set_up_arena((5, 5))
        self.assertTrue(self.robot_war.arena.x == 5)
        self.assertTrue(self.robot_war.arena.y == 5)

    def test_add_robot_to_arena(self):
        self.robot_war.set_up_arena((5, 5))
        self.robot_war.add_robot_to_arena((5, 5, "W"))
        self.assertTrue(self.robot_war.robots[0].x == 5)
        self.assertTrue(self.robot_war.robots[0].y == 5)
        self.assertTrue(self.robot_war.robots[0].dir == "W")

    def test_add_robot_to_arena_out_of_bounds(self):
        self.robot_war.set_up_arena((5, 5))
        with self.assertRaises(RobotOutOfBounds):
            self.robot_war.add_robot_to_arena((6, 6, "W"))

    def test_add_robot_to_arena_arena_not_set_up(self):
        with self.assertRaises(ArenaNotSetUp):
            self.robot_war.add_robot_to_arena((5, 5, "W"))

    def test_is_location_occupied_true(self):
        self.robot_war.set_up_arena((5, 5))
        self.robot_war.add_robot_to_arena((1, 1, "N"))
        self.robot_war.add_robot_to_arena((2, 2, "N"))
        self.robot_war.robots[0].control("MRM", self.robot_war)
        self.assertTrue(self.robot_war.robot_attacked)
        self.assertTrue(
            self.robot_war.robots[0].x == self.robot_war.robots[1].x)
        self.assertTrue(
            self.robot_war.robots[0].y == self.robot_war.robots[1].y)

    def test_get_robot_in_location(self):
        self.robot_war.set_up_arena((5, 5))
        self.robot_war.add_robot_to_arena((1, 1, "N"))
        self.robot_war.add_robot_to_arena((2, 2, "N"))
        self.robot_war.robots[0].control("MRM", self.robot_war)
        self.assertTrue(self.robot_war.robot_attacked)
        self.assertTrue(
            self.robot_war.get_robot_in_location(
                self.robot_war.robots[0].x,
                self.robot_war.robots[0].y
            ) == self.robot_war.robots[0]
        )

    def test_attack(self):
        self.robot_war.set_up_arena((5, 5))
        self.robot_war.add_robot_to_arena((1, 1, "N"))
        self.robot_war.add_robot_to_arena((2, 2, "N"))
        self.robot_war.robots[0].control("MRM", self.robot_war)
        self.assertTrue(self.robot_war.robot_attacked)
        self.assertTrue(len(self.robot_war.robots_in_battle) == 2)
        self.assertEquals(self.robot_war.robots_in_battle[0], self.robot_war.robots[0])
        self.assertEquals(self.robot_war.robots_in_battle[1], self.robot_war.robots[1])

    def test_battle(self):
        self.robot_war.set_up_arena((5, 5))
        self.robot_war.add_robot_to_arena((1, 1, "N"))
        self.robot_war.add_robot_to_arena((2, 2, "N"))
        self.robot_war.robots[0].control("MRM", self.robot_war)
        self.assertTrue(
            self.robot_war.battle("offensive")
        )
        self.assertFalse(self.robot_war.robot_attacked)

    def test_battle_robot_attacked_false(self):
        self.robot_war.set_up_arena((5, 5))
        self.robot_war.add_robot_to_arena((1, 1, "N"))
        self.robot_war.add_robot_to_arena((2, 2, "N"))
        with self.assertRaises(RobotNotAttacked):
            self.robot_war.battle("offensive")

    def test_battle_invalid_strategy(self):
        self.robot_war.set_up_arena((5, 5))
        self.robot_war.add_robot_to_arena((1, 1, "N"))
        self.robot_war.add_robot_to_arena((2, 2, "N"))
        self.robot_war.robots[0].control("MRM", self.robot_war)
        with self.assertRaises(InvalidStrategy):
            self.robot_war.battle("xxxxxxx")

    def tearDown(self):
        del self.robot_war
