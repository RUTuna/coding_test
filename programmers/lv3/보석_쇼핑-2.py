def solution(gems):
    kinds = set(gems)
    counter = {}
    answer = []
    min_size = len(gems)+1
    left, right = 0,0
    done = False
    
    while right < len(gems):
        if gems[right] in counter:
            counter[gems[right]] += 1
        else:
            counter[gems[right]] = 1
        right += 1
        
        while len(counter.keys()) == len(kinds):
            if counter[gems[left]] == 1:
                del counter[gems[left]]
            else:   
                counter[gems[left]] -= 1
            
            left += 1
            if min_size > right-left:
                min_size = right-left
                answer = [left, right]

    
    return answer