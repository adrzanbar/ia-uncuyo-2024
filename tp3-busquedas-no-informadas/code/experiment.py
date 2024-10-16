import copy
import time

from frozen_lake import generate_random_map_custom
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

    def __call__(self, agent):
        nodes = []
        execution_times = []
        for grid in self.grids:
            start = time.time()
            agent(grid)
            end = time.time()
            nodes.append(agent.node)
            execution_times.append(end - start)
        return {
            "nodes": nodes,
            "execution_times": execution_times,
        }
