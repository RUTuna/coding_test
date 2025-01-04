import heapq

# O(nlogn)
def solution(scoville, K):
    heapq.heapify(scoville) # O(n)
    answer = 0
    
    while len(scoville) > 1: # O(n)
        if scoville[0] >= K:
            return answer
        
        answer += 1
        first = heapq.heappop(scoville) # O(logn)
        second = heapq.heappop(scoville) # O(logn)
        heapq.heappush(scoville, first+2*second) # O(logn)

    return answer if scoville[0] >= K else -1