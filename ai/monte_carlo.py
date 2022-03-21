import ai.ucb as UCB
import random as rng

from game.util.constants import Color
from game.khet.strategies.strategy import Strategy

from ai.parameters import D_MAX, MC_ITERATION_COUNT
from ai.node import Node

class MonteCarloStrategy(Strategy):
    def __init__(self, color):
        super().__init__(color)
        self._current_node = None
        self._root = None

    def get_action(self, game):
        self._current_node = self._init_tree(game)

        # start = timer()
        # while timer() - start < 10:
        for _ in range(MC_ITERATION_COUNT):
            while not self._current_node.is_leaf():
                self._current_node = UCB.find_best_node_with_UCB(self._current_node)

            if self._current_node.visits == 0:
                self._rollout()
            else:
                self._current_node = self._expand(self._current_node)
                self._rollout()
            
            self._current_node = self._root

        node_to_return = None
        if self.color == Color.BLUE:
            node_to_return = max(self._current_node.children, key=lambda child: child.score)
        else:
            node_to_return = min(self._current_node.children, key=lambda child: child.score)

        print(node_to_return.action)

        return node_to_return.action

    def _init_tree(self, game):
        self._root = Node(game, None, None)
        self._expand(self._root)
        self._root.visits =  self._root.visits + 1
        return self._root

    def _expand(self, node):
        possible_actions = node.game.board.get_possible_actions(node.player.color)
        for action in possible_actions:
            game_copy = node.game.copy()
            game_copy.set_action(action)

            new_node = Node(game_copy, node, action)
            node.add_child(new_node)
        return node.children[0]

    def _back_propagate(self, leaf, score):
        temp = leaf
        while temp is not None:
            temp.visits = temp.visits + 1
            temp.score = temp.score + score
            temp = temp.parent

    def _rollout(self):
        game_copy = self._current_node.game.copy()

        for _ in range(D_MAX):
            player = game_copy.get_current_player()
            all_actions = game_copy.board.get_possible_actions(player.color)
            game_copy.set_action(all_actions[rng.randrange(len(all_actions))])

            if game_copy.is_finished:
                break

        score = game_copy.get_score()

        self._back_propagate(self._current_node, score)