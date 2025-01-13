import math

def solution(a, b, g, s, w, t):
    n = len(g)
    left, right = 0, 10**17
    answer = right
    
    while left <= right:
        mid = (left+right)//2
        
        totalSilver = 0
        totalGold = 0
        total = 0
        
        for i in range(n):
            time = mid//t[i]
            time = math.ceil(time/2)
            
            totalSilver += min(s[i], w[i]*time)
            totalGold += min(g[i], w[i]*time)
            total += min(s[i]+g[i], w[i]*time)
            
        if totalSilver >= b and totalGold >= a and total >= a+b:
            answer = mid
            right = mid-1
        else:
            left = mid+1
    
    return answer