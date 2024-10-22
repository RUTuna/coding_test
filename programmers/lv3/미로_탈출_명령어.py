def solution(n, m, x, y, r, c, k):
    # 사전 준비: 인덱스 보정
    x, y, r, c = x-1, y-1, r-1, c-1
    
    # 필요한 최소 이동 횟수
    min_dist = abs(x - r) + abs(y - c)
    
    # 거리 차이와 k의 관계에 따른 불가능한 경우 미리 반환
    if min_dist > k or (k - min_dist) % 2 != 0:
        return "impossible"
    
    # 사전순 탐색을 위한 이동 우선순위
    move = [('d', 1, 0), ('l', 0, -1), ('r', 0, 1), ('u', -1, 0)]
    
    # 경로 문자열 구성
    answer = ""
    remaining_steps = k
    
    # 현재 위치
    cur_x, cur_y = x, y
    
    while remaining_steps > 0:
        for direction, dx, dy in move:
            nxt_x, nxt_y = cur_x + dx, cur_y + dy
            # 경계 확인
            if 0 <= nxt_x < n and 0 <= nxt_y < m:
                # 목표 지점까지의 남은 거리
                next_dist = abs(nxt_x - r) + abs(nxt_y - c)
                
                # 남은 거리와 남은 스텝으로 이동이 가능하다면 이동
                if next_dist <= remaining_steps - 1:
                    answer += direction
                    cur_x, cur_y = nxt_x, nxt_y
                    remaining_steps -= 1
                    break

    return answer