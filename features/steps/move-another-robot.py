from behave import *
from robotwarapp.controllers.robotwarcontroller import *


@then('a robot attacked response is returned')
def success_message(context):
    assert (context.response == "robot_attacked")


@then('the robot has stopped in the occupied location')
def robot_locations(context):
    robots = context.app.get_final_positions()
    assert (robots[0]["x"] == 1)
    assert (robots[0]["y"] == 1)
