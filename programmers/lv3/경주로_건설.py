import sys
from collections import deque

def solution(board):
    n = len(board)
    direction = [(0,1), (1,0), (0,-1), (-1,0)]
    
    def BFS(start):
        nonlocal n
        
        queue = deque(start)
        visited = [[sys.maxsize] *n for _ in range(n)]
        visited[0][0] = 0
    
        while queue:
            (x,y), di, cost = queue.popleft()

            for i in range(4):
                newX, newY = x+direction[i][0], y+direction[i][1]

                newCost = cost + (100 if i == di else 600)
                if 0<=newX<n and 0<=newY<n and board[x][y] == 0 and visited[newX][newY] > newCost:
                    visited[newX][newY] = newCost
                    queue.append([(newX, newY), i, newCost])

        return visited[-1][-1]
    
    return min(BFS([[(0,0),0,0]]), BFS([[(0,0),1,0]]))