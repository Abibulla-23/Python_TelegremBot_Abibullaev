player1 = 'X'
player2 = '0'
board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


def ask_and_make_move(player, board):
    point1 = int(input('Введите вертикальные координаты:'))
    point2 = int(input('Введите горизонтальные координаты:'))
    move = board[point1-1][point2-1]
    if move == ' ':
        board[point1-1][point2-1] = player
        print(board)
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
