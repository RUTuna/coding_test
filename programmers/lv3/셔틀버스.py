def transform(time, d):
    hour = time//100
    minutes = time%100 + d
    
    if minutes >= 60:
        hour += minutes//60
        minutes %= 60
    elif minutes < 0:
        hour -= (-minutes)//60 + 1
        minutes = 60 - (-minutes)%60
        
    return hour*100 + minutes

def solution(n, t, m, timetable):
    timetable = sorted([int(time.replace(':','')) for time in timetable], reverse=True)
    
    last = []
    for i in range(n):
        last = []
        start = transform(900, i*t)
        count = 0
        while timetable and count < m:
            now = timetable.pop()
            if now > start:
                timetable.append(now)
                break
            last.append(now)
            count += 1
    
    answer = 0
    if len(last) < m:
        answer = transform(900, (n-1)*t)
    else:
        i = len(last)-1
        while i>0:
            if last[i] != last[i-1]:
                break
            i-=1
        answer = transform(last[i], -1) 
        
    hour = str(answer//100)
    hour = '0'*(2-len(hour)) + hour
    minutes = str(answer%100)
    minutes = '0'*(2-len(minutes)) + minutes
    
    return hour+":"+minutes