import sys

def solution(board, aloc, bloc):
    n = len(board)
    m = len(board[0])
    
    def DFS(step, now, nxt):
        if board[now[0]][now[1]] == 0: 
            return [False, step]
        
        minStep = sys.maxsize
        maxStep = step
        canWin = False
        
        board[now[0]][now[1]] = 0
        oppsiteWin = False
        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
            nr, nc = now[0]+dr, now[1]+dc
            if 0<=nr<n and 0<=nc<m and board[nr][nc]:
                [oppsiteWin, value] = DFS(step+1, nxt, (nr,nc))
                if oppsiteWin:
                    maxStep = max(maxStep, value)
                else:
                    canWin = True
                    minStep = min(minStep, value) 
        board[now[0]][now[1]] = 1

        return [canWin, minStep if canWin else maxStep]
    
    _, answer = DFS(0, aloc, bloc)
    
    return answer