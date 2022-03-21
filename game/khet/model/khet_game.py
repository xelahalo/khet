import math

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
    def __init__(self, config, board=None, players=None, current_player=None, laser_path=None, is_finished=None, score=None):
        self._config = config
        self._board = Board(config) if board is None else board
        self._players = [] if players is None else players
        self._current_player = 0 if current_player is None else current_player
        self._laser_path = [] if laser_path is None else laser_path
        self._is_finished = False if is_finished is None else is_finished
        self._score = 0 if score is None else score # player 1 is positive player 2 is negative (zero-sum game)

    @property
    def board(self):
        return self._board

    @property
    def laser_path(self):
        return self._laser_path

    @property
    def is_finished(self):
        return self._is_finished

    def copy(self):
        return KhetGame(self._config, self._board.copy(), self._players, self._current_player, self._laser_path, self._is_finished, self._score)

    def get_winner(self):
        return self._players[0] if self._score > 0 else self._players[1]

    def set_action(self, action):
        """
        It's the responsibility of the agent to check whether the move is valid or not.
        To ensure validity, use Board.can_move_pice and Board.can_move_piece_to
        """
        if action.action_type == ActionType.ROTATE:
            self.board.update_piece_rotation(action.destination, action.rotation)
        else:
            origin = self.board.get_obj(action.origin)
            destination = self.board.get_obj(action.destination)

            if action.action_type == ActionType.MOVE:
                if isinstance(origin, Obelisk) and isinstance(destination, Obelisk) and not destination.is_stacked():
                    self.board.update_obj(action.origin, self.board.parse_tile(action.origin.i, action.origin.j))
                    destination.increment()
                    return self.evaluate()
                elif isinstance(origin, Djed) and (isinstance(destination, Pyramid) or isinstance(destination, Obelisk)):
                    self.board.update_obj(action.origin, destination)
                    self.board.update_obj(action.destination, origin)
                    return self.evaluate()

                self.board.update_obj(action.destination, origin)
                self.board.update_obj(action.origin, self.board.parse_tile(action.origin.i, action.origin.j))
                
            elif action.action_type == ActionType.UNSTACK:
                origin.decrement()
                if isinstance(destination, Obelisk) and not destination.is_stacked():
                    destination.increment()
                else:
                    self.board.update_obj(action.destination, Obelisk(origin.color, 1))

        return self.evaluate()

    def evaluate(self):
        player = self.get_current_player()
        pos_of_obj = self.fire_laser(player)

        if pos_of_obj is not None:
            obj = self.board.get_obj(pos_of_obj)
            self._score = self._score + (obj.get_value() * (1 if obj.color == Color.RED else -1))

            if isinstance(obj, Obelisk) and obj.is_stacked():
                obj.decrement()
            else:
                self.board.update_obj(pos_of_obj, self.board.parse_tile(pos_of_obj.i, pos_of_obj.j))

            if isinstance(obj, Pharaoh):
                self._is_finished = True
        
        self.next_player()

    def next_player(self):
        self._current_player = 1 - self._current_player

    def get_current_player(self):
        return self._players[self._current_player]

    def add_player(self, player):
        self._players.append(player)

    def get_score(self):
        return self._score

    def fire_laser(self, player):
        board = self._board.native_board
        i, j, d = 0, 0, Direction.DOWN

        if player.color == Color.BLUE:
            i, j, d = len(board)-1, len(board[i])-1, Direction.UP

        if not isinstance(board[i][j], Tile):
            self._laser_path = []
            return Point(i,j)
        
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