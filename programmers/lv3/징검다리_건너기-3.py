from collections import deque

def solution(stones, k):
    answer = 200000001
    window = deque()
    
    for i, item in enumerate(stones):
        if window and window[0][0] <= i-k:
            window.popleft()
        
        # 내림차순 정렬
        while window and window[-1][1] < item:
            window.pop()
        
        window.append((i, item))
        
        if i>=k-1:
            answer = min(answer, window[0][1])
        
    return answer