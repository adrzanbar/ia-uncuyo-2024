from search import NQueensProblem, benchmark, hill_climbing, simulated_annealing


def main():
    # Size of the chessboard (N x N)
    N = 8

    print("hill climbing", benchmark(hill_climbing, NQueensProblem(N)))
    print("simulated annealing", benchmark(simulated_annealing, NQueensProblem(N)))


if __name__ == "__main__":
    main()
