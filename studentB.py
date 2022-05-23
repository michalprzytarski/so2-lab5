import random

def ai_move(board):
    new_board = board.copy()
    possible_cell_indexes = []
    for idx, cell in enumerate(board):
        if(cell != 'O' and cell != 'X'):
            possible_cell_indexes.append(idx)
    selected_index = random.choice(possible_cell_indexes)
    new_board[selected_index] = 'X'
    return new_board

def get_user_move(board):
    print("wybierz pole: ")
    found = False
    new_board = board.copy()
    while not found:
        res = input('').split(" ")[0]
        for idx, cell in enumerate(board):
            if(cell == res):
                new_board[idx] = 'O'
                found = True
                break
        if not found: print("Niepoprawne pole. Wybierz jeszcze raz")
    return new_board



def is_player_starting():
    print("Checsz zacząć?(t/n)")
    res = ''
    while(True):
        res = input('').split(" ")[0]
        if(res == 't'): return True
        if(res == 'n'): return False
        print("zła odpowiedź")

    