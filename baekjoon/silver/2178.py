import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
maze = []


def BFS(start_y, start_x):
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    move = [(1,0),(0,1),(-1,0),(0,-1)]
    queue = deque([(start_y, start_x)])
    
    while queue:
        now_y, now_x = queue.popleft()

        for dy, dx in move:
            nxt_y, nxt_x =  now_y + dy, now_x + dx
            if 0 <= nxt_y < n and 0 <= nxt_x < m:
                if maze[nxt_y][nxt_x] == '1' and not visited[nxt_y][nxt_x]:
                    visited[nxt_y][nxt_x] = visited[now_y][now_x] + 1
                    queue.append((nxt_y, nxt_x))
    
    return visited[n-1][m-1]     

for _ in range(n):
    maze.append(sys.stdin.readline().rstrip())
        
print(BFS(0,0))