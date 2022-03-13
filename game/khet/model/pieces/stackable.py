from abc import ABC, abstractclassmethod

from game.khet.model.pieces.piece import AbstractPiece

class Stackable(AbstractPiece):
    def __init__(self, player, initial_count):
        super.__init__(player)
        self.count = initial_count

    def increment(self):
        self.count = self.count + 1
        return True
    
    def decrement(self):
        self.count = self.count - 1
        return self.count > 0