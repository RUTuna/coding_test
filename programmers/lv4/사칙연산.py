def solution(arr):
    l = len(arr)
    dp = [[()] * l for _ in range(l)]
    
    def calculate(start, end):
        if start == end:
            dp[start][end] = (int(arr[start]), int(arr[start]))
            
        elif len(dp[start][end]) == 0:
            ans = set()
            for i in range(start+1, end, 2):
                if arr[i] == '-':
                    ans.add(calculate(start,i-1)[1] - calculate(i+1,end)[0])
                    ans.add(calculate(start,i-1)[0] - calculate(i+1,end)[1])
                else:
                    ans.add(calculate(start,i-1)[1] + calculate(i+1,end)[1])
                    ans.add(calculate(start,i-1)[0] + calculate(i+1,end)[0])
            dp[start][end] = (min(ans), max(ans))
            
        return dp[start][end]
    
    return max(calculate(0,l-1))