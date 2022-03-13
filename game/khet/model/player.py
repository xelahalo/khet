from abc import ABC, abstractclassmethod


class Player(ABC):
    def __init__(self):
        super.__init__()

    @abstractclassmethod
    def get_action(prev_actions):
        pass

    @abstractclassmethod
    def get_color():
        pass