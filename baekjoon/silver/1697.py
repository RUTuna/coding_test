import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
max_num = 10**5
visited = [0] * (max_num+1)
queue = deque([n])

while queue:
    now = queue.popleft()
        
    if now == k:
        break
    
    for nxt in (now+1, now-1, 2*now):
        if 0 <= nxt <= max_num and not visited[nxt]:
            visited[nxt] = visited[now]+1
            queue.append(nxt)
    
print(visited[k])