# This is a code for tic-tac-toe game

board = [' ', ' ', ' ',
         ' ', ' ', ' ',
         ' ', ' ', ' ']
player1 = 'X'  # player 1 is X which plays first always
player2 = 'O'  # player 2 is O
chance = 0

def showboard(board):  # it displays a board with lines
    for i in range(9):
        if (i+1) % 3 == 0 and i != 8:
            print(board[i], end="")
            print("\n---------")
        elif i == 8:
            print(board[8])
        elif i != 8:
            print(f"{board[i]} | ", end="")
showboard(board)

def check(moves):
    if board[moves - 1] != " ":  # if the index is not empty then it raises error to enter a different number
        raise TypeError("Already it contains a value, try a different number")

def checkwin():  # it checks where there is same character continuously for three boxes either horizontally nor vertically nor diagonally
    return ((board[0] != ' ' and board[0] == board[4] == board[8])
             or (board[2] != ' ' and board[2] == board[4] == board[6])
             or (board[0] != ' ' and board[0] == board[1] == board[2])
             or (board[3] != ' ' and board[3] == board[4] == board[5])
             or (board[6] != ' ' and board[6] == board[7] == board[8])
             or (board[0] != ' ' and board[0] == board[3] == board[6])
             or (board[1] != ' ' and board[1] == board[4] == board[7])
             or (board[2] != ' ' and board[2] == board[5] == board[8]))

for chance in range(9):
    if chance % 2 == 0:  # if the chance is even then it is the turn of player 1 else player 2
        moves = int(input("enter the move: "))  # the player must enter the location to place the character
        check(moves)
        board[moves - 1] = player1  # moves - 1 is the index to place the character in board
        showboard(board)
        win = checkwin()
        if win is True:
            print(f"\nWINNER {player1}")
            break
        elif chance == 8:  # if all chances are done and no one win then it is a draw match
            print("\nDRAW")
    else:
        moves = int(input("enter the move: "))
        check(moves)
        board[moves - 1] = player2
        showboard(board)
        win = checkwin()
        if win is True:
            print(f"\nWINNER {player2}")
            break
        elif chance == 8:
            print("\nDRAW")
