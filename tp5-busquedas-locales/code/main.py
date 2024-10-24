import os
import sys

import numpy as np
from search import (
    InstrumentedProblem,
    NQueensProblem,
    exp_schedule,
    genetic_search,
    hill_climbing,
    simulated_annealing,
    timed_call,
)
import matplotlib.pyplot as plt
import pandas as pd


def experiment(problem, no_of_runs, algorithm, *args, **kwargs):
    times = []
    results = []
    instrumented_problems = []
    for _ in range(no_of_runs):
        instrumented_problems.append(InstrumentedProblem(problem))
        time, result = timed_call(algorithm, instrumented_problems[-1])
        times.append(time)
        results.append(result)
    return times, results, instrumented_problems


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


if __name__ == "__main__":
    Ns = [4, 8, 10]
    problems = [NQueensProblem(N) for N in Ns]
    no_of_runs = 30

    hc_experiment_results = []
    for problem in problems:
        times, results, instrumented_problems = experiment(
            problem, no_of_runs, hill_climbing
        )
        hc_experiment_results.append(
            {
                "times": times,
                "results": results,
                "instrumented_problems": instrumented_problems,
            }
        )

    sa_experiment_results = []
    for problem in problems:
        times, results, instrumented_problems = experiment(
            problem, no_of_runs, simulated_annealing, exp_schedule(k=100, limit=1000)
        )
        sa_experiment_results.append(
            {
                "times": times,
                "results": results,
                "instrumented_problems": instrumented_problems,
            }
        )

    ga_experiment_results = []
    for problem in problems:
        times, results, instrumented_problems = experiment(
            problem, no_of_runs, genetic_search, n=50
        )
        ga_experiment_results.append(
            {
                "times": times,
                "results": results,
                "instrumented_problems": instrumented_problems,
            }
        )

    # Boxplot

    boxplot_time_series = [
        result["times"]
        for experiment_results in [
            hc_experiment_results,
            sa_experiment_results,
            ga_experiment_results,
        ]
        for result in experiment_results
    ]

    boxplot(
        boxplot_time_series,
        "Boxplot of Times for Different Algorithms and Problem Sizes",
        "Algorithm and Problem Size",
        "Times",
        [f"HC-{N}" for N in Ns] + [f"SA-{N}" for N in Ns] + [f"GA-{N}" for N in Ns],
    )

    boxplot_states_series = [
        [problem.states for problem in result["instrumented_problems"]]
        for experiment_results in [
            hc_experiment_results,
            sa_experiment_results,
        ]
        for result in experiment_results
    ] + [
        [node.path_cost for node in result["results"]]
        for result in ga_experiment_results
    ]

    boxplot(
        boxplot_states_series,
        "Boxplot of States for Different Algorithms and Problem Sizes",
        "Algorithm and Problem Size",
        "Number of States",
        [f"HC-{N}" for N in Ns] + [f"SA-{N}" for N in Ns] + [f"GA-{N}" for N in Ns],
    )

    # csv

    headers = ["Algorithm", "Problem Size", "Time", "States", "H value"]
    rows = []
    for result in hc_experiment_results:
        for i in range(len(result["times"])):
            rows.append(
                [
                    "HC",
                    result["instrumented_problems"][i].problem.N,
                    result["times"][i],
                    result["instrumented_problems"][i].states,
                    result["instrumented_problems"][i].problem.h(
                        result["results"][i].state
                    ),
                ]
            )
    for result in sa_experiment_results:
        for i in range(len(result["times"])):
            rows.append(
                [
                    "SA",
                    result["instrumented_problems"][i].problem.N,
                    result["times"][i],
                    result["instrumented_problems"][i].states,
                    result["instrumented_problems"][i].problem.h(
                        result["results"][i].state
                    ),
                ]
            )
    for result in ga_experiment_results:
        for i in range(len(result["times"])):
            rows.append(
                [
                    "GA",
                    result["instrumented_problems"][i].problem.N,
                    result["times"][i],
                    result["results"][i].path_cost,
                    result["instrumented_problems"][i].problem.h(
                        result["results"][i].state
                    ),
                ]
            )

    df = pd.DataFrame(rows, columns=headers)
    df.to_csv("tp5-Nreinas.csv")

    # mean and stdev csv

    headers = [
        "Algorithm",
        "Problem Size",
        "Time mean",
        "Time standard deviation",
        "States mean",
        "States standard deviation",
        "Success rate",
    ]
    rows = []

    for result in hc_experiment_results:
        rows.append(
            [
                "HC",
                result["instrumented_problems"][0].problem.N,
                np.mean(result["times"]),
                np.std(result["times"]),
                np.mean(
                    [problem.states for problem in result["instrumented_problems"]]
                ),
                np.std([problem.states for problem in result["instrumented_problems"]]),
                list(
                    map(
                        result["instrumented_problems"][0].problem.h,
                        map(lambda node: node.state, result["results"]),
                    )
                ).count(0)
                / no_of_runs,
            ]
        )
    for result in sa_experiment_results:
        rows.append(
            [
                "SA",
                result["instrumented_problems"][0].problem.N,
                np.mean(result["times"]),
                np.std(result["times"]),
                np.mean(
                    [problem.states for problem in result["instrumented_problems"]]
                ),
                np.std([problem.states for problem in result["instrumented_problems"]]),
                list(
                    map(
                        result["instrumented_problems"][0].problem.h,
                        map(lambda node: node.state, result["results"]),
                    )
                ).count(0)
                / no_of_runs,
            ]
        )
    for result in ga_experiment_results:
        rows.append(
            [
                "GA",
                result["instrumented_problems"][0].problem.N,
                np.mean(result["times"]),
                np.std(result["times"]),
                np.mean([node.path_cost for node in result["results"]]),
                np.std([node.path_cost for node in result["results"]]),
                list(
                    map(
                        result["instrumented_problems"][0].problem.h,
                        map(lambda node: node.state, result["results"]),
                    )
                ).count(0)
                / no_of_runs,
            ]
        )

    df = pd.DataFrame(rows, columns=headers)
    df.to_csv("tp5-Nreinas-mean-stdev.csv")
