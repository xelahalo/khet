from game.khet.strategies.strategy import Strategy


class MonteCarlo(Strategy):
    def __init__(self, color, board):
        super().__init__(color, board)

    def get_action(self, game):
        pass

    def init_tree(self):
        pass

    def expand(self):
        pass

    def back_propagate(self):
        pass

    def rollout(self):
        pass
