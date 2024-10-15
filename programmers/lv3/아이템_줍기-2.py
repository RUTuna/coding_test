from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    [characterX, characterY, itemX, itemY] = [i*2 for i in (characterX, characterY, itemX, itemY)]
    maps = [[-1]*102 for _ in range(102)]
    
    def painting(sr, sc, er, ec):
        for r in range(sr, er+1):
            for c in range(sc, ec+1):
                if r == sr or r == er or c == sc or c == ec: # 가장자리
                    maps[r][c] = abs(maps[r][c])
                else:
                    maps[r][c] = 0
    
    for (sr, sc, er, ec) in rectangle:
        painting(sr*2, sc*2, er*2, ec*2)
        
    queue = deque([(characterX, characterY, 0)])
    
    while queue:
        r, c, depth = queue.popleft()
        if maps[r][c] != 1:
            continue
            
        maps[r][c] = 0
        
        if r==itemX and c==itemY:
            answer = depth//2
            break
        
        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
            nr, nc = r+dr, c+dc
            if 0<=nr<102 and 0<=nc<102 and maps[nr][nc] == 1:
                queue.append((nr,nc, depth+1))
    
    return answer