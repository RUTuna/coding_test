def solution(cookie):
    n = len(cookie)
    dp = [[0]*n for _ in range(n)]
    
    def find(m):
        left, right = m, m+1
        leftSum, rightSum = cookie[left], cookie[right]
        maxValue = 0
        
        while left >=0 and right < n:
            if leftSum == rightSum:
                maxValue = max(maxValue, leftSum)
            
            if leftSum >= rightSum:
                right += 1
                if right < n:
                    rightSum += cookie[right]
            else:
                left -= 1
                if left >= 0:
                    leftSum += cookie[left]
                
        return maxValue
                
    answer = 0
    for m in range(n-1):
        answer = max(answer, find(m))

    return answer