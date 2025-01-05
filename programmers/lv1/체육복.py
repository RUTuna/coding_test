def solution(n, lost, reserve):
    reserveSet = set(reserve) - set(lost)
    lostSet = set(lost) - set(reserve)
    
    for r in sorted(reserveSet):
        if r-1 in lostSet:
            lostSet.remove(r-1)
        elif r+1 in lostSet:
            lostSet.remove(r+1)

    return n - len(lostSet)