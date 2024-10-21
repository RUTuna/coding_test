def solution(n, k, cmds):
    linked = { i : [i-1, i+1] for i in range(n)}
    deleted = []
    result = ['O'] * n
    index = k
    
    
    for cmd in cmds:
        cmd = cmd.split()
        
        if cmd[0] == 'U':
            for _ in range(int(cmd[1])):
                index = linked[index][0]
                
        elif cmd[0] == 'D':
            for _ in range(int(cmd[1])):
                index = linked[index][1]
                
        elif cmd[0] == 'C':
            up, down = linked[index]
            result[index] = 'X'
            deleted.append(index)
            
            if down < n:
                index = down
            else:
                index = up
            
            if up > -1:
                linked[up][1] = down
            if down < n:
                linked[down][0] = up
    
        elif cmd[0] == 'Z':
            top = deleted.pop()
            up, down = linked[top]
            result[top] = 'O'
            
            if up > -1:
                linked[up][1] = top
            if down < n:
                linked[down][0] = top
    
    return ''.join(result)