def solution(N, number):
    if N == number:
        return 1
    dp = [set([int(str(N)*i)]) for i in range(1,9)]
    
    for count in range(1,8):
        for i in range(count):
            for op1 in dp[i]:
                for op2 in dp[count-i-1]:
                    dp[count].add(op1+op2)
                    dp[count].add(op1-op2)
                    dp[count].add(op1*op2)
                    if op2 != 0:
                        dp[count].add(op1//op2)
        if number in dp[count]:
            return count+1
        
    return -1