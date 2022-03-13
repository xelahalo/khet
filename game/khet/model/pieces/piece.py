from abc import ABC, abstractclassmethod

class AbstractPiece(ABC):
    def __init__(self, color):
        super.__init__()

    @abstractclassmethod
    def on_hit(direction):
        pass

    