from robotwarapp.model.robotwar import RobotWar
from robotwarapp.model.robot import Robot
from robotwarapp.exceptions import InvalidArenaInput, InvalidRobotInput, RobotOutOfBounds, ArenaNotSetUp, InvalidMoveRobotInput, LocationOccupied, InvalidStrategyInput
from robotwarapp.helpers.inputvalidator import InputValidator


class RobotWarController:

    def __init__(self, no_of_robots):
        self.robot_war = RobotWar(no_of_robots)

    def handle_arena_input(self, arenainput):
        try:
            coords = InputValidator.validate_arena_input(arenainput)
        except InvalidArenaInput:
            return "invalid_arena_input"
        self.robot_war.set_up_arena(coords)
        return "arena_ready"

    def handle_robot_input(self, robotinput):
        try:
            position = InputValidator.validate_robot_input(
                robotinput, Robot.directions)
        except InvalidRobotInput:
            return "invalid_robot_input"
        try:
            self.robot_war.add_robot_to_arena(position)
        except RobotOutOfBounds:
            return "robot_out_of_bounds"
        except ArenaNotSetUp:
            return "arena_not_set_up"
        return "robot_ready"

    def handle_move_robot_input(self, robot, moverobotinput):
        try:
            move_commands = InputValidator.validate_move_robot_input(
                moverobotinput, Robot.commands.values()
            )
        except InvalidMoveRobotInput:
            return "invalid_move_robot_input"
        try:
            self.robot_war.robots[robot].control(move_commands, self.robot_war)
        except RobotOutOfBounds:
            return "robot_moved_out_of_arena"
        if self.robot_war.robot_attacked is True:
            return "robot_attacked"
        return "robot_moved"

    def handle_strategy_input(self, strategy_input):
        try:
            strategy = InputValidator.validate_strategy_input(
                strategy_input, RobotWar.attack_strategies
            )
        except InvalidStrategyInput:
            return "invalid_strategy_input"
        self.robot_war.battle("offensive")
        return "battle_finished"

    def get_final_positions(self):
        return [{
            "x": robot.x,
            "y": robot.y,
            "dir": robot.dir
        } for robot in self.robot_war.robots]
