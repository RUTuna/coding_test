import sys

n = int(sys.stdin.readline())
dp = [0] * (n+1) # i일에 퇴사할 때 얻는 이득의 최댓값

for d in range(n):
    t, p = map(int, sys.stdin.readline().split())
    if d > 0:
        dp[d] = max(dp[d], dp[d-1])
    if d+t <= n:
        dp[d+t] = max(dp[d+t], dp[d]+p)

    
print(max(dp))