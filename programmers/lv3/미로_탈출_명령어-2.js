function solution(n, m, x, y, r, c, k) {
  let isDone = false;
  let answer = "impossible";
  let direction = [
    [1, 0, "d"],
    [0, -1, "l"],
    [0, 1, "r"],
    [-1, 0, "u"],
  ]; // d l r u 순서

  let minDist = Math.abs(x - r) + Math.abs(y - c);
  if (minDist > k || (k - minDist) % 2) return answer;

  function DFS(nowR, nowC, path) {
    if (path.length === k) {
      if (nowR === r - 1 && nowC === c - 1) {
        answer = path.join("");
        isDone = true;
      }
      return;
    }

    let minDist = Math.abs(nowR - r + 1) + Math.abs(nowC - c + 1);
    if (minDist > k - path.length) return;

    for (let [dr, dc, d] of direction) {
      let nxtR = nowR + dr,
        nxtC = nowC + dc;
      if (0 <= nxtR && nxtR < n && 0 <= nxtC && nxtC < m && !isDone) DFS(nxtR, nxtC, [...path, d]);
    }
  }

  DFS(x - 1, y - 1, []);

  return answer;
}
