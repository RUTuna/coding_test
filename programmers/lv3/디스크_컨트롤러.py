from collections import deque
import heapq

# O(nlogn)
def solution(jobs):
    jobs = [(time, req, i) for i, (req, time) in enumerate(jobs)] # O(n)
    request = deque(sorted(jobs, key=lambda x: x[1])) # O(nlogn)
    wait = []
    now = 0
    total = 0
    
    while request or wait: # O(n)
        while request and request[0][1] <= now:
            heapq.heappush(wait, request.popleft()) # O(logn)
            
        if wait:
            run = heapq.heappop(wait) # O(logn)
            now = now + run[0]
            total += now-run[1]
        else:
            now = request[0][1]
                
    return total//len(jobs)