let fs = require("fs");
let input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

function solution(n, m, v, edges) {
  const maps = Array.from({ length: n + 1 }, () => Array(n + 1).fill(0));

  for (let i = 0; i < m; i++) {
    const [v, w] = edges[i];
    maps[v][w] = 1;
    maps[w][v] = 1;
  }
}
