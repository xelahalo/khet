from game.util.constants import TileChar
from game.khet.model.pieces.piece import Piece

class Djed(Piece):
    def __init__(self, color, rotation):
        super().__init__(color, rotation)

    def on_hit(self, direction):
        pass

    def __str__(self):
        return super().draw(self._get_char())

    def _get_char(self):
        if self._rotation == 0:
            return TileChar.DJED_C.value
        else:
            return TileChar.DJED_CC.value
