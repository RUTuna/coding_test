def solution(n):
    dp = [0] * (n+1)
    dp[0] = 1
    
    for num in range(1, n+1):
        for i in range(num):
            dp[num] += dp[i]*dp[num-i-1]

    return dp[n]