def solution(prices):
    length = len(prices)
    stack = []
    answer = [0] * length
    
    for index, item in enumerate(prices):
        while stack:
            top_index, top_item = stack.pop()
            if top_item > item:
                answer[top_index] = index-top_index
            else:
                stack.append((top_index,top_item))
                break
        
        stack.append((index,item))
    
    for index, item in enumerate(answer):
        if item == 0:
            answer[index] = length - index - 1
    
    return answer