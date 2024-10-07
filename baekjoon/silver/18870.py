import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
sorted_nums = sorted(set(nums))
priority = {}

for index, num in enumerate(sorted_nums):
    if not num in priority:
        priority[num] = index

for num in nums:
    print(priority[num], end=' ')
