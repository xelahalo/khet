from game.util.constants import TileChar
from game.khet.model.pieces.piece import Piece

class Pharaoh(Piece):
    def __init__(self, color, rotation):
        super().__init__(color, rotation)

    def on_hit(self, direction):
        pass

    def __str__(self):
        return super().__str__(self, TileChar.PHARAOH)