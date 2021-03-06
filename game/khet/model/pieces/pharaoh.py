import sys

from game.util.constants import TileChar
from game.khet.model.pieces.piece import Piece

class Pharaoh(Piece):
    def __init__(self, color, rotation):
        super().__init__(color, rotation)

    def get_value(self):
        return sys.maxsize

    def on_hit(self, _):
        return True

    def copy(self):
        return Pharaoh(self._color, self._rotation)

    def __str__(self):
        return super().__str__(TileChar.PHARAOH.value)