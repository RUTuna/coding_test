import sys
from collections import Counter

n, m = map(int, sys.stdin.readline().split())
woods = Counter(map(int, sys.stdin.readline().split()))

left = 0
right = max(woods)

while left <= right:
    mid = (left + right) // 2
    stick = sum((h - mid) * i for h, i in woods.items() if h > mid)
    
    if stick >= m:
        left = mid + 1
    else:
        right = mid - 1
        
print(right)