from game.util.constants import DJED_DIRECTION_MAP, TileChar
from game.khet.model.pieces.piece import Piece
from game.khet.model.pieces.rotatable import Rotatable

class Djed(Piece, Rotatable):
    def __init__(self, color, rotation):
        super().__init__(color, rotation)

    def on_hit(self, source_dir):
        r = self.rotation // 90
        return DJED_DIRECTION_MAP[r][source_dir]

    def rotate(self, _):
        self.rotation = 90 - self.rotation

    def get_value(self):
        return 0

    def __str__(self):
        return super().__str__(self._get_char())

    def _get_char(self):
        if self._rotation == 0:
            return TileChar.DJED_C.value
        else:
            return TileChar.DJED_CC.value
