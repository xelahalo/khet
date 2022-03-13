from game.khet.model.board.board import Board

class KhetGame:
    def __init__(self, p1, p2, config, engine):
        self._board = Board(config)
        self._players = [p1, p2]
        self._current_player = 0
        self._engine = engine

    @property
    def get_board(self):
        return self._board

    def play(self):
        while(not self._is_finished()):
            player = self._get_next_player()
            action = player.get_action([])
            self._engine.draw(self)
            self._eval_action(action)

        winner = self._get_winner()
        return winner

    def _get_winner(self):
        pass

    def _is_finished(self):
        return False

    def _eval_action(self, action):
        pass

    def _get_next_player(self):
        self._current_player = 1 - self._current_player
        return self._players[self._current_player]