from game.util.constants import TileChar
from game.khet.model.pieces.piece import Piece

class Djed(Piece):
    def __init__(self, color, rotation):
        super().__init__(color, rotation)

    def on_hit(self, direction):
        pass

    def __str__(self):
        return super().__str__(self._get_char())

    def _get_char(self, r):
        if self._rotation == 0:
            return TileChar.DJED_C
        else:
            return TileChar.DJED_CC
