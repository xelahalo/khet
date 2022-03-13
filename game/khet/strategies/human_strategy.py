from game.khet.strategies.strategy import Strategy

class HumanStrategy(Strategy):
    def get_action(self, prev_actions):
        a = input()
        return a