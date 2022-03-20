from abc import ABC, abstractclassmethod

class Rotatable(ABC):
    
    @abstractclassmethod
    def rotate(self, rotation):
        pass