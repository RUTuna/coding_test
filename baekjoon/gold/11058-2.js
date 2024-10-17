let fs = require("fs");
let n = Number(
  fs
    .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
    .toString()
    .trim()
);

function solution(n) {
  let dp = Array.from({ length: n + 1 }, (_, i) => i);

  for (let i = 3; i <= n; i++) {
    dp[i] = dp[i - 1] + 1;

    for (let j = i - 2; j > 0; j--) {
      dp[i] = Math.max(dp[i], dp[j] * (i - j - 1));
    }
  }

  return dp[n];
}

console.log(solution(n));
