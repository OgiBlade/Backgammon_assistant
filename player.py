import numpy as np
from random import randint
#privremeno je tabla ovde kasnije se pomera

board1 = np.zeros(26, dtype = int)
board1[1]  = -2
board1[6]  =  5
board1[8]  =  3
board1[12] = -5
board1[13] =  5
board1[17] = -3
board1[19] = -5
board1[24] =  2







class Player():
    #inicijalizacija playera, u name ide b/w (black/white)
    def __init__(self, name, board):
        self.name = name
        self.board = board
    
    #random generacija kockica, ako je isti broj na obe, racuna se kao 4
    def DiceRoll(self):
        
        dice = [randint(1, 6), randint(1, 6)]
        if(dice[0] == dice[1]):
            dice.append(dice[0])
            dice.append(dice[0])
        print(dice)
        return dice

#provera da li igrac moze da izbacuje iz igre zetone

    def Bearing_off(self, board, player):
        index = np.nonzero(board)
        bearing = True
        if(player.name == "w"):
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


    def genMoves(self, board, die, bearing):
        index = np.nonzero(board)
        if(self.name == "w"):
            bar = board[25]
        else:
            bar = board[0]
      
        new_states = []
        for space in index[0]:
            
            board2 = np.copy(board)
            



            if(self.name== "w"):
                #ako beli ima zeton na bar-u
                if bar>0:
                    if (board2[space] >0 and board2[25-die] == -1):
                        board2[25-die] = 1
                        board2[0]+=1
                        board2[25]-=1
                        new_states.append(board2)
                    elif (board2[space] >0 and board2[25-die]>= 0):
                        board2[25-die] += 1
                        board2[25]-=1
                        new_states.append(board2)
                    elif (board2[space] >0):
                        new_states.append(board2)
                #ako beli moze da uzme crni zeton
                elif (board2[space] >0 and  space - die >0 and board2[space-die] == -1):
                    board2[space-die] = 1
                    board2[space]-=1
                    board2[0] +=1
                    new_states.append(board2)
                #beli zavrsava igru
                elif (bearing == True and board2[space] >0):
                    if (space-die > 0):
                        board2[space-die] +=1
                        board2[space] -=1
                        new_states.append(board2)
                    elif (space==die):
                        board2[space]-=1
                        new_states.append(board2)

                    else:
                        test = True
                        for i in range(6, space, -1):
                            if (board2[i]>0):
                                test = False
                        
                        if (test == True ):
                            board2[space]-=1
                        new_states.append(board2)



                #normalan potez
                elif(board2[space]>0 and  space - die >0 and board2[space-die] >= 0):
                    board2[space-die] +=1
                    board2[space] -= 1
                    new_states.append(board2)




            if(self.name== "b"):
                #ako crni ima zetone na baru
                
                if bar>0:
                    
                    if board2[0+die] == 1:
                        board2[0+die] = -1
                        board2[25]+=1
                        board2[0]-=1
                        new_states.append(board2)
                    elif  board2[0+die]<= 0:
                        board2[0+die] -= 1
                        board2[0]-=1
                        new_states.append(board2)
                    else:
                        new_states.append(board2)
                #ako crni moze da uzme belog
                elif (board2[space] <0 and  space + die <25 and board2[space+die] == 1):
                        
                       
                        board2[space+die] = -1
                        board2[space]+= 1
                        board2[0] +=1
                        new_states.append(board2)
                #crni zavrsava
                elif (bearing == True and board2[space] <0):
                    
                    if (space+die < 25):
                        
                        board2[space+die] -=1
                        board2[space] +=1
                        new_states.append(board2)
                    elif (space+die== 25):
                        
                        board2[space]+=1
                        new_states.append(board2)

                    else:
                        
                        test = True
                        for i in range(18, space, 1):
                            if (board2[i]<0):
                                test = False
                        
                        if (test):
                            board2[space]+=1
                        new_states.append(board2)

                
                #normalan potez
                elif(board2[space]<0 and  space + die <25 and board2[space+die] <= 0):
                  
                    
                    board2[space-die] -=1
                    board2[space] += 1
                    new_states.append(board2)
        return np.array(new_states)



    def Take_turn(self, player, dice, board):
        board2 = self.board
        possible_moves = []
        if len(dice) == 4:
            possible_moves_1 = []
            possible_moves_2 = []
            possible_moves_3 = []

            possible_moves_1.append(self.genMoves(board2, dice[0], self.Bearing_off))
            for table_n in possible_moves_1[0]:
                possible_moves_2.append(self.genMoves(table_n, dice[0], self.Bearing_off))
            for i in range (len(possible_moves_2)):
                for table_n in possible_moves_2[i]:
                    possible_moves_3.append(self.genMoves(table_n, dice[0], self.Bearing_off))
            for i in range (len(possible_moves_3)):
                for table_n in possible_moves_3[i]:
                        possible_moves.append(self.genMoves(table_n, dice[0], self.Bearing_off))
            
        else:
            possible_moves_1 = []
            possible_moves_2 = []
            possible_moves_1.append(self.genMoves(board2, dice[0], self.Bearing_off))
            for table_n in possible_moves_1[0]:
                possible_moves.append(self.genMoves(table_n, dice[1], self.Bearing_off))
            
            possible_moves_2.append(self.genMoves(board2, dice[0], self.Bearing_off))
            for table_n in possible_moves_1[0]:
                possible_moves.append(self.genMoves(table_n, dice[1], self.Bearing_off))
            


        return possible_moves
        
        

x = Player("w", board1)

#print(dice)
niz = x.Take_turn(x,x.DiceRoll(), x.board)
print(niz)












