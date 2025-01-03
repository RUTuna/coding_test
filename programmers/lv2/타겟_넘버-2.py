def solution(numbers, target):
    total = 0
    answer = 0
    
    def DFS(depth):
        nonlocal total, answer
        
        if depth == len(numbers):
            if total == target:
                answer += 1
            return
        
        for op in [1, -1]:
            total += (numbers[depth]*op)
            DFS(depth+1)
            total -= (numbers[depth]*op)
    DFS(0)
    
    return answer