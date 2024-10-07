import sys

n = int(sys.stdin.readline())
cards = set(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
finds = list(map(int, sys.stdin.readline().split()))

for f in finds:
    print(1 if f in cards else 0, end=' ')
    