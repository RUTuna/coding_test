import sys

num, e, w, s, n = map(int, sys.stdin.readline().split())
l = 2*num+1
probability = [0.01*p for p in (e,w,s,n)]
direction = [(0,1), (0,-1), (1,0), (-1,0)]
visitied = [[False]*(l) for _ in range(l)]
answer = 1.0

def DFS(r, c, depth):
    global answer
    
    if depth == num:
        return 1.0
    
    nowProb = 0.0
    
    visitied[r][c] = True
    for i, (dr, dc) in enumerate(direction):
        nr, nc = r+dr, c+dc
        if 0<=nr<l and 0<=nc<l and not visitied[nr][nc] and probability[i]>0:
            nowProb += DFS(nr, nc, depth+1)*probability[i]
    visitied[r][c] = False
    return nowProb
    
print(DFS(num,num,0))