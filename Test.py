import numpy as np
from random import random
from player import Player 
from board import Board


board = Board()
white = Player("w", board.board)
black = Player("b", board.board)

dice = white.DiceRoll()
#print(dice)
for die in dice:
    print(die)
    print(white.genMoves(board.board, die,board.Bearing_off))
