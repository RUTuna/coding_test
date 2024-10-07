import sys

n = int(sys.stdin.readline())
maps = []
dp = [[0] * n  for _ in range(n)]
dp[0][0] = 1

for _ in range(n):
    maps.append(list(map(int, sys.stdin.readline().split())))

for r in range(n):
    for c in range(n):
        distance = maps[r][c]
        if distance > 0:
            if r+distance < n:
                dp[r+distance][c] += dp[r][c]
            if c+distance < n:
                dp[r][c+distance] += dp[r][c]

print(dp[n-1][n-1])
