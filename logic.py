# logic.py
def find_paths(maze):
    n = len(maze)
    paths = []
    visited = [[False]*n for _ in range(n)]

    def is_safe(x, y):
        return 0 <= x < n and 0 <= y < n and maze[x][y] == 1 and not visited[x][y]

    def solve(x, y, path):
        if x == n - 1 and y == n - 1:
            paths.append(path)
            return
        visited[x][y] = True
        for dx, dy, move in [(1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R'), (-1, 0, 'U')]:
            nx, ny = x + dx, y + dy
            if is_safe(nx, ny):
                solve(nx, ny, path + move)
        visited[x][y] = False

    if maze[0][0] == 1:
        solve(0, 0, "")
    return paths
