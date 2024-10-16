
import sys
import gymnasium as gym

sys.path.append("/home/adrzanbar/ia-uncuyo-2024/tp3-busquedas-no-informadas/code")

from frozen_lake import (
    FrozenLakeProblem,
    InformedAgent,
    generate_random_map_custom,
    manhattan_distance_heuristic,
)
from search import Node, astar_search

grid = generate_random_map_custom(32, 0.6)
print(grid)

agent = InformedAgent(32, FrozenLakeProblem, astar_search, manhattan_distance_heuristic)
agent(grid)

solution = []
if isinstance(agent.node, Node):
    print("Solution found")
    solution = agent.node.solution()
    print(solution)
else:
    print("Solution not found")

env = gym.wrappers.TimeLimit(
    gym.make(
        "FrozenLake-v1",
        desc=grid,
        is_slippery=False,
        render_mode="human",
    ),
    32,
)

env.reset()
for action in solution:
    env.step(action)
