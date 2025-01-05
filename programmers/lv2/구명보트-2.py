def solution(people, limit):
    answer = 0
    people = sorted(people)
    light, heavy = 0, len(people)-1
    
    while light <= heavy: # light 랑 heavy 랑 같아져도 ans 는 하나만 증가되니 상관 X
        if people[light] + people[heavy] <= limit:
            light += 1
        heavy -= 1
        answer += 1
    
    return answer