import itertools

# Function to print the maze
def print_maze(maze):
    for row in maze:
        print("".join(str(cell) for cell in row))

# Function to solve the maze using Brute Force algorithm
def solve_maze_bruteforce(maze):
    n, m = len(maze), len(maze[0])
    # Generate all possible paths using itertools.product
    for path in itertools.product((0, 1), repeat=(n + m - 2)):
        x, y = 0, 0
        valid_path = True
        for move in path:
            # Move right if 1, move down if 0
            if move == 0:
                x += 1
            else:
                y += 1
            # Check if the move is within bounds and not blocked
            if x >= n or y >= m or maze[x][y] == 0:
                valid_path = False
                break
        # If a valid path to the exit is found, return True
        if valid_path:
            return True
    # If no valid path is found after trying all combinations, return False
    return False

# Maze example
maze = [
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 0, 1],
    [1, 1, 1, 1]
]

# Print the original maze
print("Original Maze:")
print_maze(maze)

# Solve the maze and print the result
print("\nResult:")
if solve_maze_bruteforce(maze):
    print("There is a path to exit.")
else:
    print("There is no path to exit.")