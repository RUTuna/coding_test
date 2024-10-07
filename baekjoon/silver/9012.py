import sys

n = int(sys.stdin.readline())

def check(string):
    stack = []
    for char in string:
        if char == '(':
            stack.append(char)
        
        else:
            if not stack:
                return 'NO'
            stack.pop()

    return 'NO' if stack else 'YES'

for _ in range(n):
    print(check(sys.stdin.readline().strip()))