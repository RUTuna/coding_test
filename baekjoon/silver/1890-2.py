import sys

n = int(sys.stdin.readline())
maps = []
for _ in range(n):
    maps.append(list(map(int, sys.stdin.readline().split())))
    
    
paths = [[0]*n for _ in range(n)]
paths[0][0] = 1

for r in range(n):
    for c in range(n):
        distance = maps[r][c]
        if distance == 0:
            break
        
        for dr, dc in [(0, distance), (distance, 0)]:
            nr, nc = r+dr, c+dc
            if 0<=nr<n and 0<=nc<n:
                paths[nr][nc] += paths[r][c]


print(paths[-1][-1])