import sys

n, E, W, S, N = map(int, sys.stdin.readline().split())
probability = list(map(lambda x: x*0.01, [E, W, S, N]))
visited = [[False]*29 for _ in range(29)]
answer = 1

def DFS(prob, depth, r, c):
    global answer
    if depth > n:
        return
    
    if visited[r][c]:
        answer -= prob
        return
    
    visited[r][c] = True
    for i, (dr, dc) in enumerate([(0,1), (0,-1), (1,0), (-1,0)]):
        nr, nc = r+dr, c+dc
        if probability[i] > 0:
            DFS(prob*probability[i], depth+1, nr, nc)
    visited[r][c] = False
DFS(1,0,14,14)
print(answer)