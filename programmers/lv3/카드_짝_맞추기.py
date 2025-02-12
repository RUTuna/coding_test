from collections import deque

def solution(board, firstR, firstC):
    cardSet = set()
    for r in range(4):
        for c in range(4):
            cardSet.add(board[r][c])
    cardSet.remove(0)

    visited = set()
    queue = deque([((firstR,firstC), cardSet, 0, (-1,-1), board, 0)])
    
    def nextPos(r, c, nowBoard):
        nextPosSet = set()
        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
            nr, nc = dr+r, dc+c
            if 0<=nr<4 and 0<=nc<4:
                nextPosSet.add((nr,nc))
                
            while 0<=nr<4 and 0<=nc<4 and nowBoard[nr][nc]==0:
                nr += dr
                nc += dc
            if not(0<=nr<4 and 0<=nc<4):
                nr-=dr
                nc-=dc
            nextPosSet.add((nr,nc))
        
        return list(nextPosSet)
        
    while queue:
        nowPos, restCard, openCard, openPos, nowBoard, step = queue.popleft()
        if len(restCard) == 0:
            return step
        
        if (nowPos, tuple(restCard), openCard, openPos) in visited:
            continue
        visited.add((nowPos, tuple(restCard), openCard, openPos))
        
        # 카드 뒤집는 경우
        nextBoard = [r[:] for r in nowBoard]
        nextBoard[nowPos[0]][nowPos[1]] = 0
        if openCard>0 and openCard == nowBoard[nowPos[0]][nowPos[1]]: # 현재 카드랑 동일
            queue.append((nowPos, restCard-{openCard}, 0, nowPos, nextBoard, step+1))
            continue
            
        if openCard == 0 and nowBoard[nowPos[0]][nowPos[1]]>0:
            queue.append((nowPos, restCard, nowBoard[nowPos[0]][nowPos[1]], nowPos, nextBoard, step+1))
            
        
        # 이동하는 경우
        nextPosSet = nextPos(nowPos[0], nowPos[1], nowBoard)
        for nr, nc in nextPosSet:
            queue.append(((nr,nc), restCard, openCard, openPos, nowBoard, step+1))
                    
    answer = 0
    return answer