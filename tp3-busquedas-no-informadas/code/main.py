from functools import partial
import os
import matplotlib.pyplot as plt
import numpy as np

from experiment import Experiment
from frozen_lake import (
    ActionCostProblem,
    FrozenLakeProblem,
    RandomProblem,
)
from search import (
    Node,
    breadth_first_graph_search,
    depth_first_graph_search,
    depth_first_tree_search,
    depth_limited_search,
    uniform_cost_search,
)


def boxplot(series, title, xlabel, ylabel, xticks):
    if not os.path.exists("images"):
        os.makedirs("images")
    plt.boxplot(series)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(np.arange(1, len(series) + 1), xticks)
    plt.savefig(f"images/{title}.png")
    plt.close()


size = 100
p = 0.92
life = 1000

experiment = Experiment(size, p, 30)

print("Frozen Lake")
print("BFS")
fl_bfs = experiment(life, FrozenLakeProblem, breadth_first_graph_search)
print("DFS")
fl_dfs = experiment(life, FrozenLakeProblem, depth_first_graph_search)
print("DLS")
fl_dls = experiment(life, FrozenLakeProblem, partial(depth_limited_search, limit=10))
print("UCS")
fl_ucs = experiment(life, FrozenLakeProblem, uniform_cost_search)
print("Random")
# An agent searching a tree depth first in a problem where the possible actions
# are a single random action effectively becomes a random agent.
fl_r = experiment(life, RandomProblem, depth_first_tree_search)
print("Action Cost")
print("UCS")
ac_ucs = experiment(life, ActionCostProblem, uniform_cost_search)

total_cost_series = [
    [n.path_cost if isinstance(n, Node) else None for n in fl_bfs["nodes"]],
    [
        sum(n.solution()) + n.depth if isinstance(n, Node) else None
        for n in fl_bfs["nodes"]
    ],
    [n.path_cost if isinstance(n, Node) else None for n in fl_dfs["nodes"]],
    [
        sum(n.solution()) + n.depth if isinstance(n, Node) else None
        for n in fl_dfs["nodes"]
    ],
    [n.path_cost if isinstance(n, Node) else None for n in fl_dls["nodes"]],
    [
        sum(n.solution()) + n.depth if isinstance(n, Node) else None
        for n in fl_dls["nodes"]
    ],
    [n.path_cost if isinstance(n, Node) else None for n in fl_ucs["nodes"]],
    [n.path_cost if isinstance(n, Node) else None for n in ac_ucs["nodes"]],
    [n.path_cost if isinstance(n, Node) else None for n in fl_r["nodes"]],
    [
        sum(n.solution()) + n.depth if isinstance(n, Node) else None
        for n in fl_r["nodes"]
    ],
]
total_cost_series_filtered = [
    [value for value in series if value is not None] for series in total_cost_series
]
total_cost_series_filtered_no_dls = [
    total_cost_series_filtered[i] for i in range(10) if i not in [4, 5]
]

boxplot(
    total_cost_series_filtered,
    "Total Costs",
    "Search Algorithms",
    "Total Costs",
    [
        "BFSe1",
        "BFSe2",
        "DFSe1",
        "DFSe2",
        "DLSe1",
        "DLSe2",
        "UCSe1",
        "UCSe2",
        "Random_e1",
        "Random_e2",
    ],
)

boxplot(
    total_cost_series_filtered_no_dls,
    "Total Costs (DLS omitted)",
    "Search Algorithms",
    "Total Costs",
    [
        "BFSe1",
        "BFSe2",
        "DFSe1",
        "DFSe2",
        "UCSe1",
        "UCSe2",
        "Random_e1",
        "Random_e2",
    ],
)

state_count_series = [
    [x.depth if isinstance(x, Node) else None for x in fl_bfs["nodes"]],
    [x.depth if isinstance(x, Node) else None for x in fl_dfs["nodes"]],
    [x.depth if isinstance(x, Node) else None for x in fl_dls["nodes"]],
    [x.depth if isinstance(x, Node) else None for x in fl_ucs["nodes"]],
    [x.depth if isinstance(x, Node) else None for x in ac_ucs["nodes"]],
    [x.depth if isinstance(x, Node) else None for x in fl_r["nodes"]],
]
state_count_series_filtered = [
    [value for value in series if value is not None] for series in state_count_series
]
state_count_series_filtered_no_dls = [
    state_count_series_filtered[i] for i in range(6) if i not in [2]
]


boxplot(
    state_count_series_filtered,
    "State Counts",
    "Search Algorithms",
    "State Counts",
    ["BFS", "DFS", "DLS", "UCSe1", "UCSe2", "Random"],
)
boxplot(
    state_count_series_filtered_no_dls,
    "State Counts (DLS omitted)",
    "Search Algorithms",
    "State Counts",
    ["BFS", "DFS", "UCSe1", "UCSe2", "Random"],
)

execution_time_series = [
    [x for x in fl_bfs["execution_times"]],
    [x for x in fl_dfs["execution_times"]],
    [x for x in fl_dls["execution_times"]],
    [x for x in fl_ucs["execution_times"]],
    [x for x in ac_ucs["execution_times"]],
    [x for x in fl_r["execution_times"]],
]

boxplot(
    execution_time_series,
    "Execution Times",
    "Search Algorithms",
    "Execution Times",
    ["BFS", "DFS", "DLS", "UCSe1", "UCSe2", "Random"],
)

headers = [
    "algorithm_name",
    "env_n",
    "states_n",
    "cost_e1",
    "cost_e2",
    "time",
    "solution_found",
]


def csv(headers, experiments, filename):
    with open(filename, "w") as f:
        f.write(",".join(headers) + "\n")
        for experiment in experiments:
            for i in range(len(experiment[2])):
                f.write(
                    f"{experiment[0]},{experiment[1]},{experiment[2][i]},{experiment[3][i]},{experiment[4][i]},{experiment[5][i]},{experiment[6][i]}\n"
                )


total_cost_series_other_env = [
    [
        sum(n.solution()) + n.depth if isinstance(n, Node) else None
        for n in fl_ucs["nodes"]
    ],
    [n.depth if isinstance(n, Node) else None for n in ac_ucs["nodes"]],
]
experiments = [
    (
        "BFS",
        "env_1",
        state_count_series[0],
        total_cost_series[0],
        total_cost_series[1],
        execution_time_series[0],
        list(map(lambda x: x is not None, state_count_series[0])),
    ),
    (
        "DFS",
        "env_1",
        state_count_series[1],
        total_cost_series[2],
        total_cost_series[3],
        execution_time_series[1],
        list(map(lambda x: x is not None, state_count_series[1])),
    ),
    (
        "DLS",
        "env_1",
        state_count_series[2],
        total_cost_series[4],
        total_cost_series[5],
        execution_time_series[2],
        list(map(lambda x: x is not None, state_count_series[2])),
    ),
    (
        "UCSe1",
        "env_1",
        state_count_series[3],
        total_cost_series[6],
        total_cost_series_other_env[0],
        execution_time_series[3],
        list(map(lambda x: x is not None, state_count_series[3])),
    ),
    (
        "UCSe2",
        "env_2",
        state_count_series[4],
        total_cost_series[7],
        total_cost_series_other_env[1],
        execution_time_series[3],
        list(map(lambda x: x is not None, state_count_series[4])),
    ),
    (
        "Random",
        "env_1",
        state_count_series[5],
        total_cost_series[8],
        total_cost_series[9],
        execution_time_series[5],
        list(map(lambda x: x is not None, state_count_series[5])),
    ),
]

csv(headers, experiments, "no-informada-results.csv")
