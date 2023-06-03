Feature: Set up another Robot
    As a Robot Wars user,
    I want to add another Robot to the Robot War arena,
    So that I have another Robot to battle with.

    Scenario Outline: Set the Robot's position and orientation
        Given the Robot Wars app has been run "<robots>"
        And the Robot Wars arena has been set up "<arenainput>"
        And a Robot has been added to the arena "<robotinput>"
        And the Robot has been moved "<moverobotinput>"
        When I enter robot input "<anotherrobotinput>"
        Then a robot ready response is returned

        Examples: Arena and Robot coordinates
            |   robots  | arenainput | robotinput   |   moverobotinput  |   anotherrobotinput   |
            |   2       | 4 4        |   1 1 N      |   MMRMM           |   2 2 N               |