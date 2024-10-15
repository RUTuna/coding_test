import sys

n = int(sys.stdin.readline())
matrix = []
dp = [[0]*n for _ in range(n)]

for i in range(n):
    matrix[i:i+2] = list(map(int, sys.stdin.readline().split()))

for k in range(1,n):
    for i in range(n-k):
        for j in range(i,i+k):
            if dp[i][i+k]:
                dp[i][i+k] = min(dp[i][i+k], dp[i][j]+matrix[i]*matrix[j+1]*matrix[i+k+1]+dp[j+1][i+k])
            else:
                dp[i][i+k] = dp[i][j]+matrix[i]*matrix[j+1]*matrix[i+k+1]+dp[j+1][i+k]

            
print(dp[0][-1])