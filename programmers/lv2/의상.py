def solution(clothes):
    closet = {}
    for name, types in clothes:
        if types in closet:
            closet[types] += 1
        else:
            closet[types] = 2 # 입지 않는 경우 고려
            
    answer = 1
    for val in closet.values():
        answer *= val
        
    return answer-1 # 아무것도 안 입는 경우는 없으니