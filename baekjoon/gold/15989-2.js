let fs = require("fs");
let input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n")
  .map(Number);

function solution(ns) {
  let maxNum = Math.max(...ns);
  let dp = Array(maxNum + 1).fill(1);

  for (let d of [2, 3]) {
    for (let i = d; i < maxNum + 1; i++) {
      dp[i] += dp[i - d];
    }
  }

  for (let n of ns) {
    console.log(dp[n]);
  }
}

solution(input.slice(1));
