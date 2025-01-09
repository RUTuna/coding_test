import sys

n = int(sys.stdin.readline())
dp = [0]*(n+1)

for i in range(1, n+1):
    dp[i] = dp[i-1] + 1
    for k in range(3, i):
        dp[i] = max(dp[i], dp[i-k]+dp[i-k]*(k-2))

print(dp[n])