def solution(S):
    n = len(S)
    
    for i in range(n//2):
        if S[i] != S[n-i-1]:
            return -1
            
    return n//2 if n%2 else -1