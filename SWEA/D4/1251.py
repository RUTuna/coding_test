import sys
sys.stdin = open('1251_input.txt','r')

import heapq


def solve(n, xPoints, yPoints, e):
    privarity_queue = []
    contains = [False for _ in range(n)]
    
    for i in range(n):
        contains[i] = True
        

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    xPoints = list(map(int, input().split()))
    yPoints = list(map(int, input().split()))
    e = float(input())
    
    solve(n, xPoints, yPoints, e)
    
