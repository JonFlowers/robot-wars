from behave import *
from robotwarapp.controllers.robotwarcontroller import *


@given('a Robot has been addedd to the arena "{robotinput}"')
def enter_coordinates(context, robotinput):
    context.response = context.app.handle_robot_input(robotinput)

@when('I enter move robot commands "{moverobotinput}"')
def enter_invalid_input(context, moverobotinput):
    context.response = context.app.handle_move_robot_input(0, moverobotinput)

@then('a robot moved response is returned')
def success_message(context):
    assert (context.response == "robot_moved")

@then('an invalid move robot input error is returned')
def success_message(context):
    assert (context.response == "invalid_move_robot_input")

@then('a robot moved out of bounds error is returned')
def invalid_input_error(context):
    assert (context.response == "robot_moved_out_of_arena")
