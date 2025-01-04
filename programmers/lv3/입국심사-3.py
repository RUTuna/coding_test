def solution(n, times):
    answer = 0
    
    left = min(times)
    right = max(times)*n
    
    while left <= right:
        mid = (left+right)//2
        
        ans = 0
        for t in times:
            ans += mid//t
        
        if ans >= n:
            answer = mid
            right = mid-1
        else:
            left = mid+1
    
    return answer