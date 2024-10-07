import sys

n = int(sys.stdin.readline())
path = sys.stdin.readline().rstrip()

cost = [-1] * len(path)
cost[0] = 0

able = {'B': 'J', 'O':'B', 'J': 'O'}

for now in range(1, n):
    mincost = sys.maxsize
    
    for prev in range(now):
        if able[path[now]] == path[prev] and cost[prev] != -1:
            mincost = min(mincost, cost[prev]+(now-prev)**2)
    
    cost[now] = -1 if mincost == sys.maxsize else mincost
    
print(cost[n-1])