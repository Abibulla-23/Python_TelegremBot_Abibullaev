arena = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
def draw_board(board):
    for i in range(3):
        print(" | ".join(board[i]))
        print("---------")
draw_board(arena)