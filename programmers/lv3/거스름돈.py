def solution(n, money):
    dp = [0]*(n+1)
    dp[0] = 1
    
    for coin in money:
        for i in range(n+1):
            if i+coin <= n:
                dp[i+coin] += dp[i]
                
    return dp[n]