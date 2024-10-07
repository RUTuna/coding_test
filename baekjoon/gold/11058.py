n = int(input())
dp = [ i for i in range(n+1)]

for i in range(1, n+1):
    k=3
    dp[i]=dp[i-1]+1
    while i-k>0:
        dp[i]=max(dp[i], dp[i-k]*(k-1))
        k+=1

print(dp[n])