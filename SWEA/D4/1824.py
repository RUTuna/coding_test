import sys
sys.stdin = open('1824_input.txt','r')

from collections import deque

def solve(codes, rows, cols):
    visited = [[[ [False for _ in range(16)] for _ in range(4)] for _ in range(cols)] for _ in range(rows)] # URDL
    moves = [(-1,0),(0,1),(1,0),(0,-1)]
    isPossible = False
    queue = deque()
    queue.append((0,0,0,1))
    
    while queue:
        x,y, memory, direction = queue.popleft()
        now = codes[x][y]
        
        if now == '@':
            isPossible = True
            break
        
        if visited[x][y][direction][memory]:
            continue
        visited[x][y][direction][memory] = True
        
        if now == '?':
            for i, (dx, dy) in enumerate(moves):
                nx, ny = (x+dx)%rows, (y+dy)%cols
                queue.append((nx,ny,memory, i))
            
        else:
            if now.isdigit():
                memory = int(now)
            if now == '^' :
                direction = 0
            elif now == '>' :
                direction = 1
            elif now == 'v' :
                direction = 2
            elif now == '<' :
                direction = 3
        
            elif now == '_':
                direction = 1 if memory == 0 else 3
            elif now == '|':
                direction = 2 if memory == 0 else 0
                
            elif now == '+':
                memory = (memory + 1) % 16
            elif now == '-':
                memory = (memory - 1 + 16) % 16
                

            nx, ny = (x+moves[direction][0])%rows, (y+moves[direction][1])%cols
            queue.append((nx,ny, memory, direction))
              
        
    
    return 'YES' if isPossible else 'NO'

T = int(input())

for test_case in range(1, T+1):
    rows, cols = list(map(int, input().split()))
    codes = []
    havetoFinished = 0
    
    for i in range(rows):
        row = input()
        havetoFinished += row.find('@')
        codes.append(row)
        

    ans =  'NO' if havetoFinished == -1*rows  else solve(codes, rows, cols)
    print('#'+str(test_case), ans)