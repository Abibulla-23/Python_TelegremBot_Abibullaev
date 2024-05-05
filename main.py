board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


def draw_board(board):
    for i in range(3):
        print(" | ".join(board[i]))
        print("---------")
draw_board(board)


player1 = 'X'
player2 = '0'


def win(check_board):
    if check_board[0] == ['X', 'X', 'X'] or check_board[1] == ['X', 'X', 'X'] or check_board[2] == ['X', 'X', 'X']:
        print('Крестики победили!')


def ask_and_make_move(player, board):
    point1 = int(input('Введите вертикальные координаты:'))
    point2 = int(input('Введите горизонтальные координаты:'))
    move = board[point1-1][point2-1]
    if move == ' ':
        board[point1-1][point2-1] = player
        draw_board(board)
        win(board)
    else:
        ask_and_make_move(player, board)


ask_and_make_move(player1, board)
ask_and_make_move(player2, board)
ask_and_make_move(player1, board)
ask_and_make_move(player2, board)
ask_and_make_move(player1, board)
ask_and_make_move(player2, board)
ask_and_make_move(player1, board)
ask_and_make_move(player2, board)
ask_and_make_move(player1, board)
ask_and_make_move(player2, board)
ask_and_make_move(player1, board)
ask_and_make_move(player2, board)
ask_and_make_move(player1, board)
ask_and_make_move(player2, board)


