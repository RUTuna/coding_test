import sys

n,k = map(int, sys.stdin.readline().split())
dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    w, v = map(int, sys.stdin.readline().split())
    
    for limit in range(1, k+1):
        if limit < w:
            dp[i][limit] = dp[i-1][limit]
        else:
            dp[i][limit] = max(dp[i-1][limit], dp[i-1][limit-w]+v)

print(dp[n][k])