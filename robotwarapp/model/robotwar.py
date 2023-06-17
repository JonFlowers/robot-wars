from robotwarapp.model.arena import Arena
from robotwarapp.model.robot import Robot
from robotwarapp.exceptions import RobotOutOfBounds, ArenaNotSetUp, LocationOccupied, InvalidStrategy, RobotNotAttacked


class RobotWar:

    attack_strategies = [
        'offensive',
        'defensive'
    ]

    def __init__(self, no_of_robots):
        self.arena = Arena()
        self.no_of_robots = no_of_robots
        self.robots = []
        self.robot_attacked = False
        self.robots_in_battle = []

    def set_up_arena(self, coords):
        self.arena.set_x(coords[0])
        self.arena.set_y(coords[1])

    def add_robot_to_arena(self, position):
        x, y, dir = position
        if not self.arena.is_arena_ready():
            raise ArenaNotSetUp
        if not self.arena.is_valid_location(x, y):
            raise RobotOutOfBounds
        self.robots.append(Robot(x, y, dir))

    def is_location_occupied(self, x, y):
        for robot in self.robots:
            if robot.x == x and robot.y == y:
                return True
        return False

    def get_robot_in_location(self, x, y):
        for robot in self.robots:
            if robot.x ==  x and robot.y == y:
                return robot

    def attack(self, attacking_robot, attacked_robot):
        self.robots_in_battle.extend([attacking_robot, attacked_robot])
        self.robot_attacked = True

    def battle(self, strategy):
        if self.robot_attacked is False:
            raise RobotNotAttacked
        if strategy not in self.attack_strategies:
            raise InvalidStrategy
        self.robot_attacked = False
        return True
