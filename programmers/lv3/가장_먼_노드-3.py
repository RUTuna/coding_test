from collections import defaultdict, deque

def solution(n, edge):
    distance = [0]*(n+1)
    distance[1] = 1
    graph = defaultdict(set)
    
    for s, d in edge:
        graph[s].add(d)
        graph[d].add(s)
    
    queue = deque([1])
    maxDistance = 0
    
    while queue:
        node = queue.popleft()
        
        for e in graph[node]:
            if distance[e] == 0:
                distance[e] = distance[node]+1
                maxDistance = max(maxDistance, distance[e])
                queue.append(e)
    
    answer = 0
    for d in distance:
        if d == maxDistance:
            answer += 1

    return answer