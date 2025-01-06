import sys

def solution(n, results):
    distance = [[sys.maxsize]*n for _ in range(n)]
    
    for i in range(n): # O(n)
        distance[i][i] = 0
    
    for w, l in results: # O(m)
        distance[w-1][l-1] = 1
    
    for i in range(n): # O(n^3)
        for a in range(n):
            for b in range(n):
                distance[a][b] = min(distance[a][b], distance[a][i]+distance[i][b])
    
    
    answer = n
    for a in range(n): # O(n^2)
        can = True
        for b in range(n):
            if distance[a][b] == sys.maxsize and distance[b][a] == sys.maxsize:
                can = False
                break
        if not can:
            answer -= 1
    
    return answer