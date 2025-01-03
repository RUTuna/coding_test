from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    check = [[False]*m for _ in range(n)]
    queue = deque([[0,0,1]])
    direct = [[0,1], [1,0], [0,-1], [-1,0]]

    while queue:
        r, c, step = queue.popleft()
        if check[r][c]:
            continue
        check[r][c] = True
        if r == n-1 and c == m-1:
            return step

        for [dr, dc] in direct:
            nr = dr+r
            nc = dc+c
            
            if 0<=nr<n and 0<=nc<m and maps[nr][nc] and not check[nr][nc]:
                queue.append([nr,nc,step+1])   
    
    return -1