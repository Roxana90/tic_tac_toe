def player_input(board):
    current_player = 'X'
    inp = int(input('Enter a number 1-9: '))
    if 1 <= inp <= 9 and board[inp - 1] == '-':
        board[inp-1] = current_player
    else:
        print('Oops, player is already in that spot!')
