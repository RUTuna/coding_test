import sys
from collections import deque

def DFS(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        
        if node not in visited:
            visited.add(node)
            print(node, end=' ')
            
            for nxt in graph[node][::-1]:
                stack.append(nxt)
    print('')       

def BFS(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        
        if node not in visited:
            visited.add(node)
            print(node, end=' ')
            
            for nxt in graph[node]:
                queue.append(nxt)
    print('') 

n, m, v = map(int, sys.stdin.readline().split())
graph = { i: set() for i in range(1,n+1)}
for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].add(end)
        
    graph[end].add(start)

for key, value in graph.items():
    graph[key] = sorted(value)

DFS(graph, v)
BFS(graph, v)