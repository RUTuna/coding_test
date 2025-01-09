def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []
    
    for i, price in enumerate(prices):
        while stack and stack[-1][1] > price:
            prev_i, _ = stack.pop()
            answer[prev_i] = i-prev_i
            
        stack.append((i,price))
    
    while stack:
        prev_i, _ = stack.pop()
        answer[prev_i] = n-prev_i-1
        
    return answer