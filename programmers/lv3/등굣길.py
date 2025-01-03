def solution(m, n, puddles):
    dp = [[0]*m for _ in range(n)]
    maps = [[True]*m for _ in range(n)]
    dp[0][0] = 1
    
    for y, x in puddles:
        maps[x-1][y-1] = False
    
    for x in range(n):
        for y in range(m):
            if maps[x][y]:
                if 0<=x-1:
                    dp[x][y] += dp[x-1][y]
                if 0<=y-1:
                    dp[x][y] += dp[x][y-1]
    
    return dp[-1][-1]%1000000007