Feature: Move another Robot
    As a Robot Wars user,
    I want to move another Robot around the Robot War arena,
    So that I can do battle.
    
    Scenario Outline: The Robot moves into an occupied location
    Given the Robot Wars app has been run "<robots>"
    And the Robot Wars arena has been set up "<arenainput>"
    And a Robot has been added to the arena "<robot1input>"
    And a Robot has been added to the arena "<robot2input>"
    When I enter move robot commands "<moverobotinput>"
    Then a robot attacked response is returned
    And the robot has stopped in the occupied location
    
    Examples: Move Robot
        |   robots  |   arenainput  |   robot1input  |   moverobotinput  |  robot2input  |
        |   2       |   8 8         |   2 2 S        |   MRMRM           |  1 1 N        |