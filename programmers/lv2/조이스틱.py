def solution(name):
    n = len(name)
    spell_move = 0
    cursor_move = n-1
    
    for i, c in enumerate(name):
        spell_move += min(ord(c)-ord('A'), ord('Z')-ord(c)+1)
        
        # i+1 부터 오른쪽으로 연속된 A 찾기
        next_A = i+1
        while next_A < n and name[next_A] == 'A':
            next_A += 1
        
        # 1. 이전 커서 이동 값
        # 2. 연속된 A의 왼쪽 시작
        # 3. 연속된 A의 오른쪽 시작
        cursor_move = min([cursor_move, 2*i + (n-next_A), i + 2*(n-next_A)])
    
    return spell_move + cursor_move