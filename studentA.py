def print_board(board):
    print(board[0] + "  " + board[1] + "  " + board[2] + '\n')
    print(board[3] + "  " + board[4] + "  " + board[5] + '\n')
    print(board[6] + "  " + board[7] + "  " + board[8] + '\n')


def is_game_over(board):
    is_over = False
    for x in range(1, 10):
        field = str(x)
        if field not in board:
            is_over = True

    if board[0] == board[1] == board[2] or board[3] == board[4] == board[5] or board[6] == board[7] == board[8] or board[0] == board[4] == board[5] or board[6] == board[4] == board[2] or board[0] == board[3] == board[6] or board[1] == board[4] == board[7] or board[2] == board[5] == board[8]:
        is_over = True

    return is_over


def new_board():
    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    return board


