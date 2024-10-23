let fs = require("fs");
let input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

function solution(volumns, n, s, m) {
  let dp = Array.from({ length: n + 1 }, () => new Set());
  dp[0].add(s);

  for (let i = 1; i <= n; i++) {
    for (let prev of dp[i - 1]) {
      if (0 <= prev - volumns[i - 1]) dp[i].add(prev - volumns[i - 1]);
      if (prev + volumns[i - 1] <= m) dp[i].add(prev + volumns[i - 1]);
    }
  }

  return dp[n].size ? Math.max(...dp[n]) : -1;
}

console.log(solution(input[1].length === 1 ? [Number(input[1])] : input[1].split(" ").map(Number), ...input[0].split(" ").map(Number)));
