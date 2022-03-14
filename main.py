# https://www.ultraboardgames.com/khet-the-laser-game/game-rules.php
from game.engine.engine import Engine
from game.util.configurations import CLASSIC
from game.util.constants import Color
from game.engine.UI.console_ui import ConsoleUI
from game.khet.strategies.human_strategy import HumanStrategy
from game.khet.model.khet_game import KhetGame

def main():
    ui = ConsoleUI()
    game = KhetGame(CLASSIC)

    player1 = HumanStrategy(Color.BLUE, game.board, ui)
    player2 = HumanStrategy(Color.RED, game.board, ui)

    game.add_player(player1)
    game.add_player(player2)

    engine = Engine(game, ui)
    engine.play()
2
if __name__ == "__main__":
    main()