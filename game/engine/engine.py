from game.util.constants import Color

class Engine:
    def __init__(self, game, ui):
        self._game = game
        self._ui = ui

    def play(self):
        self._ui.draw(self._game)

        while not self._game.is_finished:
            player = self._game.get_next_player()
            self._ui.set_teminal_color(player.color)

            action = player.get_action(self._game.copy())    
            self._game.set_action(action)
            self._game.evaluate(player)

            self._ui.draw(self._game)

        winner = self._game.get_winner()
        print((Color.BLUE.value + 'BLUE WINS') if winner.color == Color.BLUE else (Color.RED.value + 'RED WINS'))