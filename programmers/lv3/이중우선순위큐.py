from collections import deque

def solution(operations):
    heap = deque([])
    for operation in operations:
        op, num = operation.split(' ')
        
        if op == 'I':
            left, right = 0, len(heap)-1
            index = 0
            num = int(num)
            
            while heap and left <= right:
                mid = (left+right) // 2
                
                if heap[mid] <= num:
                    index = mid+1
                    left = mid+1
                else:
                    right = mid-1
    
            heap.insert(index, num)
            
        elif heap and op == 'D':
            if num == '1':
                heap.pop()
            elif num == '-1':
                heap.popleft()
        
    return [heap[-1], heap[0]] if heap else [0,0]