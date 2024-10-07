import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

max_limit = 100001

def BFS(start):
    visited = [0] * max_limit
    queue = deque([(start, [start])])
    while queue:
        now, path = queue.popleft()
        
        if n > k:
            return (n-k, [ i for i in range(n, k-1, -1)])
        
        if now == k:
            return (visited[now], path)
        
        for nxt in [now-1, now+1, 2*now]:
            if 0<= nxt < max_limit and not visited[nxt]:
                visited[nxt] = visited[now] + 1
                queue.append((nxt, path + [nxt]))
                
distance, path = BFS(n)
print(distance)
print(*path)