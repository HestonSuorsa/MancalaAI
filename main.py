#!/usr/bin/env python
'''
Paul Miller
Mancala AI Bot
	Implemented using Alpha-Beta Pruning to find best move.
'''
import multiprocessing
import random
import sys  # used to catch interrupts

# use these variables for players to prevent error checking on board
DEBUG = True


class Board:
    def __init__(self, other=None):
        if other:  # make copy
            self.board = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
            for i in range(0, len(other.board)):
                self.board[i] = other.board[i]
            self.bowl = [other.bowl[0], other.bowl[1]]
            self.move_num = other.move_num
        else:
            # player 0's side of board is board[0] and bowl[0]
            self.board = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
            self.bowl = [0, 0]
            self.move_num = 0

    def move(self, player, slot):
        # add one piece in board until bowl
        # if still
        # 	remaining pieces roll them over into next players skip other players bowl
        # if in bowl and no remaining pieces, then play again
        # slot (0, 5), player (0,1)
        slot = slot + player * 6;
        pieces = self.board[slot]
        self.board[slot] = 0
        next_player = player
        while pieces > 0:
            slot = (slot + 1) % 12
            # at players bowl,
            if slot == (player + 1) * 6 % 12:
                self.bowl[player] += 1
                next_player = player
                pieces -= 1  # drop piece in players bowl
            # if pieces, continue dropping in slots
            if pieces > 0:
                self.board[slot] += 1
                next_player = (player + 1) % 2  # next player
            pieces -= 1
            # if no more pieces, and on player side, add those pieces if >1(just added)
            if pieces == 0 and (player + 1) * 6 > slot > player * 6 and self.board[slot] > 1:
                pieces = self.board[slot]
                self.board[slot] = 0
        self.move_num += 1
        return next_player

    def get_score(self, player):
        return self.bowl[player]

    def get_pieces(self, player):
        # number of pieces on players side
        pieces = 0
        for i in range(0, 6):
            pieces += self.board[player * 6 + i]
        return pieces

    def check_move(self, player, move):
        return (0 <= move <= 6) and 0 != self.board[player * 6 + move]

    def has_move(self, player):
        # if the player has any moves
        i = 0
        while i < 6 and self.board[player * 6 + i] == 0:
            i += 1
        # if reached the end, not all zeroes
        return i != 6

    def game_over(self):
        # all pieces are in the bowls, game over
        return (self.bowl[0] + self.bowl[1]) == 48

    def __repr__(self):
        layout = '--------------' + str(self.move_num) + '----------------\n'
        layout += 'P2:' + str(self.bowl[1]) + '      6 <-- 1   |\n       |'
        # show in reverse for player 1
        for p in reversed(self.board[6:14]):
            layout += str(p) + ' '
        layout += '|                    \n\n       |'
        for p in self.board[0:6]:
            layout += str(p) + ' '
        layout += '|\n       |  1 --> 6      P1: ' + str(self.bowl[0]) + '\n--------------------------------'
        return layout


def get_user_move(board, player):
    # if DEBUG:
    #	return random.randint(0,5)
    valid = False
    move = 0
    while not valid:
        try:
            # get move input (1-6), offset to index (0-5)
            move = input('>')
            move = int(move) - 1
            while move < 0 or move > 5:
                print('Pick slots (1-6)')
                move = int(input('>')) - 1
            valid = True
        except TypeError:
            if move == 'quit':
                valid = True
            else:
                print('Pick slots (1-6) Integers only!')
                valid = False
    return move


def main():
    P1 = 0
    P2 = 1
    # multiprocess computaion
    parallel = True
    lookahead = 6  # AI lookahead depth, set to negative to search entire game
    board = Board()
    # ai Player
    # ai = AI(P2, lookahead) TODO: add AI classes
    # starting player is random
    current_player = random.randint(0, 1)
    next = (current_player + 1) % 2
    move = 0
    while not board.game_over() and move != 'quit':
        print(board)
        print('\nP' + str(current_player + 1) + '\'s Turn')
        # if the current player has a move, else switch
        if board.has_move(current_player):
            # not ai turn, user turn
            if current_player != 1:  # ai.player:
                move = ''
                next = current_player
                while current_player == next and board.has_move(current_player) and move != 'quit':
                    move = get_user_move(board, current_player)
                    if not board.check_move(current_player, move):
                        print('No pieces', move)
                    if move != 'quit':
                        next = board.move(current_player, move)
                        print(board)
                        print('Play again!')
                        print('\nP' + str(current_player + 1))
            else:
                move = ''
                next = current_player
                while current_player == next and board.has_move(current_player) and move != 'quit':
                    move = get_user_move(board, current_player)
                    if not board.check_move(current_player, move):
                        print('No pieces', move)
                    if move != 'quit':
                        next = board.move(current_player, move)
                        print(board)
                        print('Play again!')
                        print('\nP' + str(current_player + 1))
            # else:
            #     # AI turn
            #     move = ai.move(board, parallel)
            #     # get the move for the ai player
            #     print('\tAI picked ', move + 1)
            #     next = board.move(ai.player, move)
            #     # while AI has another move
            #     while ai.player == next and board.has_move(ai.player) and move != 'quit':
            #         print(board)
            #         print('\tAI Playing Again...')
            #         move = ai.move(board, parallel)
            #         print('\tAI picked ', move + 1)
            #         next = board.move(ai.player, move)
            #     # set player to the next
            current_player = next
        else:
            print('\n P' + str(current_player + 1) + ' has no moves!')
            current_player = (current_player + 1) % 2

    # If game is over and user did not quit
    if move != 'quit':
        print(' 		FINAL')
        print(board)
        p1_score = board.get_score(P1)
        p2_score = board.get_score(P2)
        if p1_score > p2_score:
            print('Player 1 Wins!')
        elif p1_score < p2_score:
            print('Player 2 Wins!')
        else:
            print('It\'s a tie !')
    print('Goodbye!')


if __name__ == '__main__':
    main()  # user interactive
    # ai_battle()  # watch AI's battle it out
