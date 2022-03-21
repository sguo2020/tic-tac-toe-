import random

BOARD = [1,2,3,4,5,6,7,8,9]

# Function to print Tic Tac Toe
def print_tic_tac_toe(board):

    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board[0], board[1], board[2]))
    print('\t_____|_____|_____')
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board[3], board[4], board[5]))
    print('\t_____|_____|_____')
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board[6], board[7], board[8]))
    print("\t     |     |")
    print("\n")


def game_won(board):
    if board[0] == board[1] == board[2] or \
            board[3] == board[4] == board[5] or \
            board[6] == board[7] == board[8] or \
            board[0] == board[3] == board[6] or \
            board[1] == board[4] == board[7] or \
            board[2] == board[5] == board[8] or \
            board[0] == board[4] == board[8] or \
            board[2] == board[4] == board[6]:
        return True


def y_test(board, p):
    print(board, 40)
    print(p, 41)
    board[p - 1] = "X"
    if board[0] == board[1] == board[2] or \
            board[3] == board[4] == board[5] or \
            board[6] == board[7] == board[8] or \
            board[0] == board[3] == board[6] or \
            board[1] == board[4] == board[7] or \
            board[2] == board[5] == board[8] or \
            board[0] == board[4] == board[8] or \
            board[2] == board[4] == board[6]:
        return True
    else:
        return False


def single_player():
    player1 = input('\n\nPlayer1 will use "X".  What is your name?  ').title()
    print(f'\n\n{player1}, you are playing against the computer.')
    board_values = [1,2,3,4,5,6,7,8,9]
    print_tic_tac_toe(board_values)
    for n in range(9):
        if n % 2 == 0:
            pos = input(f'\n\n{player1}, where do you want to place "X"?\n type 1-9 to replace a number on the board: ')
            board_values[int(pos) - 1] = "X"
            print_tic_tac_toe(board_values)
            if game_won(board_values):
                print(f'Game Over! {player1.title()} won.')
                break
        else:
            numeric_board = []
            pos = 0
            for x in board_values:
                if type(x) == int:
                    numeric_board.append(x)
            print(numeric_board)
            print(board_values)
            for y in numeric_board:
                print(y, 'y', 77)
                print(board_values, 'bv', 77)
                board_test = board_values
                print(board_test, 'bt', 78)
                if y_test(board_test, y):
                    pos = y
                    print(pos, 83)
                    break
            if pos == 0:
                pos = random.choice(numeric_board)
            print(pos, 85)
            board_values[int(pos) - 1] = "O"
            print_tic_tac_toe(board_values)
            if game_won(board_values):
                print(f'Game Over! Computer won.')
                break
    if n == 8:
        print(f'Game Over! It is a draw.')

single_player()

