def solution(arrows):
    visitedNodes = set([(0,0)])
    visitedEdges = set()
    x, y = 0,0
    rooms = 0
    direct = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
    
    for arrow in arrows:
        for _ in range(2):
            nx, ny = x+direct[arrow][0], y+direct[arrow][1]
            if (nx, ny) in visitedNodes and not (x,y,nx,ny) in visitedEdges and not (nx,ny,x,y) in visitedEdges:
                rooms += 1
            else:
                visitedNodes.add((nx,ny))
            
            visitedEdges.add((nx,ny,x,y))
            visitedEdges.add((x,y,nx,ny))
            x, y = nx, ny
            
    return rooms