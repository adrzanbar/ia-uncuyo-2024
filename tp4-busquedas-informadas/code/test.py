
import sys
import gymnasium as gym

sys.path.append("/home/adrzanbar/ia-uncuyo-2024/tp3-busquedas-no-informadas/code")

from frozen_lake import (
    ActionCostProblem,
    FrozenLakeProblem,
    InformedAgent,
    generate_random_map_custom,
    manhattan_distance_heuristic,
)
from search import Node, astar_search

grid = generate_random_map_custom(32, 0.92)
print(grid)

agent_fl = InformedAgent(32, FrozenLakeProblem, astar_search, manhattan_distance_heuristic)
agent_ac = InformedAgent(32, ActionCostProblem, astar_search, manhattan_distance_heuristic)

agent_fl(grid)
agent_ac(grid)

solution_fl = []
solution_ac = []

if isinstance(agent_fl.node, Node):
    print("Solution found")
    solution_fl = agent_fl.node.solution()
    print(solution_fl)
    print(agent_fl.node.path_cost)
else:
    print("Solution not found")

if isinstance(agent_ac.node, Node):
    print("Solution found")
    solution_ac = agent_ac.node.solution()
    print(solution_ac)
    print(agent_ac.node.path_cost)
else:
    print("Solution not found")

# env = gym.wrappers.TimeLimit(
#     gym.make(
#         "FrozenLake-v1",
#         desc=grid,
#         is_slippery=False,
#         render_mode="human",
#     ),
#     32,
# )

# env.reset()
# for action in solution:
#     env.step(action)
