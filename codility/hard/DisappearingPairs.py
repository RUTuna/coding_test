def solution(S):
    result = []

    for c in S:
        if result and result[-1]==c:
            result.pop()
        else:
            result.append(c)

    return ''.join(result)