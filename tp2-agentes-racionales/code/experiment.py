import random
import time
from environment import Environment
from agent import Agent
from random_agent import RandomAgent

def run_experiment(agent: Agent):
    """
    Ejecuta el experimento con el tipo de agente proporcionado.

    Parameters:
        agent (Agent): El agente a utilizar (por ejemplo, Agent o RandomAgent).

    Returns:
        tuple: Desempeño y tiempo transcurrido.
    """
    init_posX = random.randint(0, agent.env.sizeX - 1)
    init_posY = random.randint(0, agent.env.sizeY - 1)

    # Ejecuta el agente
    start_time = time.time()
    for _ in range(1000):
        agent.think()
    elapsed_time = time.time() - start_time

    # Obtiene el desempeño final
    performance = agent.env.get_performance()
    return performance, elapsed_time
