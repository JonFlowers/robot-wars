Feature: Set up a Robot
    As a Robot Wars user,
    I want to add a Robot to the Robot War arena,
    So that I have a Robot to battle with.

    Scenario Outline: Set the Robot's position and orientation
        Given the Robot Wars app has been run "<robots>"
        And the Robot Wars arena has been set up "<arenainput>"
        When I enter robot input "<robotinput>"
        Then a robot ready response is returned

        Examples: Arena and Robot coordinates
            |   robots  | arenainput | robotinput   |
            |   1       | 5 5        |   1 2 N      |
            |   1       | 8 8        |   4 3 E      |
            |   1       | 12 10      |   3 3 S      |
            |   1       | 9 9        |   9 9 W      |

    Scenario Outline: Enter invalid Robot details
        Given the Robot Wars app has been run "<robots>"
        And the Robot Wars arena has been set up "<arenainput>"
        When I enter robot input "<robotinput>"
        Then an invalid robot input error is returned

        Examples: Arena and Robot coordinates
            |   robots  | arenainput | robotinput   |
            |   1       | 5 5        |   12N        |
            |   1       | 8 8        |   1 2 R      |
            |   1       | 4 4        |   3 3 X      |
            |   1       | 4 4        |   3 3 6 N    |
            |   1       | 14 14      |   3 E N      |

    Scenario Outline: Robot is out of bounds of the arena
        Given the Robot Wars app has been run "<robots>"
        And the Robot Wars arena has been set up "<arenainput>"
        When I enter robot input "<robotinput>"
        Then a robot out of bounds error is returned

        Examples: Arena and Robot coordinates
            |   robots  | arenainput | robotinput   |
            |   1       | 5 5        |   6 6 N      |
            |   1       | 8 8        |   10 4 E     |
            |   1       | 4 4        |   3 6 S      |
            |   1       | 4 4        |   4 5 N      |
            |   1       | 14 14      |   16 20 N    |
    
    Scenario Outline: Add a Robot before the arena has been set up
        Given the Robot Wars app has been run "<robots>"
        And the Robot Wars arena has not been set up
        When I enter robot input "<robotinput>"
        Then an arena has not been set up error is returned

        Examples: Arena and Robot coordinates
            |   robots  | robotinput    |
            |   1       |   4 6 N       |