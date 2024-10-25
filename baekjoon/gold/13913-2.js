let fs = require("fs");
let input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split(" ")
  .map(Number);

function solution(n, k) {
  let queue = [[n, [n]]];
  let visited = Array(100001).fill(false);

  if (n > k) {
    console.log(n - k);
    console.log(...Array.from({ length: n - k + 1 }, (_, i) => n - i));
    return;
  }

  while (queue.length) {
    let [cur, path] = queue.shift();
    if (cur === k) {
      console.log(path.length - 1);
      console.log(...path);
      return;
    }
    if (visited[cur]) continue;
    visited[cur] = true;

    for (let nxt of [cur - 1, cur + 1, cur * 2]) {
      if (0 <= nxt && nxt < 100001 && !visited[nxt]) queue.push([nxt, [...path, nxt]]);
    }
  }
}

solution(...input);
