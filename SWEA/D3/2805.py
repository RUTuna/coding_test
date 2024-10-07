import sys
sys.stdin = open("2805_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    sum = 0
    isDecrease = True
    index = n // 2
    
    for i in range(n):
        r = input()
        if index < 0:
            index = 1
            isDecrease = False
        start = index
        while start < n-index:
            sum += int(r[start])
            start += 1
        index -= 1 if isDecrease else -1
        
    print('#'+str(test_case), sum)
            
