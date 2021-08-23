import numpy as np
def print_state(state):
    """Prints the state."""
  
    for i in range(len(state)):
        print(state[i][0],"|",state[i][1],"|",state[i][2],sep="")
       
def score_end(state):
    """Scores the game state if the game has ended, otherwise returns None."""
    emptyslot = -1
    def checkiffull(state):   
        for row in state:     
            z = row.count(" ")
            if z>0:           
                return 0
        if z==0:
            return 1
    def game_state(state):
        plays=[]
        for row in state:   
            for x in row:
                plays.append(x)
        if (plays[0]==plays[1]==plays[2]):
            if plays[0]=="x":
                return 1
            elif plays[0]=="o":
                return -1
        elif (plays[3]==plays[4]==plays[5]):
            if plays[3]=="x":
                return 1
            elif plays[3]=="o":
                return -1
        elif (plays[6]==plays[7]==plays[8]):
            if plays[6]=="x":
                return 1
            elif plays[6]=="o":
                return -1
        elif (plays[0]==plays[4]==plays[8]):
            if plays[0]=="x":
                return 1
            elif plays[0]=="o":
                return -1
        elif (plays[2]==plays[4]==plays[6]):
            if plays[6]=="x":
                return 1
            elif plays[6]=="o":
                return -1
        elif (plays[0]==plays[3]==plays[6]):
            if plays[6]=="x":
                return 1
            elif plays[6]=="o":
                return -1
        elif (plays[1]==plays[4]==plays[7]):
            if plays[1]=="x":
                return 1
            elif plays[1]=="o":
                return -1
        elif (plays[2]==plays[5]==plays[8]):
            if plays[2]=="x":
                return 1
            elif plays[2]=="o":
                return -1
        else:
            return 0
        
    def print_result(gamestate, check):             
        if gamestate == 1:
            return 1
        elif gamestate == -1:
            return -1
        elif(gamestate==0 and check ==1):
            return 0
        elif(gamestate==0 and check ==0):
            return None
        
            
    x=checkiffull(state)
    y=game_state(state)
    z=print_result(y,x)
    return z

def play(state, row, col, mark):
    """Returns a new state after the given move has been played."""
    new_state = [] 
    for i in range(len(state)):
        row_state = []
        for j in range(len(state)):
            if i==row and j == col:
                row_state.append(mark)
            else:
                row_state.append(state[i][j])
        new_state.append(tuple(row_state))
    return tuple(new_state)



def moves(state):
    """Returns the list of moves that are avaliable from the current state."""
    
    move_list=[]
    for i in range(len(state)):
        for j in range(len(state)):
            if state[i][j]==' ':
                move_list.append((i,j))
    return move_list

def score(state, player):
    """Given the game state and whose turn it is returns a tuple (estimated game score, best move to play)"""
    
    # **************************************************************** (3 marks)
    #pass
    check_score = score_end(state)
    if check_score != None:
        return check_score,None
    
    best_moves=[]
    scores = []
    
    for empty_cell in moves(state):
        
        curr_state = play(state, empty_cell[0], empty_cell[1], player)
        
        if player=='x':
            curr_score = score(curr_state, 'o')
            scores.append(curr_score[0])
            
        else:
            curr_score = score(curr_state, 'x')
            scores.append(curr_score[0])
            
        best_moves.append(empty_cell)
        
        
    if player == 'x':   
        max_score_index = scores.index(max(scores))
        best_move = best_moves[max_score_index]
        return (max(scores),best_move)
    
    else:
        max_score_index = scores.index(min(scores))
        best_move = best_moves[max_score_index]
        return (min(scores),best_move)
               
   


