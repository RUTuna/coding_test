def solution(routes):
    routes.sort(key=lambda x: x[1])
    last_pos = -30001 
    camera = 0
    
    for [start, end] in routes:
        if last_pos < start: # 마지막에 설치된 카메라로 커버 불가능
            camera += 1
            last_pos = end

    return camera