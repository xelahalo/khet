import math

from ai.parameters import C_CONST

def calculate_UCB(total_visits, score, num_of_visits):
    if num_of_visits == 0:
        return float('inf')

    return score / num_of_visits + math.sqrt(math.log(total_visits)/(C_CONST * num_of_visits))

def find_best_node_with_UCB(node):
    return max(node.children, key=lambda child: calculate_UCB(node.visits, child.score, child.visits))

    