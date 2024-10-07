import sys
sys.stdin = open("1861_input.txt", "r")

def solve(board,n):
    answers = []
    move = [(0,1),(1,0),(0,-1),(-1,0)]
    
    def DFS(x,y,depth):
        target = board[x][y] + 1
        for dx, dy in move:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<n and board[nx][ny]==target:
                _, ans = DFS(nx,ny, depth+1)
                return (board[x][y], ans)
            
        return (board[x][y],depth)
        
    for i in range(n):
        for j in range(n):
            answers.append(DFS(i,j,1))
            
    answers.sort(key=lambda x: (x[1], -x[0]), reverse=True)

    return answers[0]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    board = []
    
    for i in range(n):
        board.append(list(map(int,input().split())))
        
    startPoint, maxNum = solve(board, n)
    print("#"+str(test_case), startPoint, maxNum)