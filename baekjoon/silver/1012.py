import sys

t = int(sys.stdin.readline())
move = [(1,0), (0,1), (-1,0), (0,-1)]

def isAble(y, x, n, m):
    return y > -1 and y < n and x > -1 and x < m

def DFS(grid, start_y, start_x, n, m):
    stack = [(start_y, start_x)]
                
    while stack:
        now_y, now_x = stack.pop()
        
        if grid[now_y][now_x] == 2: # 방문했다면
            continue
        
        grid[now_y][now_x] = 2
        
        for dy, dx in move:
            nxt_y, nxt_x = now_y + dy, now_x + dx
            
            if isAble(nxt_y, nxt_x, n, m) and grid[nxt_y][nxt_x] == 1:
                stack.append((nxt_y, nxt_x))
    
    
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    grid = [ [0] * m for _ in range(n)]
    count = 0
        
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        grid[y][x] = 1
        
    for y in range(n):
        for x in range(m):
            if grid[y][x] == 1:
                count += 1
                DFS(grid, y, x, n, m)  
                
    print(count)

