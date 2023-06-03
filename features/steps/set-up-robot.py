from behave import *
from robotwarapp.controllers.robotwarcontroller import *

@given('the Robot Wars arena has been set up "{arenainput}"')
def set_up_arena(context, arenainput):
    context.app.handle_arena_input(arenainput)

@given('the Robot Wars arena has not been set up')
def set_up_arena(context):
    pass

@when('I enter robot input "{robotinput}"')
def enter_coordinates(context, robotinput):
    context.response = context.app.handle_robot_input(robotinput)

@then('a robot ready response is returned')
def invalid_input_error(context):
    assert (context.response == "robot_ready" )

@then('an invalid robot input error is returned')
def invalid_input_error(context):
    assert (context.response == "invalid_robot_input" )

@then('a robot out of bounds error is returned')
def invalid_input_error(context):
    assert (context.response == "robot_out_of_bounds" )

@then('an arena has not been set up error is returned')
def invalid_input_error(context):
    assert (context.response == "arena_not_set_up" )