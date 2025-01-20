import math
from collections import defaultdict

def solution(enroll, referral, seller, amount):
    n = len(enroll)
    graph = defaultdict(str)
    cost = defaultdict(int)
    
    for i in range(n):
        parent = referral[i]
        child = enroll[i]
        graph[child] = parent

    def DFS(now, nowCost):
        if now == '-' or nowCost <= 0:
            return
        
        parentCost = math.floor(nowCost*0.1)
        cost[now] += nowCost - parentCost
        DFS(graph[now], parentCost)
        
    for i in range(len(seller)):
        now = seller[i]
        nowCost = amount[i]*100
        DFS(now, nowCost)
        
    return [cost[name] for name in enroll]