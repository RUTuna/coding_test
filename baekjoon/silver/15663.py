import sys

n, m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()
visited = [False] * n
path = []

def DFS(depth):
    if depth == m:
        print(*path)
        return
    
    repeat = 0
    for index, num in enumerate(numbers):
        if not visited[index] and num != repeat:
            visited[index] = True
            path.append(num)
            repeat = num
            DFS(depth+1)
            visited[index] = False
            path.pop()

DFS(0)