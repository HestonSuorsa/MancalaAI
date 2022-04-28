from random import *

class abAgressive():
    def pickAggressiveMove():
        return
    
    def runABPruning():
        return

    def run(n):
        #n is the random chance we want the AI to choose an aggressive move or not
        chooseAB = randint(0,99)
        if chooseAB > n:
            print("Choosing an aggressive move")
            pickAggressiveMove()
        else:
            print("Choosing AB Pruning")
            runABPruning()

    
