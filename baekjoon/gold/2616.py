n = int(input())
trains = list(map(int, input().split()))
maxTrains = int(input())
dp = [ [0]*4 for _ in range(n+1)] # dp[i][k] : i번째 객차까지 n개의 소형기관차를 고려했을 때 최대값
current_sum = [ sum(trains[i-maxTrains:i]) if i-maxTrains >= 0 else sum(trains[:i]) for i in range(0, n+1) ] # Trains[i-maxTrains:i+1] 의 합

for now in range(1,4):
    for t in range(maxTrains, n+1):
        dp[t][now] = max(dp[t-1][now], dp[t-maxTrains][now-1] + current_sum[t])
        
print(dp[n][3])