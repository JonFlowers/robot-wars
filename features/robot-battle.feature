Feature: Robot battle
    As a Robot Wars user
    I want to battle two robots
    So that one robot can take control of the location

    Scenario Outline: The robots do battle
      Given the Robot Wars app has been run "<robots>"
      And the Robot Wars arena has been set up "<arenainput>"
      And a Robot has been added to the arena "<robot1input>"
      And a Robot has been added to the arena "<robot2input>"
      And a Robot has been moved into an occupied location "<moverobotinput>"
      When I enter battle strategy "<strategy>"
      Then a battle outcome response is returned
      
      Examples: Move Robot
            |   robots  |   arenainput  |   robot1input  |   moverobotinput  |  robot2input  |  strategy  |
            |   2       |   8 8         |   2 2 S        |   MRM           |  1 1 N        |  1 |
            |   2       |   8 8         |   2 2 S        |   MRM           |  1 1 N        |  2 |