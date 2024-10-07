import sys

n, m = map(int, sys.stdin.readline().split())
graph = { i:[] for i in range(1, n+1)}
visited = [False for _ in range(n+1)]

for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

def DFS(start):
    stack = [start]
    
    while stack:
        now = stack.pop()
        if visited[now]:
            continue
        
        visited[now] = True
        for next in graph[now]:
            if not visited[next]:
                stack.append(next)
    
answer = 0
for i in range(1, n+1):
    if not visited[i]:
        answer += 1
        DFS(i)
        
print(answer)