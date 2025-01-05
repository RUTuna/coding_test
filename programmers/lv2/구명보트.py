from collections import deque

def solution(people, limit):
    people = deque(sorted(people))
    solo = []
    answer = 0
    
    while people:
        front = people.popleft()
        
        # front 와 함께 구조 하지 못 하는 사람들은 rest 로 이동
        while people and front + people[-1] > limit:
            solo.append(people.pop()) 
        
        # people에 남은 가장 무거운 사람은 front 와 함께 구출 될 수 있으니 구출
        if people:
            people.pop()
        
        answer += 1
    answer += len(solo) # 혼자 구해져야 하는 사람들
    
    return answer