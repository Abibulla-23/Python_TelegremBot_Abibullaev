board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
player1 = 'X'
player2 = '0'


def draw_board(board):
    for i in range(3):
        print(" | ".join(board[i]))
        print("---------")


def ask_move(player, board):
    point1 = int(input('Введите вертикальные координаты:'))
    point2 = int(input('Введите горизонтальные координаты:'))
    sign_of_player = player
    return sign_of_player, point1, point2


def make_move(player, board, x, y):
    if board[x-1][y-1] == ' ':
        board[x-1][y-1] = player
        draw_board(board)
    else:
        ask_and_make_move(player, board)


def ask_and_make_move(player, board):
    tuple_with_move = ask_move(player, board)
    sign_of_player = tuple_with_move[0]
    point1 = tuple_with_move[1]
    point2 = tuple_with_move[2]
    make_move(sign_of_player, board, point1, point2)


def win(check_board):
    if check_board[0] == ['X', 'X', 'X'] or check_board[1] == ['X', 'X', 'X'] or check_board[2] == ['X', 'X', 'X']:
        print('Крестики победили!')


draw_board(board)

ask_and_make_move(player1, board)
ask_and_make_move(player1, board)
ask_and_make_move(player1, board)