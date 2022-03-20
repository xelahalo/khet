import copy

from game.khet.model.board.board import Board
from game.khet.model.board.tile import Tile
from game.khet.model.board.laser import Laser
from game.util.constants import DIR_LASER_CHAR_MAP, ActionType, Color, Direction, LaserChar
from game.khet.model.point import Point
from game.khet.model.pieces.djed import Djed
from game.khet.model.pieces.obelisk import Obelisk
from game.khet.model.pieces.pyramid import Pyramid
from game.khet.model.pieces.pharaoh import Pharaoh

class KhetGame:
    def __init__(self, config):
        self._config = config
        self._board = Board(config)
        self._players = []
        self._current_player = 0
        self._laser_path = []
        self._is_finished = False
        self._scores = {
            Color.BLUE: 0,
            Color.RED: 0
        }

    @property
    def board(self):
        return self._board

    @property
    def laser_path(self):
        return self._laser_path

    @property
    def is_finished(self):
        return self._is_finished

    def add_player(self, player):
        self._players.append(player)

    def copy(self):
        return copy.deepcopy(self)

    def get_winner(self):
        return self._players[0] if self._scores[Color.BLUE] > self._scores[Color.RED] else self._players[1]

    def set_action(self, action):
        """
        It's the responsibility of the agent to check whether the move is valid or not.
        To ensure validity, use Board.can_move_pice and Board.can_move_piece_to
        """
        if action.action_type == ActionType.ROTATE:
            self.board.update_piece_rotation(action.destination, action.rotation)
            return
        else:
            origin = self.board.get_obj(action.origin)
            destination = self.board.get_obj(action.destination)

            if action.action_type == ActionType.MOVE:
                if isinstance(origin, Obelisk) and isinstance(destination, Obelisk) and not destination.is_stacked():
                    self.board.update_obj(action.origin, self.board.parse_tile(action.origin.i, action.origin.j))
                    destination.increment()
                    return
                elif isinstance(origin, Djed) and (isinstance(destination, Pyramid) or isinstance(destination, Obelisk)):
                    self.board.update_obj(action.origin, destination)
                    self.board.update_obj(action.destination, origin)
                    return

                self.board.update_obj(action.destination, origin)
                self.board.update_obj(action.origin, self.board.parse_tile(action.origin.i, action.origin.j))
                return
            elif action.action_type == ActionType.UNSTACK:
                origin.decrement()
                if isinstance(destination, Obelisk) and not destination.is_stacked():
                    destination.increment()
                else:
                    self.board.update_obj(action.destination, Obelisk(origin.color, 1))

    def evaluate(self, player):
        pos_of_obj = self.fire_laser(player)

        if pos_of_obj is not None:
            obj = self.board.get_obj(pos_of_obj)
            self._scores[player.color] = self._scores[player.color] + (obj.get_value() * (1 if player.color != obj.color else -1))

            if isinstance(obj, Obelisk) and obj.is_stacked():
                obj.decrement()
            else:
                self.board.update_obj(pos_of_obj, self.board.parse_tile(pos_of_obj.i, pos_of_obj.j))

            if isinstance(obj, Pharaoh):
                self._is_finished = True

    def get_first_player(self):
        return self._players[0]

    def get_next_player(self):
        player = self._players[self._current_player]
        self._current_player = 1 - self._current_player
        return player

    def fire_laser(self, player):
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
                self._laser_path = path
                return None

            obj = board[i][j]
            laserchar = DIR_LASER_CHAR_MAP[d][Direction.STRAIGHT]

            if not isinstance(obj, Tile):
                hit_result = obj.on_hit(d)
                if hit_result == True:
                    self._laser_path = path
                    return Point(i,j)
                else:
                    laserchar = DIR_LASER_CHAR_MAP[d][hit_result]
                    d = hit_result

            path.append((Point(i, j), Laser(laserchar)))