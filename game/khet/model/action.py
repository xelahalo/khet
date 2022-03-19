from game.util.constants import Rotate, ActionType

class Action:  
    def __init__(self, type, origin, destination=None, rotate=Rotate.NO_ROTATION):
        self._type = type
        self._origin = origin
        self._destination = origin if self.type == ActionType.ROTATE else destination
        self._rotate = rotate

    @property
    def origin(self):
        return self._origin

    @property
    def destination(self):
        return self._j

    @property
    def rotate(self):
        return self._rotate

    @property
    def type(self):
        return self._type

    def __str__(self):
        return self.type.value + ': ' + (str(self.destination) if self.type == ActionType.Move else str(self.rotate.value))