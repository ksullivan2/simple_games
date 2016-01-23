
import random

#if 0 then it's the comp's turn


def define_board():
    board =  []
    boardsize = int
    valid = False
    while valid == False:
        try:
            boardsize = int(input("How many cells per row and column? 3, 5, or 7?"))
        except (ValueError):
            print ("That was not an integer.")
        if boardsize in [3,5,7]:
            valid = True
            break
        print ("Try again, smart-ass.")
            
    for i in range(boardsize):
        board.append(["_"]*boardsize)
    return board

def print_board(board):
    for row in board:
        row = " ".join(row)
        print(row)
    print()

def comp_move(board):
    x = random.randint(0,len(board)-1)
    y = random.randint(0,len(board)-1)
    if board[x][y] != "_":
        comp_move(board)
    else:
        board[x][y] = "O"
        print_board(board)


def valid_input(str, boardsize):
    valid = False
    while valid == False:
        try:
            n = int(input(str))
            if n-1 in range(0,boardsize):
                valid = True
            else:
                print ("That wasn't in range.")
        except (ValueError):
            print ("That wasn't a number.")
    return n
            

def player_move(board):
    x = valid_input("Which row? ", len(board))-1
    y = valid_input("Which column? ", len(board))-1
    if board[x][y] != "_":
        print("That space is already taken, dumbass.")
        player_move(board)
    else:
        board[x][y] = "X"
        print_board(board)


def flip_coin():
    coin = random.randint(0,1)
    return coin



def check_row(row):
    if row[1:] == row[:-1] and row[0]!="_":
        return row[0], True
    else:
        return ("None", False)
        

def check_col(col,board):
    dummy = []
    for index, row in enumerate(board):
        dummy.append(row[col])
    if dummy[1:] == dummy[:-1] and dummy[0]!= "_":
        return dummy[0], True
    else:
        return ("None", False)
    

      
def check_diagonals(board):
    templist1 = []
    templist2 = []
    mid = int(len(board)/2)
    if board[mid][mid] != "_":
        for index, row in enumerate(board):
            templist1.append(row[index])
            templist2.append(row[len(board)-1-index])
        if templist1[1:] == templist1[:-1]:
            return templist1[0], True
        elif templist2[1:] == templist2[:-1]:
            return templist2[0], True

    return ("None", False)
        
    
def check_if_board_full(board):
    for row in board:
        for square in row:
            if square == "_":
                return False
    return True
    

def check_for_winner(board):
    Dwinner, Dwin  = check_diagonals(board)
    if Dwin == True:
        return Dwinner
    for i in range(0,len(board)):
        Cwinner, Cwin = check_col(i, board)
        Rwinner, Rwin= check_row(board[i])
        if Cwin == True:
            return Cwinner
        if Rwin == True:
            return Rwinner
    if check_if_board_full(board) == True:
        return "Stalemate"
                
    return "None"
        


def new_game():
    turn = 0
    board = define_board()
    print ("Turn " + str(turn))
    print_board(board)
    whose_turn = flip_coin()
    winner = "None"
    while winner == "None":  
        if whose_turn == 0:
            turn +=1
            print ("Turn " + str(turn))
            comp_move(board)
            whose_turn = 1
            winner = check_for_winner(board)          
            
        else:
            turn +=1
            print ("Turn " + str(turn))
            player_move(board)
            whose_turn = 0
            winner = check_for_winner(board)
            
            
    else:
        if winner == "X":
            print ("YOU WON! HOORAY!")
        elif winner == "Stalemate":
            print ("You couldn't beat a computer guessing randomly? Shame on you.")
        else:
            print ("You lost to a computer? How sad.")
        if input("Play again?") in ["Y","Yes","y","yes"]:
            del board[:]
            new_game()
        else:
            print ("Game over.")
        



new_game()



