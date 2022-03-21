import random

art = '''
 ______ __   ___  ______  ___    ___  ______   ___    ____
 | || | ||  //    | || | // \\\  //    | || |  // \\\  ||   
   ||   || ((       ||   ||=|| ((       ||   ((   )) ||== 
   ||   ||  \\\__    ||   || ||  \\\__    ||    \\\_//  ||___
   '''
BOARD = [1, 2, 3, 4, 5, 6, 7, 8, 9]


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


def legal_move(board):
    move = []
    for x in board:
        if type(x) == int:
            move.append(x)
    return move


def test(board, p):
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
    board_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    i = random.choice([0, 1])
    print_tic_tac_toe(board_values)
    for n in range(9):
        if (n + i) % 2 != 0:
            pos = input(f'\n\n{player1}, where do you want to place "X"?\n '
                        f'type 1-9 to replace a number on the board: ')
            if int(pos) in legal_move(board_values):
                board_values[int(pos) - 1] = "X"
                print_tic_tac_toe(board_values)
            else:
                print('Illegal move, game Over! Computer won.')
                break
            if game_won(board_values):
                print(f'Game Over! {player1.title()} won.')
                break
        else:
            pos = -1
            legal_pos = legal_move(board_values)
            for x in legal_pos:
                board_test = board_values[:]
                if test(board_test, x):
                    pos = x
                    break
            if pos == -1:
                pos = random.choice(legal_pos)
            board_values[int(pos) - 1] = "O"
            print_tic_tac_toe(board_values)
            if game_won(board_values):
                print(f'Game Over! Computer won.')
                break
    if n == 8:
        print(f'Game Over! It is a draw.')


def two_player():
    player1 = input('Player1 will use "X".  What is your name?  ').title()
    player2 = input('\nPlayer2 will use "O".  What is your name?  ').title()
    board_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print_tic_tac_toe(board_values)
    for n in range(9):
        if n % 2 == 0:
            pos = input(f'\n\n{player1.title()}, where do you want to place "X"?\n'
                        f' type 1-9 to replace a number on the board: ')
            if int(pos) in legal_move(board_values):
                board_values[int(pos) - 1] = "X"
                print_tic_tac_toe(board_values)
            else:
                print(f'Illegal move, game over.  {player2.title()} won.')
                break
            if game_won(board_values):
                print(f'Game Over! {player1.title()} won.')
                break
        else:
            pos = input(f'\n\n{player2.title()}, where do you want to place "O"? \n'
                        f' type 1-9 to replace a number on the board: ')
            if int(pos) in legal_move(board_values):
                board_values[int(pos) - 1] = "O"
                print_tic_tac_toe(board_values)
            else:
                print(f'Illegal move, game over.  {player1.title()} won.')
                break
            if game_won(board_values):
                print(f'Game Over! {player2.title()} won.')
                break
    if n == 8:
        print(f'Game Over! It is a draw.')


print(art)
print('Welcome to Tic-Tac-Toe game!')
print_tic_tac_toe(BOARD)

game_on = True
while game_on:
    num_player = input('How many people will play this game, 1 or 2?  ')
    if int(num_player) == 2:
        two_player()
    else:
        single_player()

    more_game = input("\n\nDo you want to play another game of Tic-Tac-Toe, Y/N?   ")
    if more_game.lower() != 'y':
        game_on = False
        print("Bye, have a good day!")
