import sys
from collections import Counter

n, m = map(int, sys.stdin.readline().split())
numbers = sorted(list(map(int, sys.stdin.readline().split())))
numbers = Counter(numbers)
path = []

def DFS(depth):
    if depth == m:
        print(*path)
        return
    
    for n in numbers.keys():
        if numbers.get(n) > 0:
            numbers[n] -= 1
            path.append(n)
            DFS(depth+1)
            numbers[n] += 1
            path.pop()

DFS(0)