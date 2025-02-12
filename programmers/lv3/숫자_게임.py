def solution(A, B):
    A.sort()
    B.sort(reverse = True)
    answer = 0
    
    for aTeam in A:
        while B and B[-1] <= aTeam:
            B.pop()
        if B:
            B.pop()
            answer += 1
        else:
            break
            
    return answer