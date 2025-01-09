import sys

l = int(sys.stdin.readline())
dp = [0]*5000
dp[0] = 1

def calculate(number):
    if dp[number] > 0:
        return dp[number]
    
    for i in range(number):
        dp[number] += calculate(i)*calculate(number-i-1)
    dp[number] %= 1000000007
    return dp[number] 

for _ in range(l):
    num = int(sys.stdin.readline())
    if num % 2:
        print(0)
    else:
        print(calculate(num//2))