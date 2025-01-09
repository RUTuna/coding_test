import sys
import math
from collections import deque

n = int(sys.stdin.readline())
hp = list(map(int, sys.stdin.readline().split()))

def solution(n, hp):
    if n == 1:
        return math.ceil(hp[0]/9)
    
    if n == 2:
        hp.append(0)

    attack = [(9,3,0), (3,9,0)] if n==2 else [(9,3,1), (9,1,3), (3,9,1), (3,1,9), (1,9,3), (1,3,9)]
    queue = deque([(hp, 0)])
    visited = [[[False]*61 for _ in range(61)] for _ in range(61)]
    visited[hp[0]][hp[1]][hp[2]] = True
    
    while queue:
        nowHp, i = queue.popleft()
        if sum(nowHp) == 0:
            return i
        
        for a in attack:
            nxt = [nowHp[i]-a[i] if nowHp[i]-a[i]>0 else 0 for i in range(3)]
            if not visited[nxt[0]][nxt[1]][nxt[2]]:
                visited[nxt[0]][nxt[1]][nxt[2]] = True
                queue.append((nxt, i+1))
    
    return 0

print(solution(n,hp))