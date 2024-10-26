let fs = require("fs");
let input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n")
  .map((r) => r.split(" ").map(Number));

function solution(n, s, numbers) {
  let answer = 0;

  function DFS(cur, sum, path) {
    if (cur === n) {
      if (path.length > 0 && sum === s) answer++;
      return;
    }

    DFS(cur + 1, sum, path);
    DFS(cur + 1, sum + numbers[cur], [...path, numbers[cur]]);
  }

  DFS(0, 0, []);
  return answer;
}

console.log(solution(input[0][0], input[0][1], input[1]));
