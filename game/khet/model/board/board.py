from board.tile import Tile
from configurations import BOARD_MASK
from constants import Color
from game.factory.piece_factory import PieceFactory

class Board:
    def __init__(self, config):
        self._board = self._parse_board(config)
        self._piece_factory = PieceFactory()

    def _parse_board(self, config):
        board = []
        for i in range(config):
            row = []
            for j in range(config[i]):
                c = config[i][j]
                row.append(self._parse_tile(c, i, j) if len(c) == 1 else self._parse_piece(c))
            board.append(row)
        return board

    def _parse_tile(self, c, i, j):
        n = BOARD_MASK[i+1][j+1]
        if n > 1:
            return Tile(Color.BLUE)
        elif n == 1:
            return Tile(Color.RED)
        else:
            return Tile(Color.WHITE)

    def _parse_piece(self, c):
        return self._piece_factory.create(c)
                

