import sys
sys.stdin = open("3752_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    scores = list(map(int, input().split()))
    maxScore = sum(scores)
    dp = [False for i in range(maxScore+1)]
    dp[0] = True
    
    for score in scores:
        for s in range(maxScore, score-1, -1):
            if dp[s - score]:
                dp[s] = True
    
    print('#'+str(test_case), len(list(filter(lambda x: x, dp))))