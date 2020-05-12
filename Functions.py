import random


def display_board(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' ')
    print('---|---|---')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' ')
    print('---|---|---')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' ')


def player_input():
    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('Player 1 chose X or O: ').upper()

    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, marker):
    return (board[1] == board[2] == board[3] == marker or
            board[4] == board[5] == board[6] == marker or
            board[7] == board[8] == board[9] == marker or
            board[1] == board[4] == board[7] == marker or
            board[2] == board[5] == board[8] == marker or
            board[3] == board[6] == board[9] == marker or
            board[1] == board[5] == board[9] == marker or
            board[3] == board[5] == board[7] == marker)


def choose_first():
    flip = random.randint(0, 1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):

    for i in range(1, 10):
        if board[i] == ' ':
            return False
    return True


def player_choice(board):

    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or board[position] != ' ':
        position = int(input('Choose position: (1-9) '))

    return position


def replay():
    choice = input('Play again? Enter Y or N: ').upper()

    return choice == 'Y'
