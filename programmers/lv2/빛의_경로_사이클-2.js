function solution(grid) {
  let answer = [];
  let n = grid.length,
    m = grid[0].length;
  let move = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
  ];
  let direct = {
    S: 0,
    L: -1,
    R: 1,
  };
  let visited = Array.from({ length: n }, () => Array.from({ length: m }, () => Array(4).fill(false)));

  function Find(r, c, direction) {
    let [newR, newC, newDirection] = [r, c, direction];
    let depth = 0;

    while (!visited[newR][newC][newDirection]) {
      depth++;
      visited[newR][newC][newDirection] = true;
      newDirection = (newDirection + direct[grid[newR][newC]] + 4) % 4;
      let dr = move[newDirection][0],
        dc = move[newDirection][1];
      newR = (newR + dr + n) % n;
      newC = (newC + dc + m) % m;
    }

    return depth;
  }

  for (let r = 0; r < n; r++) {
    for (let c = 0; c < m; c++) {
      for (let d = 0; d < 4; d++) {
        if (!visited[r][c][d]) answer.push(Find(r, c, d));
      }
    }
  }

  return answer.sort((a, b) => a - b);
}
