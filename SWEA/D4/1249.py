import sys
sys.stdin = open("1249_input.txt", "r")

import heapq

def solve(board, size):
    INF = float('inf')
    cost = [[INF] * size for i in range(size)]
    cost[0][0] = 0
    queue = [(0, 0, 0)] # cost, row, col
    
    move = [(1,0),(0,1),(-1,0),(0,-1)]
    
    while queue:
        cur_cost, r,c = heapq.heappop(queue)
        if r == size-1 and r == c:
            return cur_cost
        
        for dr, dc in move:
            nr, nc = r + dr, c + dc
            if 0 <= nr < size and 0 <= nc < size:
                newCost = cur_cost + board[nr][nc]
                if newCost < cost[nr][nc]:
                    cost[nr][nc] = newCost
                    heapq.heappush(queue,(newCost, nr, nc))
        
    
    return cost[size-1][size-1]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    size = int(input())
    board = []
    
    for i in range(size):
        board.append([ int(x) for x in input()])
    
    ans = solve(board, size)
    
    print('#'+str(test_case), ans)