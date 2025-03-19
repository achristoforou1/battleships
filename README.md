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
   
