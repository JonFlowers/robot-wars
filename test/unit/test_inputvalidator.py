import unittest
from robotwarapp.helpers.inputvalidator import InputValidator
from robotwarapp.exceptions import InvalidArenaInput, InvalidRobotInput, InvalidMoveRobotInput, InvalidStrategyInput


class TestInputValidator(unittest.TestCase):
    def setUp(self):
        pass

    def test_validate_arena_input(self):
        self.assertEqual(InputValidator.validate_arena_input("5 5"), [5, 5])
        self.assertEqual(
            InputValidator.validate_arena_input("10 10"), [10, 10])
        self.assertEqual(InputValidator.validate_arena_input("1 1"), [1, 1])
        self.assertRaises(InvalidArenaInput,
                          InputValidator.validate_arena_input, "5")
        self.assertRaises(InvalidArenaInput,
                          InputValidator.validate_arena_input, "5 5 5")
        self.assertRaises(InvalidArenaInput,
                          InputValidator.validate_arena_input, "0 5")
        self.assertRaises(InvalidArenaInput,
                          InputValidator.validate_arena_input, "5 0")
        self.assertRaises(InvalidArenaInput,
                          InputValidator.validate_arena_input, "0 0")
        self.assertRaises(InvalidArenaInput,
                          InputValidator.validate_arena_input, "a b")

    def test_validate_robot_input(self):
        self.assertEqual(InputValidator.validate_robot_input(
            "1 1 N", ["N", "S", "E", "W"]), [1, 1, "N"])
        self.assertEqual(InputValidator.validate_robot_input(
            "1 1 S", ["N", "S", "E", "W"]), [1, 1, "S"])
        self.assertEqual(InputValidator.validate_robot_input(
            "1 1 E", ["N", "S", "E", "W"]), [1, 1, "E"])
        self.assertEqual(InputValidator.validate_robot_input(
            "1 1 W", ["N", "S", "E", "W"]), [1, 1, "W"])
        self.assertRaises(InvalidRobotInput, InputValidator.validate_robot_input, "1 1", [
                          "N", "S", "E", "W"])
        self.assertRaises(InvalidRobotInput, InputValidator.validate_robot_input, "1 1 N N", [
                          "N", "S", "E", "W"])
        self.assertRaises(InvalidRobotInput, InputValidator.validate_robot_input, "12345", [
                          "N", "S", "E", "W"])
        self.assertRaises(InvalidRobotInput, InputValidator.validate_robot_input, "fefsfd", [
                          "N", "S", "E", "W"])

    def test_validate_move_robot_input(self):
        self.assertEqual(InputValidator.validate_move_robot_input(
            "LRM", ["L", "R", "M"]), "LRM")
        self.assertEqual(InputValidator.validate_move_robot_input(
            "LMLMLMLMM", ["L", "R", "M"]), "LMLMLMLMM")
        self.assertRaises(
            InvalidMoveRobotInput, InputValidator.validate_move_robot_input, "LRM", ["L", "R"])
        self.assertRaises(
            InvalidMoveRobotInput, InputValidator.validate_move_robot_input, "LRME", ["L", "R", "M"])

    def test_validate_strategy_input(self):
        self.assertRaises(
          InvalidStrategyInput,
          InputValidator.validate_strategy_input, "3", ["offensive", "defensive"])
        self.assertEqual(
          InputValidator.validate_strategy_input("1", ["offensive", "defensive"]), "offensive")
        self.assertEqual(
          InputValidator.validate_strategy_input("2", ["offensive", "defensive"]), "defensive")
        self.assertRaises(InvalidStrategyInput, InputValidator.validate_strategy_input,"fdsfeff", ["offensive", "defensive"])
        self.assertRaises(InvalidStrategyInput, InputValidator.validate_strategy_input, "12345", ["offensive", "defensive"])
