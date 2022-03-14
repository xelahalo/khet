from email.message import Message
from game.engine.UI.ui import UI
from game.util.constants import Color
from game.khet.model.action import Action
from game.khet.model.point import Point
from game.util.localization import MESSAGES
from game.util.constants import ActionType, Rotate

class ConsoleUI(UI):
    def draw(self, game, player):   
        self._print_board(game)
        self._set_teminal_color(player.color)

    def wait_for_action(self, color, board):
        origin = self._input_wrapper(lambda: self._choose_origin(color, board))
        action_type = self._input_wrapper(lambda: self._choose_action_type())
        destination = None
        rotation = None

        if(action_type == ActionType.MOVE):
            destination = self._input_wrapper(lambda: self._choose_destination(color, board, origin))
            return Action(origin, destination)
        else:
            rotation = self._input_wrapper(lambda: self._choose_rotation())
            return Action(origin, rotate=rotation)

    def _print_board(self, game):
        board = game.board.native_board

        for i in range(len(board)):
            for j in range(len(board[i])):
                print(board[i][j], end=' ')
            print(' ')
    
    def _set_teminal_color(self, color):
        print(Color.RESET.value + color.value)
        
    def _choose_origin(self, color, board):
        inp = input(MESSAGES.get('CHOOSE_PIECE')).split(',')
        point = Point(int(inp[0]), int(inp[1]))
        return point if board.can_move_piece(point, color) else None

    def _choose_destination(self, color, board, origin):
        inp = input(MESSAGES.get('TILE_TO_MOVE_TO')).split(',')
        dest = Point(int(inp[0]), int(inp[1]))
        return dest if board.can_move_piece_to(origin, dest, color) else None

    def _choose_rotation(self):
        inp = int(input(MESSAGES.get('ROTATION_DEGREE')))

        if (inp == Rotate.CLOCKWISE.value):
            return Rotate.CLOCKWISE
        elif (inp == Rotate.COUNTER_CLOCKWISE.value):
            return Rotate.COUNTER_CLOCKWISE
        else:
            raise Exception()

    def _choose_action_type(self):
        inp = input(MESSAGES.get('ROTATE_OR_MOVE')).lower()
        print(ActionType.MOVE.value)
        print(ActionType.ROTATE.value)
        if (inp == ActionType.MOVE.value):
            return ActionType.MOVE
        elif (inp == ActionType.ROTATE.value):
            return Action.ROTATE
        else:
            raise Exception()
    
    def _input_wrapper(self, get_input):
        ret = None
        while(ret is None):
            try:
                ret = get_input()
            except:
                print(MESSAGES.get('INVALID_INPUT'))