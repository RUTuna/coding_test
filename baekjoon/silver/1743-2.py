import sys
from collections import deque

n, m, k = map(int, sys.stdin.readline().split())
maps = [[0]*m for _ in range(n)]

for _ in range(k):
    r, c = map(int, sys.stdin.readline().split())
    maps[r-1][c-1] = 1

def BFS(start):
    queue = deque([start])
    size = 0
    
    while queue:
        r, c = queue.popleft()
        if not maps[r][c]:
            continue
        
        maps[r][c] = 0
        size+=1
        
        for dr, dc in [(0,1), (1,0), (0,-1),(-1,0)]:
            nr, nc = r+dr, c+dc
            if 0<=nr<n and 0<=nc<m and maps[nr][nc]:
                queue.append((nr,nc))
                
    return size

answer = 0
for r in range(n):
    for c in range(m):
        if maps[r][c]:
            answer = max(answer,BFS((r,c)))
            
print(answer)