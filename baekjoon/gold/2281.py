import sys
sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split())
note = []
maxNum = m**2 * n
dp = [maxNum] * (n+1) # i+1 번째 이름을 첫번째 줄에 썼을 때 최소값
dp[n] = 0

for _ in range(n):
    note.append(int(sys.stdin.readline()))

def calculation(index):
    if dp[index] < maxNum:
        return dp[index]
    
    remain = m-note[index]
    for j in range(index+1, n+1): # j-1 까지 이어서 씀
        if remain < 0:
            break
        if j == n: # 마지막 줄은 0
            dp[index] = 0
            break
        dp[index] = min(dp[index], remain**2 + calculation(j))
        remain -= note[j]+1
    
    return dp[index]
    
print(calculation(0))