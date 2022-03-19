from game.util.constants import Direction, TileChar
from game.khet.model.pieces.piece import Piece

class Djed(Piece):
    def __init__(self, color, rotation):
        super().__init__(color, rotation)

    def on_hit(self, source_dir):
        parity = 1
        if self._rotation == 0:
            parity = 1 - parity

        if source_dir.value % 2 == parity:
            return Direction._value2member_map_[source_dir.value + 1 % 4]
        else:
            return Direction._value2member_map_[source_dir.value - 1 % 4]

    def __str__(self):
        return super().__str__(self._get_char())

    def _get_char(self):
        if self._rotation == 0:
            return TileChar.DJED_C.value
        else:
            return TileChar.DJED_CC.value
