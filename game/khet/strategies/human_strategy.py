from game.khet.strategies.strategy import Strategy

class HumanStrategy(Strategy):
    def __init__(self, color, board, ui):
        super().__init__(color, board)
        self._ui = ui

    def get_action(self, prev_actions):
        action = self._ui.wait_for_action(self._color, self._board)