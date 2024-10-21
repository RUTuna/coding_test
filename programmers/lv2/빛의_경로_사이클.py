def solution(grid):
    answer = []
    length_i = len(grid)
    length_j = len(grid[0])
    direction = [(-1,0), (0, -1), (1,0), (0,1)]
    visited = [[[False] * 4 for _ in range(length_j)] for _ in range(length_i)]
    
    for i in range(length_i):
        for j in range(length_j):
            for direct_index in range(4):
                # 가봤던 경로라면 continue
                if visited[i][j][direct_index]:
                    continue
                
                now_i, now_j, now_direct = i, j, direct_index
                size = 0
                while not visited[now_i][now_j][now_direct]:
                    visited[now_i][now_j][now_direct] = True
                    if grid[now_i][now_j] == 'L':
                        now_direct = (now_direct + 1) % 4
                    elif grid[now_i][now_j] == 'R':
                        now_direct = (now_direct - 1) % 4
                    
                    size += 1
                    now_i = (now_i + direction[now_direct][0]) % length_i
                    now_j = (now_j + direction[now_direct][1]) % length_j
                
                answer.append(size)
    
    return sorted(answer)