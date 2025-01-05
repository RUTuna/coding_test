from collections import defaultdict
import heapq

def solution(n, costs):
    graph = defaultdict(list)
    
    for s, d, c in costs:
        graph[s].append((c, d))
        graph[d].append((c, s))
    
    cost = 0
    nodes = set([0])
    edges = graph[0]
    heapq.heapify(edges)
    
    while len(nodes) < n:
        cheap = heapq.heappop(edges)
        
        if cheap[1] in nodes:
            continue
        
        for e in graph[cheap[1]]:
            if not e[1] in nodes:
                heapq.heappush(edges, e)
                
        cost += cheap[0]
        nodes.add(cheap[1])
    
    return cost