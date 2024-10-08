import sys
from collections import deque

n = int(sys.stdin.readline())
maps = []
answer = []

for _ in range(n):
    maps.append(list(map(int, sys.stdin.readline().rstrip())))


def BFS(start):
    queue = deque([start])
    size = 0
    
    while queue:
        r, c = queue.popleft()
        if not maps[r][c]:
            continue
        
        size+=1
        maps[r][c] = 0
        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
            nr, nc = r+dr, c+dc
            if 0<=nr<n and 0<=nc<n and maps[nr][nc]:
                queue.append((nr,nc)) 
    
    return size
    
for r in range(n):
    for c in range(n):
        if maps[r][c]:
            answer.append(BFS((r,c)))
    
answer.sort()      
print(len(answer), *answer, sep='\n')