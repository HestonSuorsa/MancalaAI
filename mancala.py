import random
from abFullDepth import abFullDepth
from abLimitedDepth import abLimitedDepth
from abAggressive import abAggressive
from abTimeLimit import abTimeLimit

from board import Board


if __name__ == '__main__':
    game_board = Board()
    P1 = 0
    P2 = 1
    current_player = random.randint(0, 1)

    # AI player = 0
    # abAI = abLimitedDepth(10, 1)
    # abAI = abFullDepth(1)
    abAI = abAggressive(1, 1)
    # abAI = abTimeLimit(60,1)

    while not game_board.is_gameover():
        print(game_board)
        if current_player == 1:
            # move = abAI.alpha_beta_search(game_board.deepcopy())
            move = abAI.aggressive(game_board.deepcopy())
            print("AI picked: " + str(move))
            current_player = game_board.move(current_player, move)
        else:
            position = int(input(f"P{current_player + 1}'s turn >"))
            position = (position - 1) + (current_player * 6)
            current_player = game_board.move(current_player, position)

    if game_board.get_score(P1) > game_board.get_score(P2):
        print(f"Player 1 wins!")
    elif game_board.get_score(P1) < game_board.get_score(P2):
        print("Player 2 wins!")
    else:
        print("Tie!")
    game_board.print_both_scores()
