from robotwarapp.controllers.robotwarcontroller import RobotWarController

if __name__ == '__main__':

    # Console app output strings
    output = {
        "set_up_arena": "Please enter the upper right coordinates of the arena as two numbers separated by a space: ",
        "arena_ready": "The arena has been set up: ",
        "arena_error": "ERROR: Invalid arena coordinates.",
        "set_up_robot": "Enter the position and orientation of the robot. Two numbers separated by a space, followed by a space and a letter representing its initial facing direction: N, E, S, W: ",
        "invalid_robot_input": "ERROR: Invalid robot details.",
        "robot_out_of_bounds_error": "ERROR: Your Robot is out of bounds of the arena.",
        "robot_ready": "The Robot has been set up: ",
        "arena_not_set_up": "The arena has not been set up",
        "move_robot": "Enter your robot moves.",
        "robot_moved": "Your Robot was moved.",
        "invalid_move_robot_input": "You entered invalid move robot input.",
        "robot_moved_out_of_arena": "Your robot moved beyond the bounds of the arena",
        "robot_moved_into_occupied_location": "Your robot moved into a location occupied by another robot."
    }

    # Initialise the Robot Wars app
    no_of_robots = 2
    app = RobotWarController(no_of_robots)

    # Set up the arena with console input e.g. "5 5"
    while True:
        response = app.handle_arena_input(
            input(output["set_up_arena"])
        )
        print(output[response])
        if response == "arena_ready":
            break

    for robot in range(no_of_robots):
        # Set the robots starting position with console input e.g. "2 2 N"
        while True:
            response = app.handle_robot_input(
                input(output["set_up_robot"])
            )
            print(output[response])
            if response == "robot_ready":
                break

        # Move the robot with console input e.g. "MMLMRMM"
        while True:
            response = app.handle_move_robot_input(
                robot,
                input(output["move_robot"])
            )
            print(output[response])
            if response == "robot_moved":
                break

    # Print final positions
    final_positions = app.get_final_positions()
    for robot in final_positions:
        print(str(robot["x"]) + " " + str(robot["y"]) + " " + robot["dir"])
