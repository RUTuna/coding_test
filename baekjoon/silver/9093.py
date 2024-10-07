import sys

n = int(sys.stdin.readline())

for _ in range(n):
    print(' '.join(list(map(lambda s: ''.join(list(reversed(list(s)))), sys.stdin.readline().strip().split(' ')))))