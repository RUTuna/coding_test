import sys
from collections import deque

testcase = int(sys.stdin.readline())

for _ in range(testcase):
    n, m = map(int, sys.stdin.readline().split(' '))
    priority = deque(list(map(int, sys.stdin.readline().split(' '))))
    result = 0
    
    while priority:
        front = priority.popleft()
        if not priority or front >= max(priority):
            result += 1
            if m == 0:
                print(result)
                break
            
        else:
            priority.append(front)
        
        m = (m-1 + len(priority)) % len(priority)
    