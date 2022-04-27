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

        while(num_stones > 0):
            if player == 0:
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
        if fill_bowl:
            return player
        elif self.board[position] == 1 and self.board[opposite] > 0:
            self.bowl[player] += self.board[opposite] + 1
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
        