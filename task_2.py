player = 'X'
board = [[' 1', '1 ', ' 1'], [' ', ' ', ' '], [' ', ' ', ' ']]


def ask_and_make_move(player, board):
    point1 = int(input('Введите вертикальные координаты:'))
    point2 = int(input('Введите горизонтальные координаты:'))
    move = board[point1-1][point2-1]


ask_and_make_move(player, board)

