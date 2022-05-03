import random
from abFullDepth import abFullDepth
from abLimitedDepth import abLimitedDepth
from abAggressive import abAggressive
from abTimeLimit import abTimeLimit
from fullAggressive import fullAggressive

from board import Board
from humanInput import humanInput


def choose_method(player, code):
    if code == 1:
        return humanInput(player)
    elif code == 2:
        return abFullDepth(player)
    elif code == 3:
        return abLimitedDepth(10, player)
    elif code == 4:
        return abTimeLimit(200, player)
    elif code == 5:
        return abAggressive(12, player, 1)
    elif code == 6:
        return fullAggressive(player)


def play_game(p1_int, p2_int):
    game_board = Board()
    P1 = 0
    P2 = 1
    current_player = random.randint(0, 1)

    p1_unit = choose_method(P1, p1_int)
    p2_unit = choose_method(P2, p2_int)

    while not game_board.is_gameover():
        print(game_board)

        if current_player == P1:
            move = p1_unit.get_move(game_board)
            print("P1 picked: " + str(move))
        else:
            move = p2_unit.get_move(game_board)
            print("P2 picked: " + str(move))
        current_player = game_board.move(current_player, move)

    if game_board.get_score(P1) > game_board.get_score(P2):
        print(f"Player 1 wins!")
    elif game_board.get_score(P1) < game_board.get_score(P2):
        print("Player 2 wins!")
    else:
        print("Tie!")
    game_board.print_both_scores()


def prompt_user(player):
    print(f"Choose for player {player}:\n"
          "[1] Human\n"
          "[2] Full Depth Alpha-Beta\n"
          "[3] Depth Limited Alpha-Beta Pruning\n"
          "[4] Time Limited Alpha-Beta Pruning\n"
          "[5] Aggressive Alpha-Beta Pruning\n"
          "[6] Fully Aggressive Algorithm\n"
          "[7] Quit\n")
    resp = int(input('Mancala >>'))
    if resp not in [1, 2, 3, 4, 5, 6, 7]:
        raise ValueError("Invalid response")
    return resp


if __name__ == '__main__':
    P1 = 1
    P2 = 2

    print("\nWelcome to Mancala!\n")

    while True:
        try:
            p1_choice = prompt_user(P1)
            if p1_choice == 7:
                break
            p2_choice = prompt_user(P2)
            if p2_choice == 7:
                break
            play_game(p1_choice, p2_choice)
        except ValueError:
            print("Invalid choice")

    print("Goodbye!\n")
