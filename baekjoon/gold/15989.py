import sys

t = int(sys.stdin.readline())
dp = [1] * 10001

for n in (2,3):
    for i in range(10001):
        if i-n >= 0:
            dp[i] += dp[i-n]

for _ in range(t):
    num = int(sys.stdin.readline())
    print(dp[num])