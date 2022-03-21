class Node:
    def __init__(self, game, parent, action):
        self.game = game
        self.parent = parent
        self.action = action
        
        self.player = game.get_current_player()
        self.score = game.get_score()
        self.children = []
        self.visits = 0
        

    def is_leaf(self):
        return not self.children

    def add_child(self, node):
        self.children.append(node)