from collections import deque
import copy

def solution(game_board, table):
    n = len(game_board)
    visited_board = [[False] * n for _ in range(n)]
    visited_table = [[False] * n for _ in range(n)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def bfs(start, grid, target):
        queue = deque([start])
        visited = visited_board if grid == game_board else visited_table
        visited[start[0]][start[1]] = True
        shape = [(0, 0)]
        
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == target:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    shape.append((nx - start[0], ny - start[1]))
        return shape

    def rotate(piece):
        return [(y, -x) for x, y in piece]

    def normalize(piece):
        min_x = min(x for x, y in piece)
        min_y = min(y for x, y in piece)
        return sorted([(x - min_x, y - min_y) for x, y in piece])

    def extract_shapes(grid, target):
        shapes = []
        visited = visited_board if grid == game_board else visited_table
        for i in range(n):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == target:
                    shape = bfs((i, j), grid, target)
                    shapes.append(normalize(shape))
        return shapes

    board_holes = extract_shapes(game_board, 0)
    table_pieces = extract_shapes(table, 1)

    used = [False] * len(table_pieces)
    answer = 0

    for hole in board_holes:
        for i, piece in enumerate(table_pieces):
            if used[i]:
                continue
            for _ in range(4):
                piece = normalize(piece)
                if hole == piece:
                    answer += len(piece)
                    used[i] = True
                    break
                piece = rotate(piece)
            if used[i]:
                break

    return answer