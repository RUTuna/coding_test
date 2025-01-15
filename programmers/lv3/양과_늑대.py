from collections import defaultdict

def solution(info, edges):
    max_sheep = 0
    graph = defaultdict(list)
    
    for s, d in edges:
        graph[s].append(d)
    
    def DFS(now, sheep, wolf, possible):
        nonlocal max_sheep

        if info[now]:
            wolf+=1
        else:
            sheep+=1
            
        if sheep <= wolf:
            return
        
        max_sheep = max(max_sheep, sheep)
        
        next_possible = possible.copy()
        next_possible.remove(now)
        next_possible += graph[now]
        
        for nxt in next_possible:
            DFS(nxt, sheep, wolf, next_possible)
    
    DFS(0,0,0,[0])
    
    return max_sheep