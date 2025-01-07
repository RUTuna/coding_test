import sys

L, C = map(int, sys.stdin.readline().split())
candidate = sorted(sys.stdin.readline().split())
vowel = set(['a','e','i','o','u'])
code = []

def DFS(index, numV):
    if len(code) == L and numV and L-numV > 1:
        print(''.join(code))
        return
    
    if index >= C:
        return
    
    code.append(candidate[index])
    DFS(index+1, numV+1 if candidate[index] in vowel else numV)
    code.pop()
    DFS(index+1, numV)
    
DFS(0,0)