Feature: Set up the Robot Wars arena
    As a Robot Wars user,
    I want to set the upper right coordinates of the arena,
    So that I have a bounded arena for my robots to battle in.

    Scenario Outline: Set the bounds of the arena
        Given the Robot Wars app has been run "<robots>"
        When I enter arena input "<arenainput>"
        Then an arena ready response is returned
    
        Examples: Arena coordinates
            |   robots  | arenainput    |
            |   1       | 5 5           |
            |   1       | 8 4           |

    Scenario Outline: Invalid input is entered
        Given the Robot Wars app has been run "<robots>"
        When I enter arena input "<arenainput>"
        Then an invalid arena input error is returned

        Examples: Invalid arena coordinates
            |   robots  |   arenainput      |
            |   1       |   55r             |
            |   1       |   r e             |
            |   1       |   -5 0            |

