from abc import ABC, abstractclassmethod
from game.util.constants import Color

class Piece(ABC):
    def __init__(self, color, rotation):
        self._color = color
        self._rotation = rotation

    @abstractclassmethod
    def on_hit(self, direction):
        pass

    @abstractclassmethod
    def __str__(self, char):
        return self._color + char + Color.RESET