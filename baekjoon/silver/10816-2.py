import sys

n = int(sys.stdin.readline())
cards = {}
nums = map(int, sys.stdin.readline().split())
for num in nums:
    if num in cards:
        cards[num] += 1
    else:
        cards[num] = 1

m = int(sys.stdin.readline())
nums = map(int,sys.stdin.readline().split())
for num in nums:
    print(cards[num] if num in cards else 0, end=' ')
