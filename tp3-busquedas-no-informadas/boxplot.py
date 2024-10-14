from functools import partial
import matplotlib.pyplot as plt
import numpy as np

from experiment import Experiment
from frozen_lake import ActionCostProblem, FrozenLakeProblem, RandomProblem
from search import (
    breadth_first_graph_search,
    depth_first_graph_search,
    depth_first_tree_search,
    depth_limited_search,
    uniform_cost_search,
)


def boxplot(series, title, xlabel, ylabel, xticks):
    plt.boxplot(series)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(np.arange(1, len(series) + 1), xticks)
    plt.savefig(f"{title}.png")
    plt.close()


size = 100
p = 0.92
life = 1000

experiment = Experiment(size, p, 30)

fl_bfs = experiment(life, FrozenLakeProblem, breadth_first_graph_search)
fl_dfs = experiment(life, FrozenLakeProblem, depth_first_graph_search)
## Expected manhattan distance = 2 * p * size / 3
fl_dls = experiment(
    life,
    FrozenLakeProblem,
    partial(depth_limited_search, limit=round(2 * p * size / 3)),
)
fl_ucs = experiment(life, FrozenLakeProblem, uniform_cost_search)
# An agent searching a tree depth first in a problem where the possible actions
# are a single random action effectively becomes a random agent.
fl_r = experiment(life, RandomProblem, depth_first_tree_search)

boxplot(
    [
        [x for x in fl_bfs["total_costs"] if isinstance(x, int)],
        [x for x in fl_dfs["total_costs"] if isinstance(x, int)],
        [x for x in fl_dls["total_costs"] if isinstance(x, int)],
        [x for x in fl_ucs["total_costs"] if isinstance(x, int)],
        [x for x in fl_r["total_costs"] if isinstance(x, int)],
    ],
    "Total Costs - cost = 1",
    "Search Algorithms",
    "Total Costs",
    ["BFS", "DFS", "DLS", "UCS", "Random"],
)

boxplot(
    [
        [x for x in fl_bfs["state_counts"] if isinstance(x, int)],
        [x for x in fl_dfs["state_counts"] if isinstance(x, int)],
        [x for x in fl_dls["state_counts"] if isinstance(x, int)],
        [x for x in fl_ucs["state_counts"] if isinstance(x, int)],
        [x for x in fl_r["state_counts"] if isinstance(x, int)],
    ],
    "State Counts - cost = 1",
    "Search Algorithms",
    "State Counts",
    ["BFS", "DFS", "DLS", "UCS", "Random"],
)

boxplot(
    [
        [x for x in fl_bfs["execution_times"] if isinstance(x, float)],
        [x for x in fl_dfs["execution_times"] if isinstance(x, float)],
        [x for x in fl_dls["execution_times"] if isinstance(x, float)],
        [x for x in fl_ucs["execution_times"] if isinstance(x, float)],
        [x for x in fl_r["execution_times"] if isinstance(x, float)],
    ],
    "Execution Times - cost = 1",
    "Search Algorithms",
    "Execution Times",
    ["BFS", "DFS", "DLS", "UCS", "Random"],
)

ac_bfs = experiment(life, ActionCostProblem, breadth_first_graph_search)
ac_dfs = experiment(life, ActionCostProblem, depth_first_graph_search)
ac_dls = experiment(life, ActionCostProblem, partial(depth_limited_search, limit=10))
ac_ucs = experiment(life, ActionCostProblem, uniform_cost_search)
ac_r = experiment(life, RandomProblem, depth_first_graph_search)

boxplot(
    [
        [x for x in ac_bfs["total_costs"] if isinstance(x, int)],
        [x for x in ac_dfs["total_costs"] if isinstance(x, int)],
        [x for x in ac_dls["total_costs"] if isinstance(x, int)],
        [x for x in ac_ucs["total_costs"] if isinstance(x, int)],
        [x for x in ac_r["total_costs"] if isinstance(x, int)],
    ],
    "Total Costs - cost = action",
    "Search Algorithms",
    "Total Costs",
    ["BFS", "DFS", "DLS", "UCS", "Random"],
)


boxplot(
    [
        [x for x in ac_bfs["state_counts"] if isinstance(x, int)],
        [x for x in ac_dfs["state_counts"] if isinstance(x, int)],
        [x for x in ac_dls["state_counts"] if isinstance(x, int)],
        [x for x in ac_ucs["state_counts"] if isinstance(x, int)],
        [x for x in ac_r["state_counts"] if isinstance(x, int)],
    ],
    "State Counts - cost = action",
    "Search Algorithms",
    "State Counts",
    ["BFS", "DFS", "DLS", "UCS", "Random"],
)

boxplot(
    [
        [x for x in ac_bfs["execution_times"] if isinstance(x, float)],
        [x for x in ac_dfs["execution_times"] if isinstance(x, float)],
        [x for x in ac_dls["execution_times"] if isinstance(x, float)],
        [x for x in ac_ucs["execution_times"] if isinstance(x, float)],
        [x for x in ac_r["execution_times"] if isinstance(x, float)],
    ],
    "Execution Times - cost = action",
    "Search Algorithms",
    "Execution Times",
    ["BFS", "DFS", "DLS", "UCS", "Random"],
)
