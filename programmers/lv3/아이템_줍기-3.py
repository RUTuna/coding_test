from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    characterX, characterY, itemX, itemY = characterX*2, characterY*2, itemX*2, itemY*2
    maps = [[0]*101 for _ in range(101)] # 밖 0 선 1 안 -1
    
    for lx, ly, rx, ry in rectangle:
        for x in range(lx*2, rx*2+1):
            for y in range(ly*2, ry*2+1):
                if x == lx*2 or x == rx*2 or y == ly*2 or y == ry*2:
                    maps[x][y] = -1 if maps[x][y] == -1 else 1
                else:
                    maps[x][y] = -1
    
    queue = deque([(characterX, characterY, 0)])
    visited = [[False]*101 for _ in range(101)]
    
    while queue:
        nowX, nowY, depth = queue.popleft()
        if visited[nowX][nowY]:
            continue
        visited[nowX][nowY] = True
        
        if nowX == itemX and nowY == itemY:
            return depth/2
        
        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            nx, ny = nowX+dx, nowY+dy
            
            if 0<=nx<=100 and 0<=ny<=100 and maps[nx][ny]>0 and not visited[nx][ny]:
                queue.append((nx,ny,depth+1))
    
    return 0