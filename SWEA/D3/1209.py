import sys
sys.stdin = open("1209_input.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    tc = input()
    board = []
    rowMax = 0
    cols = [0] * 100
    diagonal, antiDiagonal = 0, 0
    
    for i in range(100):
        row = list(map(int, input().split()))
        board.append(row)
        
        diagonal += row[i]
        antiDiagonal += row[-(i+1)]
        
        rowMax = max(rowMax, sum(row))
        cols = [ cols[j]+row[j] for j in range(100) ]
        
    print('#'+tc, max(rowMax, *cols, diagonal, antiDiagonal))    