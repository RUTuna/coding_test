import sys

n, m, k = map(int, sys.stdin.readline().split())
grid = [ [0] * m for _ in range(n)]

for _ in range(k):
    r, c = map(int, sys.stdin.readline().split())
    grid[r-1][c-1] = 1
    
    
def DFS(r, c):
    stack = [(r, c)]
    size = 0
    
    while stack:
        now_r, now_c = stack.pop()
        
        if grid[now_r][now_c] == 2:
            continue
        grid[now_r][now_c] = 2
        size += 1
        
        for dr, dc in [(1,0), (0,1), (-1,0), (0,-1)]:
            nxt_r, nxt_c = now_r+dr, now_c+dc
            
            if 0<= nxt_r < n and 0<= nxt_c < m and grid[nxt_r][nxt_c] == 1:
                stack.append((nxt_r, nxt_c))
                 
    return size

answer = 0 
for r in range(n):
    for c in range(m):
        if grid[r][c] == 1:
            answer = max(answer, DFS(r,c))
            
print(answer)