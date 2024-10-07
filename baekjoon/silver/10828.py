import sys
n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    operator = sys.stdin.readline().split()
    
    if operator[0] == 'push':
        stack.append(int(operator[1]))
    elif operator[0] == 'pop':
        print(-1 if len(stack) == 0 else stack.pop())
    elif operator[0] == 'size':
        print(len(stack))
    elif operator[0] == 'empty':
        print( 1 if len(stack) == 0 else 0 )
    elif operator[0] == 'top':
        print(-1 if len(stack) == 0 else stack[-1])