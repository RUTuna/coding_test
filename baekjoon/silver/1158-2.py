import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
queue = deque([i for i in range(1,n+1)])
answer = []
count = 1

while queue:
    now = queue.popleft()
    if count % k:
        queue.append(now)
    else:
        answer.append(str(now))
    count += 1
        
print('<',', '.join(answer),'>', sep='')