import sys

n = int(sys.stdin.readline())
w = []
h = []
for _ in range(n):
    width, height = map(int, sys.stdin.readline().split())
    w.append(width)
    h.append(height)
    
dp = [[sys.maxsize]*n for _ in range(n)]
for i in range(n):
    dp[i][i] = 0

for size in range(1, n):
    for s in range(n-size):
        d = s+size
        for i in range(s, d):
            dp[s][d] = min(dp[s][d], dp[s][i] + w[s]*h[i]*h[d] + dp[i+1][d])

print(dp[0][n-1])