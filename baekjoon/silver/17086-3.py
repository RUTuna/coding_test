import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
distance = [[sys.maxsize]*m for _ in range(n)]
maps = []
queue = deque([])
direct = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]

for _ in range(n):
    maps.append(list(map(int, sys.stdin.readline().split())))

for r in range(n):
    for c in range(m):
        if maps[r][c]:
            queue.append((r, c, 0))
            distance[r][c] = 0

while queue:
    r, c, d = queue.popleft()
    
    for dr, dc in direct:
        nr, nc = r+dr, c+dc
        if 0<=nr<n and 0<=nc<m and not maps[nr][nc] and d+1 < distance[nr][nc]:
            queue.append((nr, nc, d+1))
            distance[nr][nc] = d+1     

print(max(list(map(max, distance))))