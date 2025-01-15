import sys
import heapq
from collections import defaultdict

def findMinDistance (n, start, graph):
    minDistance = [sys.maxsize]*(n+1)
    minDistance[start] = 0
    heap = [(0, start)]
    heapq.heapify(heap)
    
    while heap:
        cost, now = heapq.heappop(heap)
        if minDistance[now] < cost:
            continue
        for (nxt_cost, nxt) in graph[now]:
            new_cost = cost+nxt_cost
            if minDistance[nxt] > new_cost:
                minDistance[nxt] = new_cost
                heapq.heappush(heap, (new_cost, nxt))
    
    return minDistance
                

def solution(n, s, a, b, fares):
    distance = []
    graph = defaultdict(list)
    
    for [c, d, f] in fares:
        graph[c].append((f,d))
        graph[d].append((f,c))

    for start in [s, a, b]:
        distance.append(findMinDistance(n, start, graph))
    
    minDistance = sys.maxsize
    
    for i in range(1, n+1):
        minDistance = min(minDistance, distance[0][i]+distance[1][i]+distance[2][i])
    
    return minDistance