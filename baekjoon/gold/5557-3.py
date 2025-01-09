import sys
n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
dp = [[0]*21 for _ in range(n)] # dp[i][n] : i 번쨰 에서 n 을 만들 수 있는 식의 수
dp[0][numbers[0]] = 1

for i in range(1, n-1):
    for num in range(21):
        if dp[i-1][num] > 0:
            if num+numbers[i] <= 20:
                dp[i][num+numbers[i]] += dp[i-1][num]
            if num-numbers[i] >= 0:
                dp[i][num-numbers[i]] += dp[i-1][num]
                
print(dp[n-2][numbers[-1]])