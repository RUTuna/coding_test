import sys
sys.stdin = open('1226_input.txt','r')

def solve(board):
    move = [(0,1),(1,0),(0,-1),(-1,0)]
    isPossible = False
    
    def DFS(x,y):
        nonlocal isPossible
        if board[x][y] == '3':
            isPossible = True
            return
        
        for dx, dy in move:
            nx, ny = x+dx, y+dy
            if 0 <= nx < 16 and 0 <= ny < 16 and board[nx][ny] != '1':
                board[x][y] = '1'
                DFS(nx,ny)
                board[x][y] = '0'
                
    DFS(1,1)
    
    return 1 if isPossible else 0

T = 10
for test_case in range(1, T+1):
    tc = input()
    board = []
    
    for i in range(16):
        board.append(list(input()))
    
    ans = solve(board)
    
    print('#'+tc, ans)
    
