import sys

n, k = map(int, sys.stdin.readline().split(' '))
arr = [ i for i in range(1,n+1) ]
result = []
count = 0

while arr:
    count = (count + k-1)% len(arr)
    result.append(arr.pop(count))
    
sys.stdout.write('<' + ', '.join(map(str, result)) + '>\n')