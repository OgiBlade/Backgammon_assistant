import numpy as np
from random import randint, choice 


bar_value = 25
end_zone_value = -5
solo_value = -10
extra_value = 2

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
                
                elif (board2[space] >0 and  (space - die) >0 and board2[space-die] == -1):
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
                elif(board2[space]>0 and  (space - die) >0 and board2[space-die] >= 0):
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


def Solo(player, board, space_id):
    solo = False
    index = np.nonzero(board)
    if(player == "w"):
        for space in index[0]:
            if(board[space] < 0):
                solo = True
                return solo
    
    if(player == "b"):
        for space in index[0]:
            if(board[space] > 0):
                solo = True
                return solo
    
    return solo
            
                

def Calc_Rewards(player, board):
    reward = 0
    pip = 0
    if player.name == "w":
        if(board[25] != 0):
            reward -= board[25] * bar_value
        if(board[0] != 0):
            reward += board[0] * bar_value


#        for space in board[1:7]:
#            reward += end_zone_value
#        for space in board[19:25]:
#            reward -= end_zone_value

        index = np.nonzero(board)
        for space in index[0]:
            if board[space]== 1:
                if(Solo("w", board, space)):
                    reward += solo_value
            if board[space] >0:
                pip+=space * board[space]
                reward += extra_value * (space // 6 + 1)
                
    
    if player.name == "b":
        if(board[25] != 0):
            reward += board[25] * bar_value
        if(board[0] != 0):
            reward -= board[0] * bar_value


        for space in board[1:7]:
            reward -= end_zone_value
        for space in board[19:25]:
            reward += end_zone_value

        index = np.nonzero(board)
        for space in index[0]:
            if board[space]== -1:
                if(Solo("b", board, space)):
                    reward += solo_value
            if board[space] <0:
                pip += abs((space -25) *board[space])


    return reward, pip
        





def Board_Rewards(player, moves):
    Rewards = []
    Pips    = []
    board_and_rewards = []
    for space in moves:
        Reward, pip = Calc_Rewards(player, space)
        triple = (space, Reward, pip)
        board_and_rewards .append(triple)
    board_and_rewards = sorted(board_and_rewards,reverse=True, key=lambda x: (x[1]))
    print(board_and_rewards)
    return board_and_rewards[0][0]
    
    

    


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

def DicePlayer():
    dice = []
    die_1, die_2 = int(input()), int(input())
    
    dice.append(die_1)
    dice.append(die_2)
    if(dice[0] == dice[1]):
        dice.append(dice[0])
        dice.append(dice[0])
    return dice


def input_move(player, board, double):
    if(player.name == "b"):
        start, end = int(input()), int(input())
        start = abs(start-25)
        end   = abs(end - 25)
        if(start==0):
            board[start] -=1
        else:
            board[start]+=1
        if(board[end] == 1):
            board[25]+=1
            board[end] -= 1
        board[end]  -=1
        start, end = int(input()), int(input())
        start = abs(start-25)
        end   = abs(end - 25)
        if(start==0):
            board[start] -=1
        else:
            board[start]+=1
        if(board[end] == 1):
            board[25]+=1
            board[end] -= 1
        board[end]  -=1
        if(double == 1):
            start, end = int(input()), int(input())
            start = abs(start-25)
            end   = abs(end - 25)
            if(start==0):
                board[start] -=1
            else:
                board[start] +=1
            if(board[end] == 1):
                board[25]+=1
                board[end] -= 1
            board[end]  -=1
            start, end = int(input()), int(input())
            start = abs(start-25)
            end   = abs(end - 25)
            if(start==0):
                board[start] -=1
            else:
                board[start] +=1
            if(board[end] == 1):
                board[25]+=1
                board[end] -= 1
            board[end]  -=1
    return board



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
        board = Board_Rewards(player_1, moves)
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
        board = Board_Rewards(player_2, moves)
        print(board)
        if(Finished(board, player_2) == True):
            print("Win for player 2!!")
            print("Game lasted ", i, "moves")
            return
        print("Player 1: ")
        dice = DiceRoll()
    
    return

def player_vs_player():
    board = Board_init()
    i = 0
    player_1 = Player("w",board)
    player_2 = Player("b", board)
    dice = DicePlayer()
    while(len(dice)==4):
        dice = DicePlayer()
        
    if(dice[0]<dice[1]):
            player_1.name = "b"
            player_2.name = "w"

    print("Player 1: ")
    while(True):
        i+=1
        if(player_1.name == "b"):
            board = input_move(player_1, board, int(int(input())))
        else:
            moves = []
            moves =player_1.Take_turn(player_1,dice, board)
            board = Board_Rewards(player_1, moves)
        print(board)
        if(Finished(board, player_1) == True):
            print("Win for player 1!!")
            print("Game lasted ", i, "moves")
            return
        print("Player 2:")
        i+=1
        if(player_2.name == "b"):
            board = input_move(player_2, board, int(int(input())))
        else:
            dice = DicePlayer()
            moves = []
            moves = player_2.Take_turn(player_2, dice, board)
            board = Board_Rewards(player_2, moves)
        print(board)
        if(Finished(board, player_2) == True):
            print("Win for player 2!!")
            print("Game lasted ", i, "moves")
            return
        print("Player 1: ")
        if(player_1.name == "w"):
            dice = DicePlayer()

         

player_vs_player()
