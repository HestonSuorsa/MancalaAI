class humanInput:
    def __init__(self, player):
        self.player = player

    def get_move(self, board):
        position = int(input(f"(P{self.player+1}) Your turn! >>"))
        return (position - 1) + (self.player * 6)
