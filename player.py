import numpy as np
from random import randint, choice 


class Player():
    #inicijalizacija playera, u name ide b/w (black/white)
    def __init__(self, name, board):
        self.name = name
        self.board = board
    


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
                        for i in range(6, space+1, -1):
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
                        board2[25] +=1
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
                  
                    
                    board2[space+die] -=1
                    board2[space] += 1
                    new_states.append(board2)
        if(len(new_states) == 0):
            new_states.append(board)    
        return np.array(new_states)



    def Take_turn(self, player, dice, board):
        board2 = board
        moves = []
        niz2 = []
        possible_moves = []
        if len(dice) == 4:
            possible_moves_1 = []
            possible_moves_2 = []
            possible_moves_3 = []
            #racunanje svih mogucih poteza za double roll
            possible_moves_1.append(self.genMoves(board2, dice[0], self.Bearing_off(board2, player)))
            for j in range (len(possible_moves_1)):
                for table_n in possible_moves_1[j]:
                    niz2.append(table_n)
            possible_moves_1 = niz2
            
            niz2 = []
            
            for table_n in possible_moves_1:
                possible_moves_2.append(self.genMoves(table_n, dice[0], self.Bearing_off(table_n, player)))
            
            

            for j in range (len(possible_moves_2)):
                for table_n in possible_moves_2[j]:
                    niz2.append(table_n)
            
            possible_moves_2 = niz2
            niz2 = []
            

            for table_n in possible_moves_2:
                possible_moves_3.append(self.genMoves(table_n, dice[0], self.Bearing_off(table_n, player)))
            
            

            for j in range (len(possible_moves_3)):
                for table_n in possible_moves_3[j]:
                    niz2.append(table_n)
            
            possible_moves_3 = niz2
            niz2 = []


            for table_n in possible_moves_3:
                possible_moves.append(self.genMoves(table_n, dice[0], self.Bearing_off(table_n, player)))
            
          

            for j in range (len(possible_moves)):
                for table_n in possible_moves[j]:
                    niz2.append(table_n)
            
            possible_moves = niz2
            
            niz2 = []
            moves = possible_moves



            
            
            
        else:
            possible_moves_1 = []
            possible_moves_1_2 = []
            possible_moves_2 = []
            possible_moves_2_1 =[]
            #racunanje kombinacija prva,druga i druga, prva kockica, i stavljanje u niz
            possible_moves_1.append(self.genMoves(board2, dice[0], self.Bearing_off(board2, player)))
           
            

            for j in range (len(possible_moves_1)):
                for table_n in possible_moves_1[j]:
                    niz2.append(table_n)
                    nizshape = np.shape(niz2)
            possible_moves_1 = niz2
            niz2 = []
            
            for table_n in possible_moves_1:
                possible_moves_1_2.append(self.genMoves(table_n, dice[1], self.Bearing_off(table_n, player)))
            

            for j in range (len(possible_moves_1_2)):
                for table_n in possible_moves_1_2[j]:
                    niz2.append(table_n)
        
            possible_moves_1_2 = niz2
            niz2 = []
             


            possible_moves_2.append(self.genMoves(board2, dice[1], self.Bearing_off(board2, player)))
            for j in range (len(possible_moves_2)):
                for table_n in possible_moves_2[j]:
                    niz2.append(table_n)
            possible_moves_2 = niz2
            niz2 = []
            

            for table_n in possible_moves_2:
                possible_moves_2_1.append(self.genMoves(table_n, dice[0], self.Bearing_off(table_n, player)))
            

            for j in range (len(possible_moves_2_1)):
                for table_n in possible_moves_2_1[j]:
                    niz2.append(table_n)
            
            possible_moves_2_1 = niz2
            niz2 = []
        

            moves = possible_moves_1_2 + possible_moves_2_1
        

        
        
        return moves


def Board_init():
    board = np.zeros(26, dtype = int)
    board[1]  = -2
    board[6]  =  5
    board[8]  =  3
    board[12] = -5
    board[13] =  5
    board[17] = -3
    board[19] = -5
    board[24] =  2
    return board
#provera zavrsetka igre
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
    return Finish    
    #random generacija kockica, ako je isti broj na obe, racuna se kao 4
def DiceRoll():
        
    dice = [randint(1, 6), randint(1, 6)]
    if(dice[0] == dice[1]):
        dice.append(dice[0])
        dice.append(dice[0])
    print(dice)
    return dice

def bot_vs_bot():
    board = Board_init()
    i = 0
    player_1 = Player("w",board)
    player_2 = Player("b", board)
    dice = DiceRoll()
    while(len(dice)==4):
        dice = DiceRoll()
        
    if(dice[0]<dice[1]):
            player_1.name = "b"
            player_2.name = "w"

    print("Player 1: ")
    while(True):
        i+=1
        
        moves = []
        moves =player_1.Take_turn(player_1,dice, board)
        board = choice(moves)
        print(board)
        if(Finished(board, player_1) == True):
            print("Win for player 1!!")
            print("Game lasted ", i, "moves")
            return
        print("Player 2:")
        i+=1
        dice = DiceRoll()
        moves = []
        moves = player_2.Take_turn(player_2, dice, board)
        board = choice(moves)
        print(board)
        if(Finished(board, player_2) == True):
            print("Win for player 2!!")
            print("Game lasted ", i, "moves")
            return
        print("Player 1: ")
        dice = DiceRoll()
    
    return

        
         

bot_vs_bot()
