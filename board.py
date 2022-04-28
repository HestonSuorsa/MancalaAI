class Board:
    def __init__(self):
        self.board = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
        self.bowl = [0, 0]
    
    # returns player, if player stays the same it was an invalid move
    def move(self, player, position):
        num_stones = self.board[position]
        fill_bowl = True
        if num_stones == 0:
            return player
        self.board[position] = 0
        while num_stones > 0:
            if (((position + 1) == 6 and player == 0) or ((position + 1) == len(self.board))) and fill_bowl:
                self.bowl[player] += 1
                num_stones -= 1
                fill_bowl = False
            else:
                position = (position + 1) % len(self.board)
                fill_bowl = True
                self.board[position] += 1
                num_stones -= 1

        opposite = 11 - position
        # if last stone fell in current player's bowl, give him another turn
        if not fill_bowl:
            return player
        elif self.board[position] == 1 and self.board[opposite] > 0:
            self.bowl[player] += self.board[opposite] + 1
            self.board[opposite] = 0
            self.board[position] -= 1

        return (player + 1) % 2

    def get_score(self, player):
        return self.bowl[player]

    def get_pieces(self, player):
        # number of pieces on players side
        pieces = 0
        for i in range(0, 6):
            pieces += self.board[player * 6 + i]
        return pieces

    # checks if someone's side has no more stones
    def is_gameover(self):
        return self.get_pieces(0) == 0 or self.get_pieces(1) == 0

    def print_both_scores(self):
        print(f'P1 - {self.bowl(0)} | P2 - {self.bowl(1)}')

    def __repr__(self):
        layout = '------------------------------\n'
        layout += 'P2: ' + str(self.bowl[1]) + '     6 <-- 1   |\n       |'
        # show in reverse for player 1
        for p in reversed(self.board[6:14]):
            layout += str(p) + ' '
        layout += '|                    \n\n       |'
        for p in self.board[0:6]:
            layout += str(p) + ' '
        layout += '|\n       |  1 --> 6      P1: ' + str(self.bowl[0]) + '\n--------------------------------'
        return layout
        
    def deepcopy(board):
        #TODO
        return