import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
sortednum = sorted(set(nums))

def binary_search_left(n):
    left = 0
    right = len(sortednum)-1
    
    while left<=right:
        mid = (left+right)//2
        
        if sortednum[mid] < n:
            left = mid+1
        else:
            right = mid-1
            
    return right+1

for num in nums:
    print(binary_search_left(num), end=' ')
            