import sys

n,k = map(int, sys.stdin.readline().split())
dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1,n+1):
    w, v = map(int, sys.stdin.readline().split())
    for we in range(k+1):
        dp[i][we] = dp[i-1][we] if we-w < 0 else max(dp[i-1][we], dp[i-1][we-w]+v)
        
print(dp[n][k])