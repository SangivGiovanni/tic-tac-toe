
from Functions import display_board
from Functions import player_input
from Functions import place_marker
from Functions import win_check
from Functions import choose_first
from Functions import full_board_check
from Functions import player_choice
from Functions import replay


# While loop to run game

print('Welcome to tic tac toe!')

while True:

    # Play the game

    # Set up player, marker and board

    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first')

    ready_to_play = input('Ready to play? Y or N? ').upper()

    if ready_to_play == 'Y':
        game = True
    else:
        game = False

    # Gameplay

    while game:

        # Player 1 Turn

        if turn == 'Player 1':

            # Show board
            display_board(the_board)

            # Choose a position
            the_position = player_choice(the_board)

            # Place marker on position
            place_marker(the_board, player1_marker, the_position)

            # Check for win
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 Has Won! ')
                game = False

            # Or check for tie
            elif full_board_check(the_board):
                display_board(the_board)
                print('Tie Game! ')
                game = False

            # If neither win or tie then next player's turn
            else:
                turn = 'Player 2'

        # player 2 turn

        else:

            # Show board
            display_board(the_board)

            # Choose a position
            the_position = player_choice(the_board)

            # Place marker on position
            place_marker(the_board, player2_marker, the_position)

            # Check for win
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 Has Won! ')
                game = False

            # Or check for tie
            elif full_board_check(the_board):
                display_board(the_board)
                print('Tie Game! ')
                game = False

            # If neither win or tie then next player's turn
            else:
                turn = 'Player 1'

    # Break out of while loop on replay()
    if not replay():
        break
