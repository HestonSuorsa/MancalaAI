

INFINITY = 1.0e400


class abFullDepth:
    # run with a limit of n
    # n can be set to infinity for full depth search
    def __init__(self, player):
        self.player = player
        self.opponent = (player + 1) % 2
        self.chosen_move = -1

    def get_move(self, board):
        return self.alpha_beta_search(board.deepcopy())

    def alpha_beta_search(self, board):
        v = self.max_value(board, -INFINITY, INFINITY, 0)
        return self.chosen_move

    def max_value(self, board, alpha, beta, depth):
        if self.cutoff_test(board, depth):
            return self.get_score(board)

        v = -INFINITY
        for a in range(6):
            if board.is_valid_move(a + (self.player * 6)):
                position = a + (self.player * 6)

                possible_board = board.deepcopy()
                next_player = possible_board.move(self.player, position)

                if next_player != self.player:
                    v = max(v, self.min_value(possible_board, alpha, beta, depth + 1))
                else:
                    v = max(v, self.max_value(possible_board, alpha, beta, depth + 1))
                if v >= beta:
                    self.chosen_move = position
                    return v
                alpha = max(alpha, v)
        self.chosen_move = position
        return v

    def min_value(self, board, alpha, beta, depth):

        if self.cutoff_test(board, depth):
            return self.get_score(board)

        v = INFINITY
        for a in range(6):
            if board.board[a + (self.opponent * 6)] != 0:
                position = a + (self.opponent * 6)
                possible_board = board.deepcopy()
                next_player = possible_board.move(self.opponent, position)

                if next_player == self.player:
                    v = min(v, self.max_value(possible_board, alpha, beta, depth + 1))
                else:
                    v = min(v, self.min_value(possible_board, alpha, beta, depth + 1))
                if v <= alpha:
                    return v
                beta = min(beta, v)

        return v

    def cutoff_test(self, board, depth):
        # check win, loss, one side F LIMIT
        return board.is_gameover()

    def get_score(self, board):
        return board.get_score(self.player)

