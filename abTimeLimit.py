from abFullDepth import abFullDepth
from time import *

class abLimitedDepth(abFullDepth) :
    def abPruneLimited(sec):
        return
        #Call abPrune and only think (do ab pruning) for sec seconds before deciding a move
