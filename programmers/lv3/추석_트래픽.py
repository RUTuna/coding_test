from collections import deque

def transform(time):
    time = time.split(':')
    time = time[:2] + time[2].split('.')
    result = 0
    for i, v in enumerate([60, 60, 1000, 1]):
        result = (result+int(time[i]))*v
        
    return result

def solution(lines):
    logs = deque([log.split()[1:] for log in lines])
    maxValue = 0
    while logs:
        now, _ = logs.popleft()
        now = transform(now)
        count = 1
        
        for nxt, nxt_T in logs:
            nxt = transform(nxt)
            if nxt > now + 4000:
                break
                
            nxt_T = float(nxt_T.split('s')[0])*1000
            if now+1000 > nxt - nxt_T + 1:
                count += 1
        
        maxValue = max(maxValue, count)
    
    return maxValue