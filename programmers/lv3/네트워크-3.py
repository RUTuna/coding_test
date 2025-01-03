def solution(n, computers):
    answer = 0
    check = [False] * n
    
    def DFS(now):
        check[now] = True
        
        for i in range(n):
            if not check[i] and computers[now][i]:
                DFS(i)
    
    for i in range(n):
        if not check[i]:
            answer += 1
            DFS(i)
            
    return answer