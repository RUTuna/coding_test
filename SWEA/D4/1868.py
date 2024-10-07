import sys
sys.stdin = open("1868_input.txt", "r")

from collections import deque

def solve(board, n):
    move = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
    fourMove = [(0,1),(1,0),(0,-1),(-1,0)]
    island = 0
    
    def findZero(x,y):
        board[x][y] = '-1'
        for dx, dy in fourMove:
            nx, ny = x+dx, y+dy 
            if 0<= nx < n and 0<= ny < n and board[nx][ny] == '0':
                findZero(nx, ny)
        
    for r in range(n):
        for c in range(n):
            if board[r][c] == '*':
                continue
            sum = 0
            for dx, dy in move:
                nx, ny = r+dx, c+dy
                if 0<= nx < n and 0<= ny < n and board[nx][ny] == '*':
                    sum+=1
            board[r][c] = '0' if sum == 0 else '1'
    
    # for b in board:
    #     print(b)
        
    for r in range(n):
        for c in range(n):
            if board[r][c] == '0':
                island+=1
                findZero(r,c)
      
    # for b in board:
    #     print(b)
                   
    for r in range(n):
        for c in range(n):
            if board[r][c] == '1':
                for dx, dy in move:
                    nx, ny = r+dx, c+dy
                    if 0<= nx < n and 0<= ny < n and board[nx][ny] == '-1':
                        # print(r,c)
                        board[r][c] = '-2'
                        break
    
    # for b in board:
    #     print(b)
    count = 0
    for row in board:    
        cnt = row.count('1')
        count += cnt if cnt > 0 else 0
        
    print(count + island)
                    
    
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    board = []
    for i in range(n):
        board.append(list(input()))
        
    solve(board, n)
    