import sys
from collections import deque

s = int(sys.stdin.readline())
# visited[i][j]: 화면에 i개, 클립보드에 j개일 때 걸리는 최소 시간
visited = [[-1] * (s + 1) for _ in range(s + 1)]

queue = deque([(1, 0)])
visited[1][0] = 0

while queue:
    now, clipboard = queue.popleft()
    
    if now == s:
        print(visited[now][clipboard])
        break
    
    # copy
    if visited[now][now] == -1:
        visited[now][now] = visited[now][clipboard] + 1
        queue.append((now,now))
        
    # paste
    if 0 <= now+clipboard <= s and visited[now+clipboard][clipboard] == -1:
        visited[now+clipboard][clipboard] = visited[now][clipboard] + 1
        queue.append((now+clipboard,clipboard))
    
    # delete
    if 0 <= now-1 <= s and visited[now-1][clipboard] == -1:
        visited[now-1][clipboard] = visited[now][clipboard] + 1
        queue.append((now-1, clipboard))
        