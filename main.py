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

board1 = board()
itertj = iter(board1.coords1)
def print_board():
    a = 0
    while True:
        a += 1
        print(next(itertj))
        if a > 9:
            break
