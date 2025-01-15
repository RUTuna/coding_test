import sys

def solution(matrix_sizes):
    m = []
    for r, _ in matrix_sizes:
        m.append(r)
    m.append(matrix_sizes[-1][1])
    
    n = len(matrix_sizes)
    dp = [[sys.maxsize]*n for _ in range(n)]
    
    for i in range(n):
        dp[i][i] = 0
    
    for size in range(1, n):
        for start in range(n-size):
            end = start+size
            for k in range(start+1, end+1):
                dp[start][end] = min(dp[start][end], dp[start][k-1] + dp[k][end] + m[start]*m[k]*m[end+1])

    return dp[0][n-1]