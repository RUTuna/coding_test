import sys
sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split())
names = []
for _ in range(n):
    names.append(int(sys.stdin.readline()))

dp = [sys.maxsize] * (n+1) # dp[i]: i 를 첫번째 줄로 하고 (n-1)번째 이름까지 작성했을 때 최소값
dp[n] = 0

def calculate(index):
    if dp[index] != sys.maxsize:
        return dp[index]
    
    remain = m - names[index]
    for j in range(index+1, n+1):
        if remain < 0:
            break
        if j == n: # n 번째 이름은 없으므로, index 번째부터 (n-1)번째 이름까지 마지막 줄에 썼다는 의미
            dp[index] = 0
            break
        
        dp[index] = min(dp[index], calculate(j) + remain**2)
        remain -= names[j]+1 # 띄어쓰기
        
    return dp[index]

print(calculate(0))