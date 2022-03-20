from game.util.constants import Rotate, ActionType

class Action:  
    def __init__(self, action_type, origin, destination=None, rotation=Rotate.NO_ROTATION):
        self._action_type = action_type
        self._origin = origin
        self._destination = origin if self._action_type == ActionType.ROTATE else destination
        self._rotation = rotation

    @property
    def origin(self):
        return self._origin

    @property
    def destination(self):
        return self._destination

    @property
    def rotation(self):
        return self._rotation

    @property
    def action_type(self):
        return self._action_type

    def __str__(self):
        return self._action_type.value + ': ' + (str(self.destination) if self._action_type == ActionType.Move else str(self.rotate.value))