import sys
sys.stdin = open("2806_input.txt", "r")

T = int(input())

def ret(point, n):
    ans = 0
    if len(point) == n:
        return 1
    r = 0 if len(point)==0 else point[-1][0] + 1
    c = 0 
    
    while r < n:
        while c < n:
            # print(point, r,c)
            isPossible = True
            for pR,pC in point:
                if r == pR or c == pC or r-c == pR-pC or r+c == pR+pC:
                    isPossible = False
                    break
            if isPossible:
                ans += ret(point + [(r,c)], n)
            c += 1
        
        c = 0
        r += 1
                
    return ans
    

for test_case in range(1, T + 1):
    n = int(input())
    point = []

    ans = ret(point, n)
    
    
    print('#'+str(test_case), ans)
