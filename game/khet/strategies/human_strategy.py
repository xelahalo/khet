from game.khet.strategies.strategy import Strategy

class HumanStrategy(Strategy):
    def __init__(self, color, ui):
        super().__init__(color)
        self._ui = ui

    def get_action(self, game):
        return self._ui.get_action(self._color, game.board)