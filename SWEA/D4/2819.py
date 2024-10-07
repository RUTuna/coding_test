import sys
sys.stdin = open("2819_input.txt", "r")

from collections import deque


def solve(board):
    numbers = set()
    move = [(1,0), (0,1), (-1,0), (0,-1)]
    queue = deque()
    
    
    for i in range(4):
        for j in range(4):
            queue.append((board[i][j],i,j))

    while queue:
        path, x,y = queue.popleft()
        if len(path) == 7:
            numbers.add(path)
        
        else:
            for i in range(4):
                nx , ny = x+move[i][0], y+move[i][1]
                if 0 <= nx < 4 and 0 <= ny < 4:
                    
                    queue.append((path+board[nx][ny], nx, ny))

    return len(numbers)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    board = []
    
    for i in range(4):
        board.append(input().split())
    
    ans = solve(board)
    
    print('#'+str(test_case), ans)