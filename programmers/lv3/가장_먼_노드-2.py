from collections import deque

def solution(n, edge):
    maps = {i:set() for i in range(1,n+1)}
    visited = [0] * (n+1)
    max_value = 0
    
    for [s, d] in edge:
        maps[s].add(d)
        maps[d].add(s)
    
    depth = 1
    queue = deque([(1,depth)])
    
    while queue:
        now, depth = queue.popleft()
        
        if visited[now]:
            continue
        
        if depth > n:
            continue
        
        max_value = max(max_value, depth)
        visited[now] = depth
        for nxt in maps[now]:
            if not visited[nxt]:
                queue.append((nxt, depth+1))
                
    return len(list(filter(lambda x: x==max_value, visited)))