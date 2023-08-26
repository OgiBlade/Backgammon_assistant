import numpy as np
from random import random
from player import Player 
from board import Board




board1 = np.zeros(26, dtype = int)
board1[1]  = -2
board1[6]  =  5
board1[8]  =  3
board1[12] = -5
board1[13] =  5
board1[17] = -3
board1[19] = -5
board1[24] =  2

#print(dice)
#for die in dice:
#    print(die)
#    print(white.genMoves(board.board, die,board.Bearing_off))
