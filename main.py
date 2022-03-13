# https://www.ultraboardgames.com/khet-the-laser-game/game-rules.php
from game.util.configurations import CLASSIC
from game.engine.UI.console_ui import ConsoleUI
from game.khet.strategies.human_strategy import HumanStrategy
from game.khet.model.khet_game import KhetGame

game = KhetGame(HumanStrategy(), HumanStrategy(), CLASSIC, ConsoleUI())
game.play()
