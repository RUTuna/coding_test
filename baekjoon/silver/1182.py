import sys

n, s = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
answer = 0

def DFS(index, sum_val):
    global answer
    
    if index == n:
        if sum_val == s:
            answer+=1
        return
    
    DFS(index+1, sum_val + numbers[index])
    DFS(index+1, sum_val)
        
DFS(0,0)

if s == 0:
    answer -= 1
    
print(answer)