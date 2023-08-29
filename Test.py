import numpy as np
from random import random
from board import Board
import operator



board1 = np.zeros(26, dtype = int)
board1[1]  = -2
board1[6]  =  5
board1[8]  =  3
board1[12] = -5
board1[13] =  5
board1[17] = -3
board1[19] = -5
board1[24] =  2

triple = (board1, -30, 159)
triple2 = (board1, 50, 153)
lista = []
lista.append(triple)
lista.append(triple2)
lista.append(triple2)
lista.append(triple2)
lista.append(triple2)
print(type(lista))
lista = sorted(lista, reverse = True, key = operator.itemgetter(1))
print(lista)
#print(dice)
#for die in dice:
#    print(die)
#    print(white.genMoves(board.board, die,board.Bearing_off))
