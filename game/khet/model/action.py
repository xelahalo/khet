from game.util.constants import Rotate, ActionType

class Action:  
    def __init__(self, origin, destination=None, rotate=Rotate.NO_ROTATION):
        self._action_type = ActionType.MOVE if rotate == Rotate.NO_ROTATION else ActionType.ROTATE
        self._origin = origin
        self._destination = destination if self.action_type == ActionType.Move else origin
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
    def action_type(self):
        return self._action_type

    def __str__(self):
        return self.action_type.value + ': ' + (str(self.destination) if self.action_type == ActionType.Move else str(self.rotate.value))