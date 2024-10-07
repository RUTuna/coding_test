import sys

n, s, m = map(int, sys.stdin.readline().split())
vloumns = list(map(int,sys.stdin.readline().split()))
dp = [set() for _ in range(n+1)]
dp[0].add(s)

for music in range(n):
    for now in dp[music]:
        for d in (vloumns[music], -vloumns[music]):
            if 0 <= now+d <= m:
                dp[music+1].add(now+d)
                
print(max(dp[n]) if len(dp[n]) else -1)