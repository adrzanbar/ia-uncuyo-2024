import random
import sys
from search import (
    InstrumentedProblem,
    NQueensProblem,
    exp_schedule,
    genetic_algorithm,
    genetic_search,
    hill_climbing,
    select,
    simulated_annealing,
    timed_call,
)


def main():
    # Size of the chessboard (N x N)
    N = 10
    problem = NQueensProblem(N)

    # hc_problems = [InstrumentedProblem(problem) for _ in range(30)]
    # print("Hill climbing:")
    # times_results = []
    # for hc_problem in hc_problems:
    #     times_results.append(timed_call(hill_climbing, hc_problem))
    # print(
    #     "solutions found",
    #     len([result for result in times_results if problem.h(result[1].state) == 0]),
    # )
    hc_problem = InstrumentedProblem(problem)
    print("Hill climbing:")
    hc_times, hc_results = timed_call(hill_climbing, hc_problem)
    print("solution found", hc_results.state)
    print("states", hc_problem.states)
    print("path_cost", hc_results.path_cost)
    print("h", problem.h(hc_results.state))

    # sa_problems = [InstrumentedProblem(problem) for _ in range(30)]
    # times_results = []
    # print("Simulated annealing:")
    # for sa_problem in sa_problems:
    #     times_results.append(
    #         timed_call(simulated_annealing, sa_problem, exp_schedule())
    # )
    # print(
    #     "solutions found",
    #     len([result for result in times_results if problem.h(result[1].state) == 0]),
    # )
    sa_problem = InstrumentedProblem(problem)
    print("Simulated Annealing:")
    sa_times, sa_results = timed_call(simulated_annealing, sa_problem, exp_schedule())
    print("solution found", sa_results.state)
    print("states", sa_problem.states)
    print("path_cost", sa_results.path_cost)
    print("h", problem.h(sa_results.state))

    # ga_problems = [InstrumentedProblem(problem) for _ in range(30)]
    # times_results = []
    # print("Genetic algorithm:")
    # for ga_problem in ga_problems:
    #     times_results.append(timed_call(genetic_search, ga_problem))
    # print(
    #     "solutions found",
    #     len([result for result in times_results if problem.h(result[1]) == 0]),
    # )

    ga_problem = InstrumentedProblem(problem)
    print("Genetic algorith:")
    ga_time, ga_result = timed_call(genetic_search, ga_problem)
    print("solution found", ga_result.state)
    print("states", "N/A")
    print("path_cost", ga_result.path_cost)
    print("h", problem.h(ga_result.state))


if __name__ == "__main__":
    main()
