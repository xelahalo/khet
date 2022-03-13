from game.util.constants import TileChar

class Tile:
    def __init__(self, color):
        self._color = color

    @property
    def get_color(self):
        return self._color

    def __str__(self):
        return self._color.value + TileChar.TILE.value