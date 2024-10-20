import heapq
from collections import deque

def solution(n, paths, gates, summits):
    dic = {i: [] for i in range(1, n+1)}
    notlist = {}
    
    # 중간에 들리면 안되는 리스트
    for gate in gates:
        notlist[gate] = True
    for summit in summits:
        notlist[summit] = True
    
    # 링크드 리스트 구현
    for i, j, w in paths:
        dic[i].append((j,w))
        dic[j].append((i,w))
           
            
    def dijkstra():
        cost = [float('inf')] * (n+1)
        heap = []
        
        # 출입구들을 모두 시작점으로 설정
        for gate in gates:
            heapq.heappush(heap, (0, gate))
            cost[gate] = 0
            
        while heap:
            curr_cost, index = heapq.heappop(heap)
            
            # 현재 cost보다 크다면 continue
            if curr_cost > cost[index]:
                continue
            
            for nxt, nxt_cost in dic[index]:
                new_cost = max(curr_cost, nxt_cost)
                if new_cost < cost[nxt]:
                    cost[nxt] = new_cost
                    if nxt not in notlist:
                        heapq.heappush(heap, (new_cost, nxt))
        
        
        res = [0, float('inf')]
        for summit in sorted(summits):
            if res[1] > cost[summit]:
                res = [summit, cost[summit]]
                
        return res
            

    answer = dijkstra()
    
    
    return answer