Feature: Move a Robot
    As a Robot Wars user,
    I want to move a Robot around the Robot War arena,
    So that I can do battle.

    Scenario Outline: Enter valid move commands
        Given the Robot Wars app has been run "<robots>"
        And the Robot Wars arena has been set up "<arenainput>"
        And a Robot has been addedd to the arena "<robotinput>"
        When I enter move robot commands "<moverobotinput>"
        Then a robot moved response is returned

        Examples: Move Robot
        |   robots  |   arenainput  |   robotinput  |   moverobotinput  |
        |   1       |   8 8         |   2 2 N       |   MMRMMLMM        |

    Scenario Outline: Enter invalid move commands
        Given the Robot Wars app has been run "<robots>"
        And the Robot Wars arena has been set up "<arenainput>"
        And a Robot has been addedd to the arena "<robotinput>"
        When I enter move robot commands "<moverobotinput>"
        Then an invalid move robot input error is returned  

        Examples: Move Robot
        |   robots  |   arenainput  |   robotinput  |   moverobotinput  |
        |   1       |   5 5         |   2 2 N       |   RTLRMXJE        |

    Scenario Outline: Robot moves beyond the bounds of the arena
        Given the Robot Wars app has been run "<robots>"
        And the Robot Wars arena has been set up "<arenainput>"
        And a Robot has been addedd to the arena "<robotinput>"
        When I enter move robot commands "<moverobotinput>"
        Then a robot moved out of bounds error is returned   

        Examples: Move Robot
        |   robots  |   arenainput  |   robotinput  |   moverobotinput  |
        |   1       |   5 5         |   2 2 N       |   MMLMMMMR        | 