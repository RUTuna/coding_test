import sys

def solution(a):
    n = len(a)
    if n == 1:
        return 1
    
    left_min = [sys.maxsize] * n
    right_min = [sys.maxsize] * n
    left_min[0] = a[0]
    right_min[n-1] = a[n-1]
    
    for i in range(1, n):
        left_min[i] = min(left_min[i-1], a[i])
        right_min[n-i-1] = min(right_min[n-i], a[n-i-1])
    
    answer = 0
    for i in range(1, n-1):
        if a[i] > left_min[i-1] and a[i] > right_min[i+1]:
            continue
        answer += 1

    return answer+2 ## 양 끝 값은 항상 가능