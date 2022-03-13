from game.engine.UI.ui import UI

class ConsoleUI(UI):
    def draw(self, game):
         game.board.print_board()