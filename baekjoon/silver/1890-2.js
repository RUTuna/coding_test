let fs = require("fs");
let input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

function solution(n, maps) {
  let direction = [
    [0, 1],
    [1, 0],
  ];
  let dp = Array.from({ length: n }, () => Array(n).fill(BigInt(0)));
  dp[0][0]++;

  for (let r = 0; r < n; r++) {
    for (let c = 0; c < n; c++) {
      for (let [dr, dc] of direction) {
        let newR = r + dr * maps[r][c],
          newC = c + dc * maps[r][c];
        if (0 <= newR && newR < n && 0 <= newC && newC < n) {
          dp[newR][newC] += dp[r][c];
        }
      }
    }
  }

  return (dp[n - 1][n - 1] / BigInt(4)).toString();
}

console.log(
  solution(
    Number(input[0]),
    input.splice(1, Number(input[0]) + 1).map((e) => e.split(" ").map(Number))
  )
);
