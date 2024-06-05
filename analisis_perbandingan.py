import time
from itertools import product

# Function to check if a move is safe (within bounds and not blocked)
def is_safe(maze, x, y):
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 1

# Backtracking algorithm to solve the maze
def solve_maze_backtracking(maze):
    solution = [[0 for _ in range(len(maze[0]))] for _ in range(len(maze))]
    if solve_maze_util(maze, 0, 0, solution):
        return solution
    else:
        return None

def solve_maze_util(maze, x, y, solution):
    if x == len(maze) - 1 and y == len(maze[0]) - 1:
        solution[x][y] = 1
        return True

    if is_safe(maze, x, y):
        solution[x][y] = 1

        if solve_maze_util(maze, x + 1, y, solution):
            return True

        if solve_maze_util(maze, x, y + 1, solution):
            return True

        solution[x][y] = 0
        return False

    return False

# Brute force algorithm to solve the maze
def solve_maze_bruteforce(maze):
    n, m = len(maze), len(maze[0])
    for path in product((0, 1), repeat=(n + m - 2)):
        x, y = 0, 0
        valid_path = True
        for move in path:
            if move == 0:
                x += 1
            else:
                y += 1
            if x >= n or y >= m or maze[x][y] == 0:
                valid_path = False
                break
        if valid_path:
            return True
    return False

# Function to measure runtime of Backtracking algorithm
def measure_backtracking_runtime(maze):
    start_time = time.time()
    solve_maze_backtracking(maze)
    end_time = time.time()
    return end_time - start_time

# Function to measure runtime of Brute Force algorithm
def measure_bruteforce_runtime(maze):
    start_time = time.time()
    solve_maze_bruteforce(maze)
    end_time = time.time()
    return end_time - start_time

# Sample mazes for testing
small_maze = [
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 0, 1],
    [1, 1, 1, 1]
]

medium_maze = [
    [1, 0, 1, 1, 1, 1],
    [1, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 1],
    [0, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1]
]

large_maze = [
    [1, 0, 1, 1, 1, 0, 1, 1],
    [1, 1, 0, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1],
    [0, 0, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 0, 1, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1]
]

# Measure and compare runtimes
backtracking_runtime_small = measure_backtracking_runtime(small_maze)
bruteforce_runtime_small = measure_bruteforce_runtime(small_maze)

backtracking_runtime_medium = measure_backtracking_runtime(medium_maze)
bruteforce_runtime_medium = measure_bruteforce_runtime(medium_maze)

backtracking_runtime_large = measure_backtracking_runtime(large_maze)
bruteforce_runtime_large = measure_bruteforce_runtime(large_maze)

print(f"Backtracking runtime (small maze): {backtracking_runtime_small:.6f} seconds")
print(f"Brute Force runtime (small maze): {bruteforce_runtime_small:.6f} seconds")

print(f"Backtracking runtime (medium maze): {backtracking_runtime_medium:.6f} seconds")
print(f"Brute Force runtime (medium maze): {bruteforce_runtime_medium:.6f} seconds")

print(f"Backtracking runtime (large maze): {backtracking_runtime_large:.6f} seconds")
print(f"Brute Force runtime (large maze): {bruteforce_runtime_large:.6f} seconds")
