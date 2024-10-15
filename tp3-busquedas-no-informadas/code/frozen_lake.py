from collections import deque
import random
from search import Node, Problem, SimpleProblemSolvingAgentProgram
import gymnasium as gym


def generate_random_map_custom(size, p):
    """
    Permite definir el tamaño de la grilla, la probabilidad que una casilla sea de hielo, y ubica de forma aleatoria la posición inicial del agente y del objetivo (el entorno creado a partir de dicha función podría no tener
    solución).
    Args:
        size: tamaño de cada lado de la grilla
        p: probabilidad de que una casilla sea de hielo
    """
    assert 0 <= p <= 1, "La probabilidad debe estar en el rango [0, 1]"
    assert size > 0, "El tamaño de la grilla debe ser mayor a 0"

    grid = [random.choices(["F", "H"], weights=[p, 1 - p], k=size) for _ in range(size)]

    start_position = goal_position = random.randint(0, size * size - 1)
    while start_position == goal_position:
        goal_position = random.randint(0, size * size - 1)

    i, j = divmod(start_position, size)
    grid[i][j] = "S"
    i, j = divmod(goal_position, size)
    grid[i][j] = "G"

    return grid


class FrozenLakeState:

    def __init__(self, position, move_count):
        self.position = position
        self.move_count = move_count


class FrozenLakeNode(Node):

    def expand(self, problem):
        return [
            self.child_node(problem, action)
            for action in problem.actions(FrozenLakeState(self.state, self.depth))
        ]

    def child_node(self, problem, action):
        next_state = problem.result(self.state, action)
        next_node = FrozenLakeNode(
            next_state,
            self,
            action,
            problem.path_cost(self.path_cost, self.state, action, next_state),
        )
        return next_node


class FrozenLakeProblem(Problem):

    def __init__(self, start, goal, grid, life):
        super().__init__(start, goal)
        self.grid = grid
        self.life = life

    def validate_action(self, position: int, action):
        i, j = divmod(position, len(self.grid))
        if action == 0:  # Left
            return j > 0 and self.grid[i][j - 1] != "H"
        if action == 1:  # Down
            return i < len(self.grid) - 1 and self.grid[i + 1][j] != "H"
        if action == 2:  # Right
            return j < len(self.grid[i]) - 1 and self.grid[i][j + 1] != "H"
        if action == 3:  # Up
            return i > 0 and self.grid[i - 1][j] != "H"
        return False

    def actions(self, state: FrozenLakeState):
        if state.move_count >= self.life:
            return []
        return [
            action
            for action in range(4)
            if self.validate_action(state.position, action)
        ]

    def result(self, state, action):
        if action == 0:
            return state - 1
        if action == 1:
            return state + len(self.grid)
        if action == 2:
            return state + 1
        if action == 3:
            return state - len(self.grid)


class ActionCostProblem(FrozenLakeProblem):

    def path_cost(self, c, state1, action, state2):
        return c + action + 1


class RandomProblem(FrozenLakeProblem):

    def actions(self, state: FrozenLakeState):
        return [random.choice(super().actions(state))] if super().actions(state) else []


class FrozenLakeAgent(SimpleProblemSolvingAgentProgram):

    def __init__(self, life, problem_class, search_algorithm):
        super().__init__()
        self.life = life
        self.problem_class = problem_class
        self.search_algorithm = search_algorithm
        self.node = None

    def update_state(self, state, percept):
        return percept

    def formulate_goal(self, state):
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == "G":
                    return i * len(state) + j

    def formulate_problem(self, state, goal):
        start = None
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == "S":
                    start = i * len(state) + j
                    break
            if start is not None:
                break
        return self.problem_class(start, goal, state, self.life)

    def search(self, problem):
        node = self.search_algorithm(problem, node_class=FrozenLakeNode)
        if isinstance(node, Node):
            self.node = node
            return node.solution()
