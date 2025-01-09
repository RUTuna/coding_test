import sys
import heapq
from collections import defaultdict

def solution(n, paths, gates, summits):
    graph = defaultdict(list)
    cant = set(gates+summits)
    
    for i, j, w in paths:
        graph[i].append((w,j))
        graph[j].append((w,i))
    
    heap = []
    distance = [sys.maxsize] * (n+1)
    for gate in gates:
        heapq.heappush(heap, (0,gate))
        distance[gate] = 0
    
    while heap:
        cost, now = heapq.heappop(heap)
        if cost > distance[now]:
            continue
            
        for nxt_cost, nxt in graph[now]:
            new_cost = max(nxt_cost, cost)
            if new_cost < distance[nxt]:
                distance[nxt] = new_cost
                if not nxt in cant:
                    heapq.heappush(heap, (new_cost, nxt))              
    
    answer = [n+1, 10000001]
    summits.sort()
    for s in summits:
        if answer[1] > distance[s]:
            answer = [s, distance[s]]
            
    return answer