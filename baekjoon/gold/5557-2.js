let fs = require("fs");
let input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

function solution(n, numbers) {
  let dp = Array.from({ length: n }, () => Array(21).fill(0));
  dp[0][numbers[0]] = 1;

  for (let depth = 1; depth < n - 1; depth++) {
    dp[depth - 1].forEach((v, i) => {
      if (i + numbers[depth] < 21) dp[depth][i + numbers[depth]] += v;
      if (i - numbers[depth] > -1) dp[depth][i - numbers[depth]] += v;
    });
  }

  return dp[n - 2][numbers[n - 1]];
}

console.log(solution(Number(input[0]), input[1].split(" ").map(Number)));
