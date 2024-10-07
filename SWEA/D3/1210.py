import sys
sys.stdin = open('1210_input.txt','r')



def solve(board):
    r = 99
    c = board[r].index('2')
    move = [(0,-1), (-1,0), (0,1)]
    dir = 1
    
    def checkTurn(x,y):
        return  0 <= y < 100 and board[x][y] == '1'
    
    while r > 0:
        r = r + move[dir][0]
        c = c + move[dir][1]
        
        if dir == 1:
            if checkTurn(r, c+1):
                dir = 2
            elif checkTurn(r, c-1):
                dir = 0
        
        elif dir == 0 or dir == 2:
            if board[r+1][c] == '1':
                dir = 1
    
    return c
        

T = 10

for test_case in range(1,T+1):
    board = []
    tc = input()
    for i in range(100):
        board.append(input().split())
    
    ans = solve(board)
    print('#'+tc, ans)