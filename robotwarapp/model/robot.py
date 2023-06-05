from robotwarapp.exceptions import RobotOutOfBounds, LocationOccupied


class Robot:

    commands = {
        "move": "M",
        "turn_left": "L",
        "turn_right": "R"
    }

    directions = [
        "N", "E", "S", "W"
    ]

    def __init__(self, x, y, dir):
        self.x = x
        self.y = y
        self.dir = dir

    def set_x(self, x, arena):
        if arena.is_valid_location(x, self.y) is not True:
            raise RobotOutOfBounds
        self.x = x

    def set_y(self, y, arena):
        if arena.is_valid_location(self.x, y) is not True:
            raise RobotOutOfBounds
        self.y = y

    def set_dir(self, dir):
        self.dir = dir

    def control(self, commands, robot_war):
        for command in commands:
            if command == self.commands["turn_left"]:
                self.turn_left()
            elif command == self.commands["turn_right"]:
                self.turn_right()
            elif command == self.commands["move"]:
                self.move(robot_war) 
                if robot_war.robot_attacked is True:
                    return

    def turn_left(self):
        if self.dir == "N":
            self.dir = "W"
        elif self.dir == "E":
            self.dir = "N"
        elif self.dir == "S":
            self.dir = "E"
        elif self.dir == "W":
            self.dir = "S"

    def turn_right(self):
        if self.dir == "N":
            self.dir = "E"
        elif self.dir == "E":
            self.dir = "S"
        elif self.dir == "S":
            self.dir = "W"
        elif self.dir == "W":
            self.dir = "N"

    def move(self, robot_war):
        new_x = self.x
        new_y = self.y
        if self.dir == "N":
            new_y = self.y + 1
        elif self.dir == "E":
            new_x = self.x + 1
        elif self.dir == "S":
            new_y = self.y - 1
        elif self.dir == "W":
            new_x = self.x - 1

        if robot_war.is_location_occupied(new_x, new_y):
            robot_war.attack()

        self.set_x(new_x, robot_war.arena)
        self.set_y(new_y, robot_war.arena)
