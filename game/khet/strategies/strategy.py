from abc import ABC, abstractclassmethod

class Strategy(ABC):
    def __init__(self, color):
        self._color = color

    @abstractclassmethod
    def get_action(self, game):
        pass

    @property
    def color(self):
        return self._color