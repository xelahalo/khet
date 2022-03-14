from abc import ABC, abstractclassmethod
from game.util.constants import Color

class Piece(ABC):
    def __init__(self, color, rotation):
        self._color = color
        self._rotation = rotation

    @property
    def color(self):
        return self._color

    @property
    def rotation(self):
        return self._rotation

    @rotation.setter
    def rotation(self, value):
        self._rotation = value

    @abstractclassmethod
    def on_hit(self, direction):
        pass

    def __str__(self, char):
        return self._color.value + str(char) + Color.RESET.value