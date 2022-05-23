from studentA import print_board, is_game_over, new_board
from studentB import ai_move, get_user_move, is_player_starting 

def announce_outcome(board, players_move):
    is_winner = False
    for i in range(3):
        if(board[i] == board[i+3] and board[i] == board[i+6]):
            is_winner = True
            break
        if(board[3*i] == board[3*i+1] and oard[3*i] == board[3*i+2]):
            is_winner = True
            break
        if(board[0] == board[4] and board[0] == board[8]):
            is_winner = True
            break
        if(board[2] == board[4] and board[2] == board[6]):
            is_winner = True
            break
        
    if(not is_winner): 
        print("REMIS")
        return
    
    if(players_move):
        print("WYGRAŁ KOMPUTER")
        return

    print("WYGRAŁ GRACZ")


board = new_board()
players_move = is_player_starting()
while not is_game_over(board):
    print_board(board)
    board = players_move and get_user_move(board) or ai_move(board)
    players_move = not players_move

announce_outcome(board, players_move)