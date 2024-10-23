import sys
from collections import deque 

direction = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]
n, m = map(int, sys.stdin.readline().split())
sea = []
cost = [[sys.maxsize] * m for _ in range(n)]
queue = deque()

for _ in range(n):
    sea.append(sys.stdin.readline().split())
   
def BFS():
    while queue:
        r,c = queue.popleft()
        
        for dr, dc in direction:
            new_r, new_c = r+dr, c+dc
            if 0<=new_r<n and 0<=new_c<m and sea[new_r][new_c] == '0' and cost[new_r][new_c] > cost[r][c]+1:
                cost[new_r][new_c] = cost[r][c] + 1
                queue.append((new_r,new_c))

for i in range(n):
    for j in range(m):
        if sea[i][j] == '1':
            cost[i][j] = 0
            queue.append((i,j))
BFS()
            
answer = 0
for row in cost:
    answer = max(answer, *row)
    
print(answer)