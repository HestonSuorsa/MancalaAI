import random

from board import Board


if __name__ == '__main__':
    game_board = Board()
    P1 = 0
    P2 = 1
    current_player = random.randint(0, 1)

    while not game_board.is_gameover():
        print(game_board)
        position = int(input(f"P{current_player + 1}'s turn >"))
        position = (position - 1) + (current_player * 6)
        current_player = game_board.move(current_player, position)

    game_board.bowl[P1] += game_board.get_pieces(P1)
    game_board.bowl[P2] += game_board.get_pieces(P2)

    if game_board.get_score(P1) > game_board.get_score(P2):
        print(f"Player 1 wins!")
    elif game_board.get_score(P1) < game_board.get_score(P2):
        print("Player 2 wins!")
    else:
        print("Tie!")
    game_board.print_both_scores()
