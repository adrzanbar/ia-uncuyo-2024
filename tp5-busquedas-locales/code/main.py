from search import NQueensAgent, hill_climbing


def actions(state):
    N = len(state)
    return [
        state[:col] + (i,) + state[col + 1 :]  # Create a new state
        for col in range(N)  # Iterate over each element (column)
        for i in range(N)  # Iterate over all possible values for that element
        if i != state[col]  # Skip if the value is the same as the current one
    ]


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

    # state = (0,1,2,3,4,5,6,7)
    # action_list = actions(state)
    # for a in action_list:
    #     print(a)


if __name__ == "__main__":
    main()
