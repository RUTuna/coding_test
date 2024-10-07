import sys

n = int(sys.stdin.readline())
m = []
dp = [[0] * n for _ in range(n)] 
a, b = 0,0

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    m.append(a)

m.append(b)

for diff in range(1,n):
    for i in range(n-diff):
        min_val = sys.maxsize
        for d in range(i,i+diff):
            min_val = min(min_val, dp[i][d] + dp[d+1][i+diff] + m[i]*m[d+1]*m[i+diff+1])
        dp[i][i+diff] = min_val if min_val!=sys.maxsize else 0

print(dp[0][n-1])