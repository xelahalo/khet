from game.util.constants import PYRAMID_DIRECTION_MAP, TileChar
from game.khet.model.pieces.piece import Piece
from game.khet.model.pieces.rotatable import Rotatable

class Pyramid(Piece, Rotatable):
    def __init__(self, color, rotation):
        super().__init__(color, rotation)

    def on_hit(self, source_dir):
        r = self._rotation // 90
        d = source_dir.value

        if d == r or d == (r + 1) % 4:
            return True
        
        return PYRAMID_DIRECTION_MAP[r][source_dir]
    
    def rotate(self, rotation):
        self.rotation = (self.rotation + (90 * rotation.value)) % 360

    def get_value(self):
        return 75000

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
