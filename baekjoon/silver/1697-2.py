import sys
from collections import deque

limit = 100001
n, k = map(int, sys.stdin.readline().split())
visited = [False] * limit
queue = deque([(n,0)])

while queue:
    now, step = queue.popleft()
    
    if now == k:
        print(step)
        break
    
    visited[now] = True
    for nxt in [now+1, now-1, now*2]:
        if 0<=nxt<limit and not visited[nxt]:
            visited[nxt] = True
            queue.append((nxt, step+1))