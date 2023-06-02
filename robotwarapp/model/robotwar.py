from robotwarapp.model.arena import Arena
from robotwarapp.model.robot import Robot
from robotwarapp.exceptions import RobotOutOfBounds, ArenaNotSetUp, LocationOccupied


class RobotWar:

    def __init__(self, no_of_robots):
        self.arena = Arena()
        self.no_of_robots = no_of_robots
        self.robots = []

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
