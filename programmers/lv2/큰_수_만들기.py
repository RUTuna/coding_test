from collections import deque

def solution(number, k):
    n = len(number)
    number = deque(number)
    answer = []
    
    while number:
        front = number.popleft()
        while answer and k > 0 and int(answer[-1]) < int(front):
            k -= 1
            answer.pop()
        answer.append(front)
    
    if k > 0 :
        answer = answer[:-k]
        
    return ''.join(answer)