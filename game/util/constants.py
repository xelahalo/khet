from enum import Enum

class ActionType(Enum):
    MOVE = 'move'
    ROTATE = 'rotate'
    UNSTACK = 'unstack'

class Rotate(Enum):
    CLOCKWISE = 1
    COUNTER_CLOCKWISE = -1
    NO_ROTATION = 0

class Direction(Enum):
    LEFT = 0
    UP = 1
    RIGHT = 2
    DOWN = 3
    STRAIGHT = 4

class TileChar(Enum):
    TILE = '▢'
    PHARAOH = '▣'
    DJED_C = '/'
    DJED_CC = '\\'
    PYRAMID_UL = '◪'
    PYRAMID_UR = '⬕'
    PYRAMID_DR = '◩'
    PYRAMID_DL = '⬔'
    OBELISK = '▨'
    OBELISK_STACKED = '▩' 

class LaserChar(Enum):
    VERTICAL = '|'
    HORIZONTAL = '-'
    ROTATE_C = '/'
    ROTATE_CC = '\\'

class Color(Enum):
    RESET = '\u001b[0m'
    RED = '\u001b[31m'
    GREEN = '\u001b[32m'
    BLUE = '\u001b[34m'
    WHITE = '\u001b[37m'

TURN_ORDER = [Color.BLUE, Color.RED]

COLOR_MASKS = {
    Color.RED: 1,
    Color.BLUE: 2
}

DIR_LASER_CHAR_MAP = {
    Direction.LEFT: {
        Direction.STRAIGHT: LaserChar.HORIZONTAL,
        Direction.UP: LaserChar.ROTATE_CC,
        Direction.DOWN: LaserChar.ROTATE_C
    },
    Direction.UP: {
        Direction.STRAIGHT: LaserChar.VERTICAL,
        Direction.LEFT: LaserChar.ROTATE_CC,
        Direction.RIGHT: LaserChar.ROTATE_C
    },
    Direction.RIGHT: {
        Direction.STRAIGHT: LaserChar.HORIZONTAL,
        Direction.UP: LaserChar.ROTATE_C,
        Direction.DOWN: LaserChar.ROTATE_CC
    },
    Direction.DOWN: {
        Direction.STRAIGHT: LaserChar.VERTICAL,
        Direction.LEFT: LaserChar.ROTATE_C,
        Direction.RIGHT: LaserChar.ROTATE_CC
    }
}

PYRAMID_DIRECTION_MAP = [
    {
        Direction.DOWN: Direction.LEFT,
        Direction.RIGHT: Direction.UP
    },
    {
        Direction.DOWN: Direction.RIGHT,
        Direction.LEFT: Direction.UP
    },
    {
        Direction.LEFT: Direction.DOWN,
        Direction.UP: Direction.RIGHT
    },
    {
        Direction.RIGHT: Direction.DOWN,
        Direction.UP: Direction.LEFT
    }
]

DJED_DIRECTION_MAP = [
    {
        Direction.LEFT: Direction.DOWN,
        Direction.UP: Direction.RIGHT,
        Direction.RIGHT: Direction.UP,
        Direction.DOWN: Direction.LEFT
    },
    {
        Direction.LEFT: Direction.UP,
        Direction.UP: Direction.LEFT,
        Direction.RIGHT: Direction.DOWN,
        Direction.DOWN: Direction.RIGHT
    }
]