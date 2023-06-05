from behave import *
from robotwarapp.controllers.robotwarcontroller import *

@given('a Robot has been added to the arena "{robotinput}"')
def set_up_arena(context, robotinput):
    context.app.handle_robot_input(robotinput)

@given('the Robot has been moved "{moverobotinput}"')
def set_up_arena(context, moverobotinput):
    context.app.handle_move_robot_input(0, moverobotinput)
