from game.khet.model.board.tile import Tile
from game.util.configurations import BOARD_MASK
from game.util.constants import Color
from game.khet.factory.piece_factory import PieceFactory

class Board:
    def __init__(self, config):
        self._piece_factory = PieceFactory()
        self._board = self._parse_board(config)

    def _parse_board(self, config):
        board = []
        for i in range(len(config)):
            row = []
            for j in range(len(config[i])):
                c = config[i][j]
                row.append(self._parse_tile(i, j) if len(c) == 1 else self._parse_piece(c))
            board.append(row)
        return board

    def _parse_tile(self, i, j):
        n = BOARD_MASK[i+1][j+1]
        if n > 1:
            return Tile(Color.BLUE)
        elif n == 1:
            return Tile(Color.RED)
        else:
            return Tile(Color.WHITE)

    def _parse_piece(self, c):
        return self._piece_factory.create(c)
                
    def print_board(self):
        for i in range(len(self._board)):
            for j in range(len(self._board[i])):
                print(self._board[i][j], end=' ')
            print(' ')

