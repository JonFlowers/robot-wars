from behave import *
from robotwarapp.controllers.robotwarcontroller import *


@given('the Robot Wars app has been run "{robots}"')
def run_robot_wars(context, robots):
    context.app = RobotWarController(robots)

@when('I enter arena input "{arenainput}"')
def enter_coordinates(context, arenainput):
    context.response = context.app.handle_arena_input(arenainput)

@then('an arena ready response is returned')
def success_message(context):
    assert (context.response == "arena_ready" )

@then('an invalid arena input error is returned')
def invalid_input_error(context):
    assert (context.response == "invalid_arena_input" )
