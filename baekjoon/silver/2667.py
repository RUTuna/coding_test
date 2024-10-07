import sys
from collections import deque

n = int(sys.stdin.readline())
maps = []
result = []
visited = [[False] * n for _ in range(n)]
direction = [(1,0),(0,1),(-1,0),(0,-1)]

def isAble(i, j):
    return i > -1 and i < n and j > -1 and j < n

def BFS(postion):
    result = 0
    queue = deque([postion])
    
    while queue:
        pos_i, pos_j = queue.popleft()
        if visited[pos_i][pos_j]:
            continue
        
        result += 1
        visited[pos_i][pos_j] = True
        
        for i, j in direction:
            nxt_i, nxt_j = pos_i + i, pos_j + j
            if isAble(nxt_i, nxt_j) and not visited[nxt_i][nxt_j] and maps[nxt_i][nxt_j]:
                queue.append((nxt_i, nxt_j))
        
    
    return result
    
for _ in range(n):
    maps.append(list(map(int,sys.stdin.readline().rstrip())))

for i in range(n):
    for j in range(n):
        if not visited[i][j]:    
            if maps[i][j]:
                result.append(BFS((i,j)))
            
result.sort() 
print(len(result), *result, sep='\n')