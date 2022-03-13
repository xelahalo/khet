from game.util.constants import Color, TileChar
from game.khet.model.pieces.pharaoh import Pharaoh
from game.khet.model.pieces.djed import Djed
from game.khet.model.pieces.pyramid import Pyramid
from game.khet.model.pieces.obelisk import Obelisk

_TYPE_MAP = {
    TileChar.PHARAOH: (Pharaoh, 0),
    TileChar.DJED_C: (Djed, 0),
    TileChar.DJED_CC: (Djed, 90),
    TileChar.PYRAMID_UL: (Pyramid, 0),
    TileChar.PYRAMID_UR: (Pyramid, 90),
    TileChar.PYRAMID_DR: (Pyramid, 180),
    TileChar.PYRAMID_DL: (Pyramid, 270),
    TileChar.OBELISK: (Obelisk, 1),
    TileChar.OBELISK_STACKED: (Obelisk, 2)
}

class PieceFactory:
    def create(self, piece):
        color = Color.RED if piece[0] == 'R' else Color.BLUE
        char = piece[1]
            
        (activator, descriptor) = _TYPE_MAP.get(TileChar._value2member_map_[char])
        piece = activator(color, descriptor)
        return piece
        
