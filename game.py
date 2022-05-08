import random
from board import print_board, board
from player_input import player_input


game_running = True
winner = None
current_player = 'X'


def check_horizontally(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != '-':
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != '-':
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != '-':
        winner = board[6]
        return True


def check_row(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != '-':
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != '-':
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != '-':
        winner = board[2]
        return True


def check_diagonally(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != '-':
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != '-':
        winner = board[2]
        return True


def check_win(board):
    global game_running
    if check_diagonally(board):
        print_board(board)
        print(f'The winner is {winner}!')
        game_running = False

    elif check_row(board):
        print_board(board)
        print(f'The winner is {winner}!')
        game_running = False

    elif check_diagonally(board):
        print_board(board)
        print(f'The winner is {winner}!')
        game_running = False


def check_tie(board):
    global game_running
    if '-' not in board:
        print_board(board)
        print('It is a tie!')
        game_running = False


def switch_player():
    global current_player
    if current_player == 'X':
        current_player = '0'
    else:
        current_player = 'X'


def computer(board):
    while current_player == '0':
        position = random.randint(0, 8)
        if board[position] == '-':
            switch_player()


while game_running:
    print_board(board)
    player_input(board)
    check_win(board)
    check_tie(board)
    switch_player()
    computer(board)
    check_win(board)
    check_tie(board)
