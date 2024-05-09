from colorama import init
from colorama import Fore, Back, Style
init(autoreset=True)

board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
player = 'X'


def draw_board(board):
    for i in range(3):
        print(Fore.GREEN + " | ".join(board[i]))
        print(Fore.GREEN + "---------")


def check_win(player, board):
    if board[0] == [player, player, player] or board[1] == [player, player, player] or board[2] == [player, player, player]:
        print('Победили', player)
        exit()
    elif player == board[0][1] == board[1][1] == board[2][1] or player == board[0][0] == board[1][0] == board[2][0] or player == board[0][2] == board[1][2] == board[2][2]:
        print('Победили', player)
        exit()
    elif player == board[0][0] == board[1][1] == board[2][2] or player == board[0][2] == board[1][1] == board[2][0]:
        print('Победили', player)
        exit()
    else:
        print('Следующий ход')
    if player == 'X':
        gamer = '0'
    else:
        gamer = 'X'
    return gamer

def ask_move(player, board):
    point1 = int(input('Введите вертикальные координаты:'))
    point2 = int(input('Введите горизонтальные координаты:'))
    sign_of_player = player
    return sign_of_player, point1, point2


def make_move(player, board, x, y):
    if player == 'X':
        if board[x-1][y-1] == ' ':
            board[x-1][y-1] = Fore.RED + player
        else:
            ask_and_make_move(player, board)
    elif player == '0':
        if board[x-1][y-1] == ' ':
            board[x-1][y-1] = Fore.MAGENTA + player
        else:
            ask_and_make_move(player, board)

def ask_and_make_move(player, board):
    tuple_with_move = ask_move(player, board)
    player = tuple_with_move[0]
    point1 = tuple_with_move[1]
    point2 = tuple_with_move[2]
    make_move(player, board, point1, point2)


def tic_tac_toe(player):
    draw_board(board)
    ask_and_make_move(player, board)
    player = check_win(player, board)
    tic_tac_toe(player)


tic_tac_toe(player)
