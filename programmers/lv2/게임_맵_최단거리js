function solution(maps) {
    let n = maps.length, m = maps[0].length
    const visited = Array.from({length:n}, ()=>Array(m).fill(false))
    const direct = [[0,1],[1,0],[0,-1],[-1,0]] 
    
    const queue = [[0,0,1]]
    
    while(queue.length>0){
        let [r,c,depth] = queue.shift()
        if(visited[r][c]) continue
        
        if(r===n-1 && c===m-1) return depth
        
        visited[r][c] = true
        for(let [dr, dc] of direct){
            let nr = dr+r, nc = dc+c
            if(0<=nr && nr<n && 0<=nc && nc<m && maps[nr][nc] && !visited[nr][nc] ) {
                queue.push([nr,nc,depth+1])
            }
        } 
    }
    
    return -1;
}