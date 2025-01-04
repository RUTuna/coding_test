def solution(distance, rocks, n):
    if n == len(rocks):
        return distance
    rocks.sort()
    rocks = [0] + rocks + [distance]
    
    answer = 0
    left, right = 0, distance
    
    while left <= right:
        mid = (left+right) // 2
        count = 0
        prevPos = 0
        
        for i in range(1, len(rocks)):
            if rocks[i]-prevPos < mid:
                count += 1
            else:
                prevPos = rocks[i]
                
        if count > n:
            right = mid-1
        else:
            answer = mid
            left = mid+1
        
    return answer