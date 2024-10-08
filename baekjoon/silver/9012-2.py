import sys

n = int(sys.stdin.readline())

for _ in range(n):
    ps = sys.stdin.readline().rstrip()
    stack = []
    isValid = True
    for p in ps:
        if p == '(':
            stack.append(p)
        else:
            if not stack:
                isValid = False
                break
            stack.pop()
    
    print('YES' if isValid and not stack else 'NO')