from game.util.constants import Color
from game.engine.UI.ui import UI
from game.khet.model.action import Action
from game.khet.model.point import Point
from game.util.localization import MESSAGES
from game.util.constants import ActionType, Rotate

class ConsoleUI(UI):
    def draw(self, game):
        self._print_laser(game)
        self._print_board(game.board.native_board)

    def get_action(self, color, board):
        origin = self._input_wrapper(lambda: self._choose_origin(color, board))
        action_type = self._input_wrapper(lambda: self._choose_action_type(origin, board))
        destination = None
        rotation = None

        if action_type == ActionType.ROTATE:
            rotation = self._input_wrapper(lambda: self._choose_rotation())
            return Action(action_type, origin, rotation=rotation)
        else:
            destination = self._input_wrapper(lambda: self._choose_destination(color, board, origin, action_type))
            return Action(action_type, origin, destination)

    def set_teminal_color(self, color):
        print(Color.RESET.value + color.value)

    def _choose_origin(self, color, board):
        inp = input(MESSAGES['CHOOSE_PIECE']).split(',')
        point = Point(int(inp[0]), int(inp[1]))
        return point if board.can_move_piece(point, color) else None

    def _choose_destination(self, color, board, origin, action_type):
        inp = input(MESSAGES['TILE_TO_MOVE_TO']).split(',')
        dest = Point(int(inp[0]), int(inp[1]))
        return dest if board.can_move_piece_to(origin, dest, color, action_type) else None

    def _choose_rotation(self):
        inp = int(input(MESSAGES['ROTATION_DEGREE']))

        if inp == Rotate.CLOCKWISE.value:
            return Rotate.CLOCKWISE
        elif inp == Rotate.COUNTER_CLOCKWISE.value:
            return Rotate.COUNTER_CLOCKWISE
        else:
            raise Exception()

    def _choose_action_type(self, origin, board):
        inp = input(MESSAGES['ROTATE_OR_MOVE_OR_UNSTACK']).lower()

        if inp == ActionType.MOVE.value:
            return ActionType.MOVE
        elif inp == ActionType.ROTATE.value:
            return ActionType.ROTATE
        elif inp == ActionType.UNSTACK.value and board.can_unstack_piece(origin):
            return ActionType.UNSTACK
        else:
            raise Exception()
    
    def _input_wrapper(self, get_input):
        ret = None
        while ret is None:
            try:
                ret = get_input()
            except:
                print(MESSAGES['INVALID_INPUT'])
        
        return ret

    def _print_laser(self, game):
        if not game.laser_path:
            return

        g = game.copy()
        board = g.board.native_board
        
        for point, char in game.laser_path:
            board[point.i][point.j] = char

        self._print_board(board)
        print(Color.WHITE.value + '-------------------')

    def _print_board(self, board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                print(board[i][j], end=' ')
            print(' ')