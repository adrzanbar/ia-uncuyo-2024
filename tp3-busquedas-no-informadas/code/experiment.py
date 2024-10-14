import time
from frozen_lake import FrozenLakeAgent, generate_random_map_custom
from search import Node


class Experiment:

    def __init__(self, size, p, times):
        self.size = size
        self.p = p
        self.times = times
        self.generate_grids()

    def generate_grids(self):
        self.grids = []
        for _ in range(self.times):
            grid = generate_random_map_custom(self.size, self.p)
            self.grids.append(grid)

    def __call__(self, life, problem_class, search_algorithm):
        state_counts = []
        total_costs = []
        execution_times = []
        for grid in self.grids:
            agent = FrozenLakeAgent(life, problem_class, search_algorithm)
            start = time.time()
            agent(grid)
            end = time.time()
            execution_times.append(end - start)
            if isinstance(agent.node, Node):
                state_counts.append(len(agent.node.path()))
                total_costs.append(agent.node.path_cost)
            else:
                state_counts.append(agent.node)
                total_costs.append(agent.node)
        return {
            "total_costs": total_costs,
            "state_counts": state_counts,
            "execution_times": execution_times,
        }
