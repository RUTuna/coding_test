import sys

k, n = map(int, sys.stdin.readline().split())
lines = []

for _ in range(k):
    lines.append(int(sys.stdin.readline()))
    
left = 1
right = max(lines)

while left <= right:
    mid = (left + right) // 2
    
    count = 0
    
    for line in lines:
        count += line // mid
        if count >= n:
            break
        
    if count >= n:
        left = mid + 1
    else:
        right = mid - 1

print(right)