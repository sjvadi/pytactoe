from enum import Enum

class board(object):
    coords1 = [[0,0,0],[0,0,0],[0,0,0]]
    def __init__(self):
        print("board generated")
    def make_move(self, move):
        self.coords1[move.coords[0]][move.coords[1]] = move.color
class move:
    def __init__(self, color, coords):
        self.color = color
        self.coords = coords
class color(Enum):
    CROSS = 1
    CIRCLE = 2
if __name__ == "__main__":
    game_over = True
    game_loop()

def game_loop():
    while True:
        #handle input
        #make changes to the board
        #switch colors
        #check if game over
        if game_over:
            break

def handle_input():
    if current_color == color.CROSS:
        print("Cross' turn")
    else: 
        print("Circle's turn")
    #get input
    #apply the changes to board
itertj = iter(board1.coords1)
def print_board():
    a = 0
    while True:
        a += 1
        print(next(itertj))
        if a > 9:
            break
