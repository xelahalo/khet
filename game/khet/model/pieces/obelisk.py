from game.util.constants import TileChar
from game.khet.model.pieces.stackable import Stackable

class Obelisk(Stackable):
    def __init__(self, color, initial_count):
        super().__init__(color, initial_count)

    def on_hit(self, direction):
        pass

    def __str__(self):
        return super().draw(TileChar.OBELISK.value)