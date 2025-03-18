import random

class Board:
    """
    Main board class. Sets board size, number of ships, player name and board tyoe (player or computer)
    Has methods for adding ships and guesses and printing the board.
    """
    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [["." for _ in range (size)] for _ in range (size)]#Creation of blank board
        self.num_ships = num_ships
        self.name = name #Player name/Computer
        self.type = type # Player or computer board type
        self.guesses = set() #Coordinates that have been used
        self.ships = set() #Ship coordinates

    def print_board(self, hide_ships = False):#Computer board with computer ships hidden
        print(f"{self.name}'s Board:")
        for row in self.board:
            print("". join(row))
        print()

    def guess(self,x,y):#Processing attack attempts
        self.guesses.add((x,y))
        if (x,y) in self.ships:
            self.board [x][y] = "*"#Hit
            return "Hit!"
        else:
            self.board[x][y]= "X"#Miss
            return "Miss!"


   
    
def add_ship(self, x, y):# Ship addition to board
    if len(self.ships) >= self.num_ships:
        print("Error:You cannot add any more ships")
    else:
        self.ships.add((x,y))
        if self.type == "player":
            self.board [x][y] = "@" #Showing the ships only for the player

def random_point(size, excluded_points):
    #Creates random position that isn't in excluded_points
    while True:
        x, y = random.randint (0,size -1), random.randint (0,size -1)
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
                print(f"Invalid input! Please enter a number between 0 and {board.size - 1}.")
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
            #Check for re used cordinates
            if (x, y) in defender_board.guesses:
                print("You've already guessed this coordinate! Try again.")
                continue
        else:
            #Automatic computer move
            x, y = random_point(defender_board.size, defender_board.guesses)
        

def play_game(computer_board, player_board):
    while True:
        #player turn
        print("/nPlayer's turn:")
        x, y, result = make_guess(player_board, computer_board)
        print(f"Player guessed: ({x}, {y})")
        print("Player hit a ship!" if result == "Hit!" else "Player missed this time!")

    
def new_game():
    """
    Starts new game. Sets the board size and number of ships,
    resets the scores and initializes the boards.
    """
    size = 5
    num_ships = 4
    scores ["computer"] = 0
    scores ["player"] = 0
    print ("-" * 35)
    print ("Welcome to Ultimate Battleships")
    print (f"Board Size: {size}. Number of ships:{num_ships}")
    print ("Top left corner is row: 0, col: 0")
    print ("-" * 35)
    player_name = input("Please enter your name: \n")
    print ("-" * 35)

computer_board = Board(size,num_ships,"Computer", type = "computer")
player_board = Board (size, num_ships, player_name, type = "player")

for _ in range(num_ships):
    populate_board(player_board)
    populate_board(computer_board)

play_game(computer_board, player_board)

new_game()