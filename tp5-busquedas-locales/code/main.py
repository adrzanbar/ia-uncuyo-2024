from search import NQueensAgent, hill_climbing


def main():
    # Size of the chessboard (N x N)
    N = 8

    agent = NQueensAgent()

    solution = agent(N)

    # Display the solution
    if solution:
        print("Solution found:")
        for col in range(N):
            row = solution[col]
            print(f"Queen {col} placed at row {row}")
    else:
        print("No solution found.")


if __name__ == "__main__":
    main()
