from collections import deque

n, k = map(int, input().split())

max_limit = 100001
visited = [0] * max_limit
ways = [0] * max_limit

queue = deque([n])
visited[n] = 1  # 시작 위치를 방문으로 체크
ways[n] = 1  # 시작 위치에서 갈 수 있는 방법은 1가지

while queue:
    now = queue.popleft()
    
    for nxt in [now - 1, now + 1, 2 * now]:
        if 0 <= nxt < max_limit:
            if not visited[nxt]:  # 처음 방문
                visited[nxt] = visited[now] + 1
                ways[nxt] = ways[now]
                queue.append(nxt)
            elif visited[nxt] == visited[now] + 1:  # 최단 시간으로 도달
                ways[nxt] += ways[now]

print(visited[k] - 1, ways[k], sep='\n')