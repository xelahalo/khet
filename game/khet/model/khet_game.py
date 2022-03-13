from game.khet.model.board.board import Board
from util import parse_board
from board import board

class KhetGame:
    def __init__(self, p1, p2, config):
        self.board = Board(config)
        self.players = [p1, p2]
        self.current_player = 0

    def play(self):
        while(not self.is_finished()):
            player = self.get_next_player()
            action = player.get_action()
            self.eval_action(action)

        winner = self.get_winner()
        return winner

    def get_winner(self):
        pass

    def is_finished(self):
        return False

    def eval_action(self, action):
        pass

    def get_next_player(self):
        self.current_player = 1 - self.current_player
        return self.players[self.current_player]