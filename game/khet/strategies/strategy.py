from abc import ABC, abstractclassmethod

class Strategy(ABC):
    def __init__(self, color, board):
        self._color = color
        self._board = board

    @abstractclassmethod
    def get_action(self, game, prev_actions):
        pass

    @property
    def color(self):
        return self._color