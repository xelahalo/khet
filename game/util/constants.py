from enum import Enum, IntFlag

class Rotate(Enum):
    CLOCKWISE = 1
    COUNTER_CLOCKWISE = -1

class Direction(Enum):
    LEFT = 0
    UP = 1
    RIGHT = 2
    DOWN = 3
    UP_LEFT = 4
    UP_RIGHT = 5
    DOWN_LEFT = 6
    DOWN_RIGHT = 7

class Tiles(IntFlag):
    WALL = -1
    SILVER = 1
    RED = 1 << 1
    PHARAOH = 1 << 2
    DJED = 1 << 3
    PYRAMID = 1 << 4
    SPHINX = 1 << 5
    OBELISK = 1 << 6
    OBELISK2 = 1 << 7     