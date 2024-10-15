from functools import partial
import gymnasium as gym

from frozen_lake import (
    FrozenLakeAgent,
    FrozenLakeProblem,
    RandomProblem,
    generate_random_map_custom,
)
from search import (
    breadth_first_graph_search,
    breadth_first_tree_search,
    depth_first_graph_search,
    depth_first_tree_search,
    depth_limited_search,
)

grid = generate_random_map_custom(16, 0.92)
env = gym.wrappers.TimeLimit(
    gym.make("FrozenLake-v1", is_slippery=False, desc=grid, render_mode="human"), 16
)
# agent = FrozenLakeAgent(
#     16,
#     FrozenLakeProblem,
#     partial(depth_limited_search, limit=round(1.84 * 16 / 3)),
# )
agent = FrozenLakeAgent(16 * 16, RandomProblem, depth_first_tree_search)
print(agent(grid))
actions = agent.node.solution() if agent.node is not None else []

env.reset()
for action in actions:
    env.step(action)
