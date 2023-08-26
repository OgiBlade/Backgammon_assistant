import numpy as np
from  random import random
from player import Player 

class Board():


    #pocetno stanje, beli su +, crni su -
    def __init__(self):
        board = np.zeros(26, dtype = int)
        board[1]  = -2
        board[6]  =  5
        board[8]  =  3
        board[12] = -5
        board[13] =  5
        board[17] = -3
        board[19] = -5
        board[24] =  2
        self.board = board

    #provera da li je igrac zavrsio
    def Finished(board, Player):
        index = np.nonzero(board)
        Finish = True
        if(Player.name == "w"):
            for space in index[0]:
                if(board[space]>0):
                    Finish = False
                    break
        
        else:
            for space in index[0]:
                if(board[space] <0):
                    Finish = False
                    break


    #provera da li igrac moze da izbacuje iz igre zetone
    def Bearing_off(board, Player):
        index = np.nonzero(board)
        bearing = True
        if(Player.name == "w"):
            for space in index[0]:
                if(space>6 and board[space] > 0):
                    bearing = False
                    break
        
        else:
            for space in index[0]:
                if(space <19 and board[space]<0):
                    bearing = False
                    break


        return bearing

        
