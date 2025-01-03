def solution(arr):
    arr = ''.join(arr).split('-')
    arr = [list(map(int, x.split('+'))) for x in arr]
    tail_min, tail_max = 0,0
    
    while len(arr)>1:
        sub = arr.pop()
        total = sum(sub)
        sub_min = min(-total+tail_min, -total-tail_max)
        sub_max = max(total-2*sub[0]+tail_max, -total-tail_min)
        
        tail_min = sub_min
        tail_max = sub_max
        
    return sum(arr[0])+tail_max