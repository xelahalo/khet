import copy
from game.khet.model.board.board import Board

class KhetGame:
    def __init__(self, config):
        self._board = Board(config)
        self._players = []
        self._current_player = 0

    @property
    def board(self):
        return self._board

    def add_player(self, player):
        self._players.append(player)

    def copy(self):
        return copy.deepcopy(self)

    def get_winner(self):
        pass

    def is_finished(self):
        return False

    def set_action(self, action):
        pass

    def get_next_player(self):
        self._current_player = 1 - self._current_player
        return self._players[self._current_player]