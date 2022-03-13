from abc import ABC, abstractclassmethod

class Strategy(ABC):
    @abstractclassmethod
    def get_action(self, prev_actions):
        pass