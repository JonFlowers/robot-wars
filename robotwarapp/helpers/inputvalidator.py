from robotwarapp.exceptions import InvalidArenaInput, InvalidRobotInput, InvalidMoveRobotInput, InvalidStrategyInput


class InputValidator:

    def validate_arena_input(arenainput):
        try:
            coords = [int(coord) for coord in arenainput.split(" ")]
        except ValueError:
            raise InvalidArenaInput
        if len(coords) != 2:
            raise InvalidArenaInput
        for coord in coords:
            if coord < 1:
                raise InvalidArenaInput
        return coords

    def validate_robot_input(robotinput, directions):
        position = [pos for pos in robotinput.split(" ")]
        try:
            position[0] = int(position[0])
            position[1] = int(position[1])
        except ValueError:
            raise InvalidRobotInput
        except IndexError:
            raise InvalidRobotInput
        if len(position) != 3:
            raise InvalidRobotInput
        if position[2].upper() not in directions:
            raise InvalidRobotInput
        return position

    def validate_move_robot_input(moverobotinput, commands):
        for command in moverobotinput:
            if command not in commands:
                raise InvalidMoveRobotInput
        return moverobotinput

    def validate_strategy_input(strategyinput, strategies):
        try:
            if int(strategyinput) > len(strategies):
                raise InvalidStrategyInput
        except ValueError:
            raise InvalidStrategyInput
        return strategies[int(strategyinput) - 1]
