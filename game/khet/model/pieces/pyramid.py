from game.util.constants import TileChar
from game.khet.model.pieces.piece import Piece

class Pyramid(Piece):
    def __init__(self, color, rotation):
        super().__init__(color, rotation)

    def on_hit(self, direction):
        pass

    def __str__(self):
        return super().__str__(self._get_char())

    def _get_char(self):
        r = self._rotation
        if r == 0:
            return TileChar.PYRAMID_UL
        elif r == 90:
            return TileChar.PYRAMID_UR
        elif r == 180:
            return TileChar.PYRAMID_DR
        else:
            return TileChar.PYRAMID_DL
