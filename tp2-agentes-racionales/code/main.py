from experiment import run_experiment
from agent import Agent
from random_agent import RandomAgent

def main():
    sizes = [2, 4, 8, 16, 32, 64, 128]
    dirt_rates = [0.1, 0.2, 0.4, 0.8]
    num_trials = 10

    results = []

    for size in sizes:
        for dirt_rate in dirt_rates:
            for _ in range(num_trials):
                # Reflexive Agent Experiment
                performance, elapsed_time = run_experiment(size, size, dirt_rate, Agent)
                results.append((size, dirt_rate, 'Reflexive', performance, elapsed_time))

                # Random Agent Experiment
                performance, elapsed_time = run_experiment(size, size, dirt_rate, RandomAgent)
                results.append((size, dirt_rate, 'Random', performance, elapsed_time))

    # Guarda los resultados en un archivo CSV
    with open('experiment_results.csv', 'w') as file:
        file.write('Size, Dirt Rate, Agent Type, Performance, Time\n')
        for result in results:
            file.write(f'{result[0]}, {result[1]}, {result[2]}, {result[3]}, {result[4]}\n')

if __name__ == "__main__":
    main()
