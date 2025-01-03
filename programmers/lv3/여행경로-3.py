def solution(tickets):
    airport = set()
    
    for start, end in tickets: # O(n)
        airport.add(start)
        airport.add(end)
    
    airport = sorted(list(airport))
    airport_num = {}
    
    for index, port in enumerate(airport): # O(m)
        airport_num[port] = index
    
    tickets_matrix = [[0]*len(airport) for _ in airport]
    
    for start, end in tickets: # O(n)
        tickets_matrix[airport_num[start]][airport_num[end]] += 1
        
    answer = ['ICN']
    done = False
    
    def DFS(now):
        nonlocal done 
        
        if len(answer) == len(tickets)+1:
            done = True
            return
        
        for nxt, isAble in enumerate(tickets_matrix[now]):
            if isAble and not done:
                tickets_matrix[now][nxt] -= 1
                answer.append(airport[nxt])
                DFS(nxt)
                if done:
                    return
                tickets_matrix[now][nxt] += 1
                answer.pop()
                
    DFS(airport_num['ICN'])
    return answer