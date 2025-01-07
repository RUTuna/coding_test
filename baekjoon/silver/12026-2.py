import sys

n = int(sys.stdin.readline())
road = sys.stdin.readline()

def solution(n, road):
    if n == 1:
        return 0
    
    dp = [sys.maxsize] * n
    dp[0] = 0
    order = {'B':"O", "O":'J', 'J':'B'}
    
    for i in range(n):
        target = order[road[i]]
        
        for j in range(i+1, n):
            if road[j] == target:
                dp[j] = min(dp[j], dp[i]+pow((j-i),2))
    
    return -1 if dp[-1] == sys.maxsize else dp[-1]

print(solution(n, road))    
