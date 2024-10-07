import sys
sys.stdin = open('1220_input.txt','r')

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    length = int(input())
    table = []
    
    for i in range(length):
        table.append(input().split())
    
    count = 0
    for c in range(length):
        isInner = False
        for r in range(length):
            if table[r][c] == '1' and not isInner:
                isInner = True
            
            elif table[r][c] == '2' and isInner:
                isInner = False
                count += 1
                
    print('#'+str(test_case), count)