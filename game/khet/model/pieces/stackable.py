from abc import ABC, abstractclassmethod

from game.khet.model.pieces.piece import Piece

class Stackable(Piece):
    def __init__(self, color, initial_count):
        super().__init__(color, 0)
        self._count = initial_count

    def increment(self):
        self._count = self._count + 1
        return True
    
    def decrement(self):
        self._count = self._count - 1
        return self._count > 0