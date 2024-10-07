import sys
from collections import deque

sys.stdin = open("1868_input.txt", "r")

direct = [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)]

def changeBoard(board, n):
    changed = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == '*': 
                changed[i][j] = board[i][j]
            else:
                count = 0
                for di, dj in direct:
                    new_i, new_j = di+i, dj+j
                    if 0<=new_i<n and 0<=new_j<n and board[new_i][new_j]=='*':
                        count+=1
                changed[i][j] = count
    return changed

def solve(board, n):
    newBoard = changeBoard(board, n)
    visited = [[False] * n for _ in range(n)]
    answer = 0
    
    def BFS(start):
        queue = deque([start])
        
        while queue:
            now_i, now_j = queue.popleft()
            if visited[now_i][now_j]:
                continue
            visited[now_i][now_j] = True
            
            for di, dj in direct:
                new_i, new_j = di+now_i, dj+now_j
                if 0<=new_i<n and 0<=new_j<n and not visited[new_i][new_j]: # 현재 0이니 인접한 것은 숫자 아니면 0임
                    if newBoard[new_i][new_j]==0:
                        queue.append((new_i,new_j))
                    else:
                        visited[new_i][new_j] = True
                
    
    # 0섬 찾기
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and newBoard[i][j]==0:
                answer+=1
                BFS((i,j))
    
    # 방문하지 않고 남아있는 숫자 찾기
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and type(newBoard[i][j]) is int:
                answer+=1
    
    return answer
        

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    board = []
    for i in range(n):
        board.append(list(input()))
        
    print('#'+str(test_case), solve(board, n))