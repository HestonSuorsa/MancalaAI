INFINITY = 1.0e400
from copy import deepcopy
from sre_constants import IN
from board import Board

class abLimitedDepth() :
    #run with a limit of n
    #n can be set to infinity for full depth search
    def __init__(self, limit, player):
        self.player = player
        self.limit = limit
        self.current_depth = 0
        self.chosen_move = -1

    def alpha_beta_search(self, board):
        self.current_depth = 0
        print("AI player num: " + str(self.player))
        v = self.max_value(board, -INFINITY, INFINITY, self.player)
        # TODO: make it so it returns the index of the move we make, not the value of highest score
        return self.chosen_move

    def max_value(self, board, alpha, beta, next_player) :
        self.current_depth += 1
        print("max current depth: " + str(self.current_depth) + "\n")
        stop = self.cutoff_test(board)
        if stop :
            return self.get_score(board)

        v = -INFINITY
        for a in range(6) :
            if board.board[a + (next_player*6)] != 0:
                position = a + (next_player*6)
                possible_board = board.deepcopy()
                next_player = possible_board.move(self.player, position)
                print("max move " + str(position))
                print("Possible board at max depth " + str(self.current_depth) + ": " + str(possible_board))
                if next_player != self.player:
                    v = max(v, self.min_value(possible_board, alpha, beta, next_player))
                else:
                    v = max(v, self.max_value(possible_board, alpha, beta, next_player))
                if v >= beta :
                    self.chosen_move = position
                    self.current_depth -= 1
                    return v
                alpha = max(alpha, v)

                if self.current_depth >= self.limit :
                    self.chosen_move = position
                    break
        self.chosen_move = position
        self.current_depth -= 1
        print("in max with chosen_move = " + str(self.chosen_move))
        return v

    def min_value(self, board, alpha, beta, next_player) :
        self.current_depth += 1
        print("min current depth: " + str(self.current_depth) + "\n")
        if self.cutoff_test(board) :
            return self.get_score(board)

        v = INFINITY
        for a in range(6) :
            if board.board[a + (next_player*6)] != 0:
                position = a + (next_player*6)
                possible_board = board.deepcopy()
                next_player = possible_board.move(self.player, position)
                print("min move " + str(position))
                print("Possible board at min depth " + str(self.current_depth) + ": " + str(possible_board))
                if next_player == self.player:
                    v = min(v, self.max_value(possible_board, alpha, beta, next_player))
                else:
                    v = min(v, self.min_value(possible_board, alpha, beta, next_player))
                if v<= alpha :
                    self.current_depth -= 1
                    return v
                beta = min(beta, v)

                if self.current_depth >= self.limit :
                    break
        self.current_depth -= 1
        return v

    def cutoff_test(self, board) :
        #check win, loss, one side F LMIT
        return (board.is_gameover() or self.current_depth >= self.limit)

    def get_score(self, board) :
        return board.get_score(self.player)















#     def runABPruning(board, n):
#         #run alphabetamove n times per player's move
#         for i in n:
#             #alphabetamove
#             if is_gameover(board):
#                 print("Someone won")
#         return

#     def maxValue(self, board, ply, turn):
#         """ Find the minimax value for the next move for this player
#         at a given board configuation. Returns score."""
#         if board.gameOver():
#             return turn.score(board)
#         score = -INFINITY
#         for m in board.legalMoves(self):
#             if ply == 0:
#                 #print "turn.score(board) in max value is: " + str(turn.score(board))
#                 return turn.score(board)
#             # make a new player to play the other side
#             opponent = Player(self.opp, self.type, self.ply)
#             # Copy the board so that we don't ruin it
#             nextBoard = deepcopy(board)
#             nextBoard.makeMove(self, m)
#             s = opponent.minValue(nextBoard, ply-1, turn)
#             #print "s in maxValue is: " + str(s)
#             if s > score:
#                 score = s
#         return score
    
#     def minValue(self, board, ply, turn):
#         """ Find the minimax value for the next move for this player
#             at a given board configuation. Returns score."""
#         if board.gameOver():
#             return turn.score(board)
#         score = INFINITY
#         for m in board.legalMoves(self):
#             if ply == 0:
#                 #print "turn.score(board) in min Value is: " + str(turn.score(board))
#                 return turn.score(board)
#             # make a new player to play the other side
#             opponent = Player(self.opp, self.type, self.ply)
#             # Copy the board so that we don't ruin it
#             nextBoard = deepcopy(board)
#             nextBoard.makeMove(self, m)
#             s = opponent.maxValue(nextBoard, ply-1, turn)
#             #print "s in minValue is: " + str(s)
#             if s < score:
#                 score = s
#         return score


#     # The default player defines a very simple score function

#     def score(self, board):
#         """ Returns the score for this player given the state of the board """
#         if board.hasWon(self.num):
#             return 100.0
#         elif board.hasWon(self.opp):
#             return 0.0
#         else:
#             return 50.0

 
#     def alphaBetaMove(self, board, ply):
#         """ Choose a move with alpha beta pruning.  Returns (score, move) """
#         move = -1
#         alpha = -INFINITY
#         beta = INFINITY
#         score = -INFINITY
#         turn = self
#         for m in board.legalMoves(self):
#             #for each legal move
#             if ply == 0:
#                 #if we're at ply 0, we need to call our eval function & return
#                 return (self.score(board), m)
#             if board.gameOver():
#                 return (-1, -1)  # Can't make a move, the game is over
#             nb = deepcopy(board)
#             #make a new board
#             nb.makeMove(self, m)
#             #try the move
#             opp = Player(self.opp, self.type, self.ply)
#             s = opp.minABValue(nb, ply-1, turn, alpha, beta)
#             #and see what the opponent would do next
#             if s > score:
#                 #if the result is better than our best score so far, save that move,score
#                 move = m
#                 score = s
#             alpha = max(score, alpha)
#         #return the best score and move so far
#         return score, move

#     #lower bound
#     def minABValue(self, board, ply, turn, alpha, beta):
#         """ Find the alpha-beta value for the next move for this player
#         at a given board configuation. Returns score."""
#         if board.gameOver():
#             return turn.score(board)
#         score = INFINITY
#         for m in board.legalMoves(self):
#             if ply == 0:
#                 #print "turn.score(board) in minValue is: " + str(turn.score(board))
#                 return turn.score(board)
#             # make a new player to play the other side
#             opponent = Player(self.opp, self.type, self.ply)
#             # Copy the board so that we don't ruin it
#             nextBoard = deepcopy(board)
#             nextBoard.makeMove(self, m)
#             #new score is the min value between old score and value when you call maxAB val on opponent
#             score = min(score, opponent.maxABValue(nextBoard, ply-1, turn, alpha, beta))
#             #if new score is smaller than alphaValue prune rest of tree branch
#             if(score <= alpha):
#                 return score
#             #update beta
#             beta = min(beta, score)
#              #print "score in minABValue is: " + str(s)
#         return score

#     #higher bound
#     def maxABValue(self, board, ply, turn, alpha, beta):
#         """ Find the alpha-beta value for the next move for this player
#             at a given board configuation. Returns score."""
#         if board.gameOver():
#             return turn.score(board)
#         score = -INFINITY
#         for m in board.legalMoves(self):
#             if ply == 0:
#                 #print "turn.score(board) in beta Value is: " + str(turn.score(board))
#                 return turn.score(board)
#             # make a new player to play the other side
#             opponent = Player(self.opp, self.type, self.ply)
#             # Copy the board so that we don't ruin it
#             nextBoard = deepcopy(board)
#             nextBoard.makeMove(self, m)
#             #score is the larger value between the old score and the value created by the function minABValue called on opp
#             score = max(score, opponent.minABValue(nextBoard, ply-1, turn, alpha, beta))
#             #if new score is larger than old betaValue prune rest of tree branch
#             if (score >= beta):
#                 return score
#             #update alpha
#             alpha = max(alpha, score)
#             #print "score in maxABValue is: " + str(s)
#         return score
                
#     def chooseMove(self, board):
#         return
#         # TODO

#     def deepcopy(board):
#         #TODO
#         return

# class Player:
#     HUMAN = 0
#     ABPRUNE = 1
    
#     def __init__(self, playerNum, playerType, ply=0):
#         self.num = playerNum
#         self.opp = 2 - playerNum + 1
#         self.type = playerType
#         self.ply = ply

#     def __repr__(self):
#         return str(self.num)

