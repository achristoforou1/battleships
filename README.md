# BATTLESHIPS 2025!

Battleships 2025 is a Python terminal game which runs in the Code Institute mock terminal on Heroku.

Users can try to beat the computer by finding all of the computer's battleships before the computer finds theirs! Each battleship occupies one square on the board.

The live link can be found here - https://battleships2025-e85330e989f6.herokuapp.com/

![game preview on all different screen sizes](/assets/images/am_i_responsive.png)

## How to play

Battleships 2025 is based on the classic pen and paper game. You can read more about it on Wikipedia.

In this version, the player enters their name in the initial prompt which is immediately after the welcome message.

The two boards are then randomly generated.

The player can see where their ships are, indicated by an @ sign, but cannot see where the computer's ships are.

Guesses are marked on the board with an X. Hits are indicated by *.

The player and the computer then take turns making guesses and try to sink eachother's battleships.

The winner is the player who sinks all of their opponent's battleships first.

## Features

### Existing Features

- __Random board generation__

  - Ships are randomly placed on both the player and computer boards.
  - The player cannot see where the computer ships are.

  ![image of random boards generated](/assets/images/random_boards.png)

  - __Play against the computer__
  - __Accepts user input__
  - __Maintains scores after each round__
  - __Option given after each round to quit game or continue__

  ![image of a completed round by player and computer](/assets/images/round_image.png)

  - __Input validation and error-checking__
   - You cannot enter coordinates outside the size of the grid.
   - You must enter numbers.
   - You cannot enter the same guess twice.

   ![image of input validation](/assets/images/input_validation.png)

   - __Data maintained in class instances__

   ### Future Feaures

   - __Allow player to select the board size and number of ships__
   - __Allow player to position ships themselves__
   - __Have ships larger than 1x1__

   ## Data model

   I decided to use a Board class as my model. The game creates two instances of the Board class to hold the player's and computer's boards.

   The Board class stores the board size, the number of ships, the position of the ships, the guesses against that board and details such as the board type (player's board or computer) and the player's name.

   The class also has methods to help play the game, such as print method to print out the current board, an add_ships method to add ships tp the board and an add_guess method to add a guess and return the result.

   ## Testing

   I have manually tested this project ny doing the following:

   - __Passed the code through a PEP8 linter and confirmed there are no problems__
   - __Given invalid inputs: strings when numbers are expected, out of bounds inputs, same input twice__
   - __Tested in my local terminal and the Code Institute Heroku terminal__

   ## Bugs

   ### Solved bugs

   - __When i was writing the project and trying to run it I often encountered errors due to indentation which I eventually fixed__
   - __Due to the length of each line of code having to be under 80 characters I split some strings using the + sign and some print messages into multiple lines__
   - __In the make_guess function i was getting an error message when running the program after the continue in the if statement a break statement was also needed to come out of the loop__

   ### Remaining Bugs

   - __No bugs remaining__

   ### Validator testing

   - __PEP8__
    - For testing i used https://pep8ci.herokuapp.com/
    - All errors regarding lines were fixed with spliting the strings, breaking the print lines into multiple lines and also formatting using black.
    - One error has remained for trailing whitespace which I don't have the time to research. The other ones I managed to fix.

    ![image of PEP8 tesing](/assets/images/pep8_testing.png)





