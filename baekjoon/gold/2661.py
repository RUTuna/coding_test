n = int(input())

def DFS(path):
    length = len(path)
    
    # 새로 추가된 수에 의해 규칙이 파괴되었는지 확인
    for i in range(1, length//2 + 1):
        if path[-i:] == path[-2*i:-i]:
            return False
    
    if length == n:
        print(*path, sep='')
        return True
    
    for num in (1,2,3):
        res = DFS(path+[num])
        if res:
            return res
    
DFS([])