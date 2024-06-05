def solveMaze(maze, x, y, solution):
    # Base case: jika (x, y) adalah titik keluar
    if x == exit_x and y == exit_y:
        solution[x][y] = 1
        return True

    # Pengecekan kondisi valid
    if isSafe(maze, x, y):
        # Tandai titik ini sebagai bagian dari jalur solusi
        solution[x][y] = 1

        # Bergerak ke arah bawah
        if solveMaze(maze, x + 1, y, solution):
            return True

        # Bergerak ke arah kanan
        if solveMaze(maze, x, y + 1, solution):
            return True

        # Bergerak ke arah atas
        if solveMaze(maze, x - 1, y, solution):
            return True

        # Bergerak ke arah kiri
        if solveMaze(maze, x, y - 1, solution):
            return True

        # Jika tidak ada solusi dari titik ini, batalkan tanda (backtrack)
        solution[x][y] = 0
        return False

    return False

def isSafe(maze, x, y):
    # Memastikan (x, y) berada di dalam batas grid dan bukan dinding
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0

# Contoh penggunaan
maze = [[0, 1, 0, 0],
        [0, 0, 1, 0],
        [1, 0, 0, 0],
        [0, 1, 1, 0]]
solution = [[0 for _ in range(len(maze[0]))] for _ in range(len(maze))]
exit_x, exit_y = 3, 3

if solveMaze(maze, 0, 0, solution):
    print("Solusi ditemukan:")
    for row in solution:
        print(row)
else:
    print("Tidak ada solusi yang ditemukan")