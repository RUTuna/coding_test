n = int(input())
dp = [0] * 5000
dp[0] = 1

for i in range(2501):
    for j in range(i):
        dp[i] += dp[j]*dp[i-j-1]
    dp[i] %= 1000000007
    
for _ in range(n):
    num = int(input())
    if num % 2:
        print(0)
    else:
        print(dp[num//2])