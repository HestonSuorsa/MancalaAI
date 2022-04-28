INFINITY = 1.0e400
from abLimitedDepth import abLimitedDepth
class abFullDepth(abLimitedDepth) :
    def run(board):
        abLimitedDepth(board, INFINITY)
        #call limited depth but don't have a limit
        #Return or print the move to be taken