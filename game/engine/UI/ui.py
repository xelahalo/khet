from abc import ABC, abstractclassmethod

class UI:
    @abstractclassmethod
    def draw(self, game, player):
        pass

    @abstractclassmethod
    def wait_for_action(self, color, board):
        pass
