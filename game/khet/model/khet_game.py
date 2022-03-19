import copy

from game.khet.model.board.board import Board
from game.khet.model.board.tile import Tile
from game.khet.model.board.laser import Laser
from game.util.constants import DIR_LASER_CHAR_MAP, Color, Direction, LaserChar
from game.khet.model.point import Point

class KhetGame:
    def __init__(self, config):
        self._config = config
        self._board = Board(config)
        self._players = []
        self._scores = [0, 0]
        self._current_player = 0

    @property
    def board(self):
        return self._board

    def add_player(self, player):
        self._players.append(player)

    def copy(self):
        return copy.deepcopy(self)

    def get_winner(self):
        return self._players[0] if self._scores[0] > self._scores[1] else self._players[1]

    def is_finished(self):
        return False

    def set_action(self, action):
        pass

    def get_first_player(self):
        return self._players[0]

    def get_next_player(self):
        player = self._players[self._current_player]
        self._current_player = 1 - self._current_player
        return player

    def build_laser_path(self, player):
        board = self._board.native_board
        i, j, d = 0, 0, Direction.DOWN

        if player.color == Color.BLUE:
            i, j, d = len(board)-1, len(board[i])-1, Direction.UP

        path = [(Point(i, j), Laser(LaserChar.VERTICAL))]

        while True:
            if d == Direction.LEFT:
                j = j - 1
            elif d == Direction.UP:
                i = i - 1
            elif d == Direction.RIGHT:
                j = j + 1
            elif d == Direction.DOWN:
                i = i + 1

            if self._board.out_of_bounds(i,j):
                return path

            obj = board[i][j]
            laserchar = DIR_LASER_CHAR_MAP[d][Direction.STRAIGHT]

            if not isinstance(obj, Tile):
                hit_result = obj.on_hit(d)
                if hit_result == True:
                    return path
                else:
                    laserchar = DIR_LASER_CHAR_MAP[d][hit_result]
                    d = hit_result

            path.append((Point(i, j), Laser(laserchar)))