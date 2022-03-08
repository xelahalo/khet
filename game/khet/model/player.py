from abc import abstractclassmethod


class Player:
    def __init__(self):
        super.__init__()

    @abstractclassmethod
    def get_action(prev_actions):
        pass

    @abstractclassmethod
    def get_color():
        pass