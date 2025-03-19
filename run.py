import random
import sys


class Board:
    """
    Main board class. Sets board size, number of ships, player name and board
    type (player or computer)
    Has methods for adding ships and guesses and printing the board.
    """

    def __init__(self, size, num_ships, name, board_type):
        self.size = size
        self.board = [
            ["." for _ in range(size)] for _ in range(size)
        ]  # Creation of blank board
        self.num_ships = num_ships
        self.name = name  # Player name/Computer
        self.type = board_type  # Player or computer board type
        self.guesses = set()  # Coordinates that have been used
        self.ships = set()  # Ship coordinates

    def print_board(
        self, hide_ships=False
    ):  # Computer board with computer ships hidden
        print(f"{self.name}'s Board:")
        for row in self.board:
            print(" ".join(row))
        print()

    def guess(self, x, y):  # Processing attack attempts
        self.guesses.add((x, y))
        if (x, y) in self.ships:
            self.board[x][y] = "*"  # Hit
            return "Hit!"
        else:
            self.board[x][y] = "X"  # Miss
            return "Miss!"

    def add_ship(self, x, y):  # Ship addition to board
        if len(self.ships) >= self.num_ships:
            print("Error:You cannot add any more ships")
        else:
            self.ships.add((x, y))
            if self.type == "player":
                self.board[x][y] = "@"  # Showing the ships only for the player


def random_point(size, excluded_points):
    # Creates random position that isn't in excluded_points
    while True:
        x, y = random.randint(0, size - 1), random.randint(0, size - 1)
        if (x, y) not in excluded_points:
            return x, y


def get_valid_input(prompt, board):
    """
    Validates coordinates that have been input and makes sure
    they are not outside the board scope
    """
    while True:
        try:
            value = int(input(prompt))
            if 0 <= value < board.size:
                return value
            else:
                print(
                    f"Invalid input! Please enter a number between "
                    + f"0 and {board.size - 1}."
                )
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def make_guess(attacker_board, defender_board):
    """
    Processes the guesses. If player guess then prompt for input.
    If comp guess, random row and column, exactly the same as when
    populating the board
    """
    while True:
        if attacker_board.type == "player":
            x = get_valid_input("Enter row:", attacker_board)
            y = get_valid_input("Enter column:", attacker_board)
            # Check for re used cordinates
            if (x, y) in defender_board.guesses:
                print("You've already guessed this coordinate! Try again.")
                continue
            break
        else:
            # Automatic computer move
            x, y = random_point(defender_board.size, defender_board.guesses)

            break

    result = defender_board.guess(x, y)

    return x, y, result


def play_game(computer_board, player_board):
    while True:
        # player turn
        print("\nPlayer's turn:")
        x, y, result = make_guess(player_board, computer_board)
        print(f"Player guessed: ({x}, {y})")
        print(
            "Player hit a ship!" if result == "Hit!"
            else "Player missed this time!"
        )         
        # Check for player win and game restart
        if computer_board.ships.issubset(
            computer_board.guesses
        ):  # check computer board
            print("\nPlayer wins!")
            choice2 = input(
                "\nEnter any key to restart a game or 'n' to exit: "
            )
            if choice2.lower() == "n":
                print("Game exited. Goodbye!")
                sys.exit()
            else:
                new_game()
        # Computer's turn
        print("\nComputer's turn:")
        cx, cy, cresult = make_guess(computer_board, player_board)
        print(f"Computer guessed: ({cx}, {cy})")
        print(
            "Computer hit a ship!"
            if cresult == "Hit!"
            else "Computer missed this time!"
        )

        # Check for computer win and game restart
        if player_board.ships.issubset(player_board.guesses):
            print("\nComputer wins!")
            choice2 = input(
                "\nEnter any key to restart a game or 'n' to exit: "
            )
            if choice2.lower() == "n":
                print("Game exited. Goodbye!")
                sys.exit()
            else:
                new_game()

        # Score print and exit option
        print("\n------------------------------------")
        player_score = len(computer_board.guesses & computer_board.ships)
        computer_score = len(player_board.guesses & player_board.ships)
        print(
            f"After this round, the scores are:\nPlayer: {player_score}\n"
            f"Computer: {computer_score}"
        )
        print("------------------------------------")

        choice = input("\nEnter any key to continue or 'n' to exit: ")
        if choice.lower() == "n":
            print("Game exited. Goodbye!")
            sys.exit()

        # Boards update
        print("\nCurrent Boards:")
        player_board.print_board()
        computer_board.print_board(hide_ships=True)


def new_game():
    """
    Starts new game. Sets the board size and number of ships,
    resets the scores and initializes the boards.
    """
    size = 5
    num_ships = 4
    print("-" * 35)
    print("Welcome to Ultimate Battleships")
    print(f"Board Size: {size}. Number of ships:{num_ships}")
    print("Top left corner is row: 0, col: 0")
    print("-" * 35)
    player_name = input("Please enter your name: \n")
    print("-" * 35)

    # Board variables from board class
    computer_board = Board(size, num_ships, "Computer", "computer")
    player_board = Board(size, num_ships, player_name, "player")

    # Ship positioning for both boards
    for _ in range(num_ships):
        x, y = random_point(size, player_board.ships)
        player_board.add_ship(x, y)
        x, y = random_point(size, computer_board.ships)
        computer_board.add_ship(x, y)

    print("Initial Boards:")
    player_board.print_board()

    # Hide computer ships
    computer_board.print_board(hide_ships=True)

    play_game(computer_board, player_board)


new_game()
