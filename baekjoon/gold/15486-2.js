let fs = require("fs");
let input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

function solution(n, task) {
  let dp = Array(n + 50).fill(0);

  task.forEach(([t, p], i) => {
    dp[i] = Math.max(i > 0 ? dp[i - 1] : 0, dp[i]);
    dp[i + t] = Math.max(dp[i + t], dp[i] + p);
  });

  return Math.max(dp[n - 1], dp[n]);
}

console.log(
  solution(
    Number(input[0]),
    input.splice(1).map((e) => e.split(" ").map(Number))
  )
);
