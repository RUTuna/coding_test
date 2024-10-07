import sys
sys.stdin = open("1215_input.txt", "r")


def check(string): 
    rev = list(string)      
    rev.reverse()
    return list(string) == rev
        
    
T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    board = []
    count = 0
    for t in range(8):
        row = input()
        board.append(row)
        for i in range(8 - (n-1)):
            if row[i] == row[i+n-1]:
                count += int(check(row[i:i+n]))
    
    board = list(map(list,zip(*board)))
    
    for col in board:
        for i in range(8 - (n-1)):
            if col[i] == col[i+n-1]:
                count += int(check(col[i:i+n]))
    
    print('#'+str(test_case),count)