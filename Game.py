#Author:- Hoshner Tavadia
#Email:- hoshnertavadia@gmail.com/htavadia@my.yorku.ca

from Utilities import *
from os import system

def enterval():
        row = int(input("Enter Row Number(1-3): "))-1
        col = int(input("Enter Col Number(1-3): "))-1
        while(row>2 or row<0 or col>2 or col<0):
                print("\nInvalid Input Try Again")
                row = int(input("Enter Row Number(1-3): "))-1
                col = int(input("Enter Col Number(1-3): "))-1
        return row,col

def pvp():
    print("\nGAMEMODE: Player vs Player")
    state = ((' ',' ',' '),(' ',' ',' '),(' ',' ',' '))
    print("\nStarting Board")
    print_state(state)
    player1='x'
    player2='o'
    while(True):
        print('\nPlayer 1\'s turn')
        row,col = enterval()
        state = play(state,row,col,player1)
        print_state(state)    
        check_score = score_end(state)
        if check_score == 1:
            print("\n-GAME OVER-")
            print("---Player 1 wins!---")
            break
        elif check_score == -1:
            print("\n-GAME OVER-")
            print("---Player 2 wins!---")
            break
        if check_score == 0:
            print("\n-GAME OVER-")
            print("---Draw---")
            break
        
        print('\nPlayer 2\'s turn')
        row,col = enterval()
        state = play(state,row,col,player2)
        print_state(state)    
        check_score = score_end(state)
        if check_score == 1:
            print("\n-GAME OVER-")
            print("---Player 1 wins!---")
            break
        elif check_score == -1:
            print("\n-GAME OVER-")
            print("---Player 2 wins!---")
            break
        if check_score == 0:
            print("\n-GAME OVER-")
            print("---Draw---")
            break
    input()
    system('CLS')
    main()

    
def pvc():
    print("\nGAMEMODE: Player vs Computer")
    state = ((' ',' ',' '),(' ',' ',' '),(' ',' ',' '))
    print("\nStarting Board")
    print_state(state)
    player='x'
    computer='o'
    while(True):
        print('\nPlayer\'s turn')
        row,col = enterval()
        state = play(state,row,col,player)
        print_state(state)    
        check_score = score_end(state)
        if check_score == 1:
            print("\n-GAME OVER-")
            print("---Player wins!---")
            break
        elif check_score == -1:
            print("\n-GAME OVER-")
            print("---Computer wins!---")
            break
        if check_score == 0:
            print("\n-GAME OVER-")
            print("---Draw---")
            break
        
        print('\nComputer\'s turn')
        move= score(state,computer)[1]
        state = play(state, move[0], move[1], computer)
        print_state(state)    
        check_score = score_end(state)
        if check_score == 1:
            print("\n-GAME OVER-")
            print("---Player wins!---")
            break
        elif check_score == -1:
            print("\n-GAME OVER-")
            print("---Computer wins!---")
            break
        if check_score == 0:
            print("\n-GAME OVER-")
            print("---Draw---")
            break
    input()
    system('CLS')
    main()

    
def cvc():
    print("\nGAMEMODE: Computer vs Computer")
    state = ((' ',' ',' '),(' ',' ',' '),(' ',' ',' '))
    print("\nStarting Board")
    print_state(state)
    computer1='x'
    computer2='o'
    while(True):
        print('\nComputer 1\'s turn')
        move= score(state,computer1)[1]
        state = play(state, move[0], move[1], computer1)
        print_state(state)    
        check_score = score_end(state)
        if check_score == 1:
            print("\n-GAME OVER-")
            print("---Computer 1 wins!---")
            break
        elif check_score == -1:
            print("\n-GAME OVER-")
            print("---Computer 2 wins!---")
            break
        if check_score == 0:
            print("\n-GAME OVER-")
            print("---Draw---")
            break    
        print('\nComputer 2\'s turn')
        move= score(state,computer2)[1]
        state = play(state, move[0], move[1], computer2)
        print_state(state)    
        check_score = score_end(state)
        if check_score == 1:
            print("\n-GAME OVER-")
            print("---Computer 1 wins!---")
            break
        elif check_score == -1:
            print("\n-GAME OVER-")
            print("---Computer 2 wins!---")
            break
        if check_score == 0:
            print("\n-GAME OVER-")
            print("---Draw---")
            break
    input()
    system('CLS')
    main()


def main():
    print("Welcome To Cross And Naughts Game")
    print("""\nRULES:

1. The game is played on a grid that's 3 squares by 3 squares.
2. You are X, your friend (or the computer) is O. Players take turns putting their marks in empty squares.
3. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.
4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.
5. Player choses their mark by inputing the row and col of its mark (range 1-3).


GAMEMODES:
1.Player vs Player
2.Player vs Computer
3.Computer vs Computer
4.Exit Program""")
    inp = input("Enter The Number To Choose Your Gamemode : ")
    inp = int(inp)
    if (inp==1):
        pvp()
    elif (inp==2):
        pvc()
    elif (inp==3):
        cvc()
    elif (inp==4):
        exit()
    else:
        print("Invalid Input, Try Again\n")
        input()
        system('CLS')
        main()

if __name__ == "__main__":
    main()
