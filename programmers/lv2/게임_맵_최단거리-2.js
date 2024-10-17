function solution(maps) {
  let direction = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
  ];
  let n = maps.length,
    m = maps[0].length;
  let queue = [[0, 0, 1]];
  let visited = Array.from({ length: n }, () => Array(m).fill(0));

  while (queue.length > 0) {
    let [r, c, d] = queue.shift();

    if (r === n - 1 && c === m - 1) return d;
    if (visited[r][c]) continue;

    visited[r][c] = d;

    for (let [dr, dc] of direction) {
      let nr = r + dr,
        nc = c + dc;
      if (0 <= nr && nr < n && 0 <= nc && nc < m && maps[nr][nc] && visited[nr][nc] === 0) {
        queue.push([nr, nc, d + 1]);
      }
    }
  }

  return -1;
}
