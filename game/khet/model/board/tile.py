class Tile:
    def __init__(self, color):
        self._color = color

    @property
    def get_color(self):
        return self._color
