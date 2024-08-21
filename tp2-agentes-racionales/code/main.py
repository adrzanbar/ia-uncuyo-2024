from experiment import run_experiment
from agent import Agent
from random_agent import RandomAgent
import time

def main():
    sizes = [2, 4, 8, 16, 32, 64, 128]
    dirt_rates = [0.1, 0.2, 0.4, 0.8]
    num_trials = 10

    reflexive_results = []
    random_results = []

    for size in sizes:
        for dirt_rate in dirt_rates:
            for _ in range(num_trials):
                # Reflexive Agent Experiment
                performance, elapsed_time = run_experiment(size, size, dirt_rate, Agent)
                reflexive_results.append((size, dirt_rate, 'Reflexivo', performance, elapsed_time))

                # Random Agent Experiment
                performance, elapsed_time = run_experiment(size, size, dirt_rate, RandomAgent)
                random_results.append((size, dirt_rate, 'Aleatorio', performance, elapsed_time))

    with open(f'reflexive_experiment_results{time.time()}.csv', 'w') as file:
        file.write('Tamaño, Tasa de Suciedad, Agente, Medida de Desempeño, Tiempo\n')
        for result in reflexive_results:
            file.write(f'{result[0]}, {result[1]}, {result[2]}, {result[3]}, {result[4]}\n')

    with open(f'random_experiment_results{time.time()}.csv', 'w') as file:
        file.write('Tamaño, Tasa de Suciedad, Agente, Medida de Desempeño, Tiempo\n')
        for result in random_results:
            file.write(f'{result[0]}, {result[1]}, {result[2]}, {result[3]}, {result[4]}\n')

if __name__ == "__main__":
    main()
