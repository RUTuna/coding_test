import sys
from collections import deque

def solution(board):
    n = len(board)
    visited = [[sys.maxsize]*n for _ in range(n)]
    direct = [(0,1), (1,0), (0,-1), (-1,0)]
    queue = deque([(0,0,0,0), (0,0,1,0)])
    visited[0][0] = 0
    
    while queue:
        r, c, d, cost = queue.popleft()
        if r == c == n-1:
            continue
        
        for i, (dr, dc) in enumerate(direct):
            nr, nc = dr+r, dc+c
            nxtCost = cost + (100 if i==d else 600)
            if 0<=nr<n and 0<=nc<n and board[nr][nc]==0 and visited[nr][nc]+500 > nxtCost:
                visited[nr][nc] = min(nxtCost, visited[nr][nc])
                queue.append((nr,nc,i,nxtCost))
                
    return visited[-1][-1]