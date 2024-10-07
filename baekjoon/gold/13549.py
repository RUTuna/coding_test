from collections import deque

n, k = map(int, input().split())

max_limit = 100001
visited = [0] * max_limit

queue = deque([n])
visited[n] = 1

while queue:
    now = queue.popleft()
    
    for nxt in [now-1, now+1, 2*now]:
        if 0 <= nxt < max_limit:
            nxt_time = visited[now] + (0 if nxt == 2*now else 1)
            if visited[nxt] == 0 or visited[nxt] > nxt_time: # 방문한 적이 없거나, 지금보다 더 오랜시간으로 도달 했을 경우
                visited[nxt] = nxt_time
                queue.append(nxt)

print(visited[k]-1)