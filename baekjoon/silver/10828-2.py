import sys

n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    op = sys.stdin.readline().split()
    if op[0] == 'push':
        stack.append(int(op[1]))
    elif op[0] == 'pop':
        print(stack.pop() if stack else -1)
    elif op[0] == 'size':
        print(len(stack))
    elif op[0] == 'empty':
        print(0 if stack else 1)
    elif op[0] == 'top':
        print(stack[-1] if stack else -1)