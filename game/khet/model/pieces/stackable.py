from abc import ABC, abstractclassmethod

from game.khet.model.pieces.piece import Piece

class Stackable(Piece):
    def __init__(self, color, initial_count):
        super().__init__(color, 0)
        self.count = initial_count

    def increment(self):
        self.count = self.count + 1
        return True
    
    def decrement(self):
        self.count = self.count - 1
        return self.count > 0