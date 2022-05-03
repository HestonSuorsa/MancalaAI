class fullAggressive:
    def __init__(self, player):
        self.player = player
        self.opponent = (player + 1) % 2
        self.chosen_move = -1

    def get_move(self, board):
        return self.aggressive(board)

    def aggressive(self, board):
        optimum = None  # optimum eval func should be highest always
        chosen_move = -1
        for i in range(6):
            if board.board[i + (self.player * 6)] == 0:
                continue
            possible_board = board.deepcopy()
            position = i + (self.player * 6)
            next_player = possible_board.move(self.player,
                                              position)  # Move name not required but is: move_name_map[pl] + str(i+2)
            if not optimum or optimum.get_score(self.player) < possible_board.get_score(self.player):
                optimum = possible_board
                chosen_move = position

        return chosen_move