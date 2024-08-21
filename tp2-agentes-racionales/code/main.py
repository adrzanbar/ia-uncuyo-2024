from experiment import run_experiment
from agent import Agent
from environment import Environment
from random_agent import RandomAgent
import time
import random
import copy

def main():
    sizes = [2, 4, 8, 16, 32, 64, 128]
    dirt_rates = [0.1, 0.2, 0.4, 0.8]
    num_trials = 10
    
    for dirt_rate in dirt_rates:

        reflexive_results = []
        random_results = []

        for size in sizes:
            for _ in range(num_trials):
                init_posX = random.randint(0, size - 1)
                init_posY = random.randint(0, size - 1)

                env = Environment(size, size, init_posX, init_posY, dirt_rate)
                reflex_agent = Agent(copy.deepcopy(env))
                random_agent = RandomAgent(copy.deepcopy(env))


                # Reflexive Agent Experiment
                performance, elapsed_time = run_experiment(reflex_agent)
                reflexive_results.append((size, dirt_rate, 'Reflexivo', performance, elapsed_time))

                # Random Agent Experiment
                performance, elapsed_time = run_experiment(random_agent)
                random_results.append((size, dirt_rate, 'Aleatorio', performance, elapsed_time))

        with open(f'reflexive_experiment_results_dirt_rate_{dirt_rate}_{time.time()}.csv', 'w') as file:
            file.write('Tamaño, Tasa de Suciedad, Agente, Medida de Desempeño, Tiempo\n')
            for result in reflexive_results:
                file.write(f'{result[0]}, {result[1]}, {result[2]}, {result[3]}, {result[4]}\n')

        with open(f'random_experiment_results_dirt_rate_{dirt_rate}_{time.time()}.csv', 'w') as file:
            file.write('Tamaño, Tasa de Suciedad, Agente, Medida de Desempeño, Tiempo\n')
            for result in random_results:
                file.write(f'{result[0]}, {result[1]}, {result[2]}, {result[3]}, {result[4]}\n')

if __name__ == "__main__":
    main()
