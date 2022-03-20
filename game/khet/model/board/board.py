from game.khet.model.board.tile import Tile
from game.util.configurations import BOARD_MASK
from game.util.constants import COLOR_MASKS, ActionType, Color
from game.khet.factory.piece_factory import PieceFactory
from game.khet.model.pieces.piece import Piece
from game.khet.model.pieces.djed import Djed
from game.khet.model.pieces.obelisk import Obelisk
from game.khet.model.pieces.pyramid import Pyramid
from game.khet.model.pieces.stackable import Stackable

class Board:
    def __init__(self, config):
        self._piece_factory = PieceFactory()
        self._native_board = self._parse_board(config)

    @property
    def native_board(self):
        return self._native_board

    @native_board.setter
    def native_board(self, value):
        self._native_board = value

    def out_of_bounds(self, i, j):
        return i < 0 or j < 0 or i >= len(self._native_board) or j >= len(self._native_board[i])

    def can_move_piece(self, point, color):
        piece = self._native_board[point.i][point.j]
        return isinstance(piece, Piece) and color == piece.color

    def can_move_piece_to(self, origin, destination, color, action_type):
        color_mask = COLOR_MASKS[color]
        origin_piece = self._native_board[origin.i][origin.j]
        dest_obj = self._native_board[destination.i][destination.j]

        # wall is chosen
        if BOARD_MASK[destination.i][destination.j] < 0:
            return False
        # destination is not within 1 tile
        elif abs(origin.i - destination.i) > 1 or abs(origin.j - destination.j) > 1:
            return False
        # can't stay in place
        elif origin.i == destination.i and origin.j == destination.j:
            return False
        # tile is of the other player's color
        elif BOARD_MASK[destination.i + 1][destination.j + 1] > 0 and BOARD_MASK[destination.i + 1][destination.j + 1] != color_mask:
            return False
        # tile is occupied by another piece
        elif isinstance(dest_obj, Piece):
            if not isinstance(origin_piece, Djed) and not isinstance(origin_piece, Stackable):
                return False
        # djeds can switch places with pyramids or obelisks
        elif isinstance(origin_piece, Djed) and not(isinstance(dest_obj, Pyramid) or isinstance(dest_obj, Obelisk)):
            return False
        elif isinstance(dest_obj, Stackable):
            if not action_type == ActionType.UNSTACK or dest_obj.is_stacked():
                return False

        return True

    def can_unstack_piece(self, point):
        obj = self._native_board[point.i][point.j]
        return isinstance(obj, Stackable) and obj.is_stacked()

    def get_obj(self, point):
        return self._native_board[point.i][point.j]

    def update_obj(self, point, obj):
        self._native_board[point.i][point.j] = obj

    def update_piece_rotation(self, point, rotation):
        self._native_board[point.i][point.j].rotate(rotation)

    def parse_tile(self, i, j):
        n = BOARD_MASK[i+1][j+1]
        if n > 1:
            return Tile(Color.BLUE)
        elif n == 1:
            return Tile(Color.RED)
        else:
            return Tile(Color.WHITE)

    def _parse_board(self, config):
        board = []
        for i in range(len(config)):
            row = []
            for j in range(len(config[i])):
                c = config[i][j]
                row.append(self.parse_tile(i, j) if len(c) == 1 else self._parse_piece(c))
            board.append(row)
        return board

    def _parse_piece(self, c):
        return self._piece_factory.create(c)

