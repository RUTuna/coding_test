import sys
from collections import deque
from itertools import permutations

n = int(input())
hp = list(map(int, input().split()))
visited = [[[0]*61 for _ in range(61)] for _ in range(61) ]
start = [ hp[i] if i<len(hp) else 0 for i in range(3)]
queue = deque([[start, 0]])
answer = 0

choice = list(permutations([9,3,1], 3))

while queue:
    [f, s, t], depth = queue.popleft()
    if visited[f][s][t]:
        continue
    
    visited[f][s][t] = depth
    if f==s==t==0:
        break
    
    for fh, sh, th in choice:
        queue.append([[max(0,f-fh), max(0,s-sh), max(0,t-th)], depth+1])

print(visited[0][0][0])
    