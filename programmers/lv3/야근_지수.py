import heapq

def solution(n, works):
    time = [-i for i in works]
    heapq.heapify(time)
    remind = n
    
    while remind > 0 and time:
        bigger = heapq.heappop(time)
        if bigger + 1 < 0:
            heapq.heappush(time, bigger+1)
        remind -= 1

    answer = 0
    for i in time:
        answer += i**2
        
    return answer