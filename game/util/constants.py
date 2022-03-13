from enum import Enum

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

class TileChar(Enum):
    WALL_HORIZONTAL = '|'
    WALL_VERTICAL = '-'
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

class Color(Enum):
    RESET = '\u001b[0m'
    BLUE = '\u001b[31m'
    RED = '\u001b[34m'
    WHITE = '\u001b[37m'