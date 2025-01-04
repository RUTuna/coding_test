def solution(participant, completion):
    runner = {}
    for c in completion:
        if c in runner:
            runner[c] += 1
        else:
            runner[c] = 1
    
    for p in participant:
        if (not p in runner) or runner[p] == 0:
            return p
        else:
            runner[p] -= 1
    return ''