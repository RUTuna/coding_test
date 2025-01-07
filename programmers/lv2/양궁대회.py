from collections import deque

def solution(n, info):
    arrow = deque([(0, n, [])]) # index, scoreL, scoreA, remain, ans
    max_score = 0
    answer = []
    
    def calculate(score):
        scoreL, scoreA = 0,0
        for i in range(11):
            if info[i] < score[i]:
                scoreL += (10-i)
            elif info[i] > 0:
                scoreA += (10-i)
        return (scoreL, scoreA)
    
    while arrow:
        i, remain, result = arrow.popleft()
        
        if i == 10 or remain == 0:
            result += [0]*(10-i+1)
            result[-1] = remain
            scoreL, scoreA = calculate(result)
            if scoreL > scoreA and max_score <= scoreL-scoreA:
                max_score = scoreL-scoreA
                answer = result
            continue
        
        if remain > info[i]:
            shot = info[i]+1
            arrow.append((i+1, remain-shot, result+[shot]))
        arrow.append((i+1, remain, result+[0]))
    
    return answer if len(answer) else [-1]