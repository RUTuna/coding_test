import sys
from collections import Counter

n = int(sys.stdin.readline())
cards = Counter(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
finds = list(map(int, sys.stdin.readline().split()))

for f in finds:
    if f in cards:
        print(cards[f], end=' ')
    else:
        print (0, end=' ')