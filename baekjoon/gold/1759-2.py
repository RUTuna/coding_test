import sys

l, c = map(int, sys.stdin.readline().split())
chars = sorted(sys.stdin.readline().split())

def checkMo(string):
    count = 0
    mo = set(['a','e','i','o','u'])
    for s in string:
        if s in mo:
            count+=1
    return count

def DFS(depth, path):
    if len(path) == l:
        password = ''.join(path)
        mo = checkMo(password)
        if mo>=1 and l-mo>=2:
            print(password)
            return
            
    if depth == c:
        return
    
    DFS(depth+1, path+[chars[depth]])
    DFS(depth+1, path)

DFS(0,[])