from game.util.constants import TileChar
from game.khet.model.pieces.stackable import Stackable

class Obelisk(Stackable):
    def __init__(self, color, initial_count):
        super().__init__(color, initial_count)

    def on_hit(self, _):
        return True

    def copy(self):
        return Obelisk(self._color, self._count)

    def __str__(self):
        return super().__str__(TileChar.OBELISK_STACKED.value if self.is_stacked() else TileChar.OBELISK.value)