from game.util.constants import Color

class Laser:
    def __init__(self, char):
        self._char = char

    @property
    def char(self):
        return self.char

    def __str__(self):
        return Color.GREEN.value + self._char.value + Color.RESET.value