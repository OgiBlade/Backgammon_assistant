import numpy as np
from random import randint
#privremeno je tabla ovde kasnije se pomera
board1 = np.zeros(26, dtype = int)
'''board1[1]  = -2
board1[6]  =  5
board1[8]  =  3
board1[12] = -5
board1[13] =  5
board1[17] = -3
board1[19] = -5
board1[24] =  2
'''






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















