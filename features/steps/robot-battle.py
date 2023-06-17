from behave import *
from robotwarapp.controllers.robotwarcontroller import *

@given('a Robot has been moved into an occupied location "{moverobotinput}"')
def success_message(context, moverobotinput):
    context.response = context.app.handle_move_robot_input(0, moverobotinput)

@when('I enter battle strategy "{strategy}"')
def enter_strategy(context, strategy):
    context.response = context.app.handle_strategy_input(strategy)

@then('a battle outcome response is returned')
def battle_outcome_message(context):
    assert (context.response == "battle_finished")
