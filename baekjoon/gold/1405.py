import sys
sys.setrecursionlimit(10000)

step, E, W, S, N = map(int, sys.stdin.readline().split())
prob = [E*0.01, W*0.01, S*0.01, N*0.01]
dx = [0, 0, 1, -1]  
dy = [1, -1, 0, 0]
visited = [[False] * (2*step+1) for _ in range(2*step+1)]

def DFS(depth, x, y):
    if depth == step:
        return 1.0
    
    visited[x][y] = True
    now_prob = 0.0
    
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if not visited[nx][ny] and prob[i] != 0:
            now_prob += DFS(depth+1, nx, ny) * prob[i]
    
    visited[x][y] = False
    return now_prob

print(DFS(0, step,step))