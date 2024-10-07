import sys

n,m = map(int, sys.stdin.readline().split())
nums = [i for i in range(n, 0, -1)]

def BFS():
    stack = [[]]
    
    while stack:
        ans = stack.pop()
        
        if len(ans) == m:
            print(' '.join(ans))
            continue
        
        for nxt in nums:
            stack.append(ans + [str(nxt)])

BFS()