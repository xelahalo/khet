from game.util.constants import PYRAMID_DIRECTION_MAP, TileChar
from game.khet.model.pieces.piece import Piece

class Pyramid(Piece):
    def __init__(self, color, rotation):
        super().__init__(color, rotation)

    def on_hit(self, source_dir):
        r = self._rotation // 90
        d = source_dir.value

        if d == r or d == (r + 1) % 4:
            return True

        negate = 1
        if (r + 2) % 4 == d:
            negate = negate * (-1)
        
        return PYRAMID_DIRECTION_MAP[r][source_dir]
    

    def __str__(self):
        return super().__str__(self._get_char())

    def _get_char(self):
        r = self._rotation
        if r == 0:
            return TileChar.PYRAMID_UL.value
        elif r == 90:
            return TileChar.PYRAMID_UR.value
        elif r == 180:
            return TileChar.PYRAMID_DR.value
        else:
            return TileChar.PYRAMID_DL.value
