def solution(board, skill):
    n = len(board)
    m = len(board[0])
    prefixSum = [[0]*(m+1) for _ in range(n+1)]
    
    # 누적합을 위한 배열
    for t, r1, c1, r2, c2, d in skill:
        prefixSum[r1][c1] += d if t==2 else -d
        prefixSum[r1][c2+1] += -d if t==2 else d
        prefixSum[r2+1][c1] += -d if t==2 else d
        prefixSum[r2+1][c2+1] += d if t==2 else -d
    
    # 누적합 계산
    for r in range(n+1):
        for c in range(m+1):
            if c>0:
                prefixSum[r][c] += prefixSum[r][c-1]
            if r>0:
                prefixSum[r][c] +=prefixSum[r-1][c]
            if c>0 and r>0:
                prefixSum[r][c] -= prefixSum[r-1][c-1]
    
    answer = 0
    # 파괴된 건물 세기
    for r in range(n):
        for c in range(m):
            if board[r][c] + prefixSum[r][c] > 0:
                answer += 1
    
    return answer