class Board:
    """
    Main board class. Sets board size, number of ships, player name and board tyoe (player or computer)
    Has methods for adding ships and guesses and printing the board.
    """
def __init__(self, size, num_ships, name, type):
    self.size = size
    self.board = [("5" for x in range (size) for y in range (size))]
    self.num_ships = num_ships
    self.name = name
    self.type = type
    self.guesses = []
    self.ships = []

def print(self):
    for row in self.board:
        print("". join(row))

def guess(self,x,y):
    self.guesses.append(x,y)
    self.board [x][y] = "x"

    if (x,y) in self.ships:
        self.board[x][y] = ""
        return "Hit"
    else:
        return "Miss"
    
