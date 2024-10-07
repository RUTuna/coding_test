import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
dp = [[0] * 21 for _ in range(n)]; # dp[i][j] 처음부터 i개 써서 j 만들 수 있는 경우의 수
dp[0][numbers[0]] = 1;

for i in range(1,n-1):
    for j in range(21):
        if 0<=j-numbers[i]<=20:
            dp[i][j-numbers[i]] += dp[i-1][j]
        if 0<=j+numbers[i]<=20:
            dp[i][j+numbers[i]] += dp[i-1][j]
            
print(dp[n-2][numbers[n-1]])