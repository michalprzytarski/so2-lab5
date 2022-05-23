def print_board(board):
    print(board[0] + "  " + board[1] + "  " + board[2] + '\n')
    print(board[3] + "  " + board[4] + "  " + board[5] + '\n')
    print(board[6] + "  " + board[7] + "  " + board[8] )
    print("====================================")


def is_game_over(board):
    is_over = False
    # for x in range(1, 10):
    #     field = str(x)
    #     if field not in board:
    #         is_over = True

    # if board[0] == board[1] == board[2] or board[3] == board[4] == board[5] or board[6] == board[7] == board[8] or board[0] == board[4] == board[5] or board[6] == board[4] == board[2] or board[0] == board[3] == board[6] or board[1] == board[4] == board[7] or board[2] == board[5] == board[8]:
    #     is_over = True
    for i in range(9):
        if (board[i] != 'O' and board[i] != 'X'):
            break
        else:
            if(i == 8):
                 return True

    for i in range(3):
        if(board[i] == board[i+3] and board[i] == board[i+6]):
            is_over = True
            break
        if(board[3*i] == board[3*i+1] and board[3*i] == board[3*i+2]):
            is_over = True
            break
        if(board[0] == board[4] and board[0] == board[8]):
            is_over = True
            break
        if(board[2] == board[4] and board[2] == board[6]):
            is_over = True
            break

    return is_over


def new_board():
    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    return board


