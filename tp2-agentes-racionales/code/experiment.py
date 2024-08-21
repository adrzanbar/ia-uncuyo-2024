import random
import time
from environment import Environment
from agent import Agent
from random_agent import RandomAgent

def run_experiment(sizeX, sizeY, dirt_rate, agent_type):
    """
    Ejecuta el experimento con el tipo de agente proporcionado.

    Parameters:
        sizeX (int): Dimensión X de la cuadrícula.
        sizeY (int): Dimensión Y de la cuadrícula.
        dirt_rate (float): Tasa de suciedad en la cuadrícula.
        agent_type (class): La clase del agente a utilizar (por ejemplo, Agent o RandomAgent).

    Returns:
        tuple: Desempeño y tiempo transcurrido.
    """
    # Inicializa el entorno y el agente
    init_posX = random.randint(0, sizeX - 1)
    init_posY = random.randint(0, sizeY - 1)

    env = Environment(sizeX, sizeY, init_posX, init_posY, dirt_rate)
    agent = agent_type(env)

    # Ejecuta el agente
    start_time = time.time()
    for _ in range(1000):
        agent.think()
    elapsed_time = time.time() - start_time

    # Obtiene el desempeño final
    performance = env.get_performance()
    return performance, elapsed_time
