def solution(triangle):
    dp = [[-1]*i for i in range(1,len(triangle)+1)]
    dp[0][0] = triangle[0][0]
    
    for childX in range(1, len(triangle)):
        for childY in range(childX+1):
            dp[childX][childY] = triangle[childX][childY]
            if childY == 0:
                dp[childX][childY] += dp[childX-1][childY]
            elif childY == childX:
                dp[childX][childY] += dp[childX-1][childY-1]
            else:
                dp[childX][childY] += max(dp[childX-1][childY], dp[childX-1][childY-1])
                
    return max(dp[-1])