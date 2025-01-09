import sys

n = int(sys.stdin.readline())
goodNumber = []

def DFS(i):
    for j in range(1, i//2+1):
        if goodNumber[-j:] == goodNumber[-2*j:-j]:
            return False
    
    if i >= n-1:
        return ''.join(goodNumber)
    
    for num in (1,2,3):
        goodNumber.append(str(num))
        res = DFS(i+1)
        if res:
            return res
        goodNumber.pop()
        

print(DFS(-1))