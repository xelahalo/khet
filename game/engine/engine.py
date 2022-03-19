class Engine:
    def __init__(self, game, ui):
        self._game = game
        self._ui = ui

    def play(self):
        player = self._game.get_first_player()
        self._ui.draw(self._game, player, initial=True)

        while not self._game.is_finished():
            self._ui.set_teminal_color(player.color)

            player = self._game.get_next_player()

            action = player.get_action(self._game.copy())    

            self._game.set_action(action)

            self._ui.draw(self._game, player)

        winner = self._game.get_winner()
        return winner