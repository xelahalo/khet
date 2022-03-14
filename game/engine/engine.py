class Engine:
    def __init__(self, game, ui):
        self._game = game
        self._ui = ui

    def play(self):
        while(not self._game.is_finished()):
            player = self._game.get_next_player()
            self._ui.draw(self._game, player)
            action = player.get_action([])
            self._game.set_action(action)

        winner = self._game.get_winner()
        return winner