let fs = require("fs");
let input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split(" ")
  .map(Number);

function solution(n, k) {
  let queue = [n];
  let visited = Array(100001).fill(Number.MAX_SAFE_INTEGER);
  let way = Array(100001).fill(0);
  visited[n] = 0;
  way[n] = 1;

  while (queue.length) {
    let cur = queue.shift();

    for (let nxt of [cur - 1, cur + 1, cur * 2]) {
      if (0 <= nxt && nxt < 100001) {
        if (visited[nxt] === Number.MAX_SAFE_INTEGER) {
          visited[nxt] = visited[cur] + 1;
          queue.push(nxt);
        }
        if (visited[nxt] === visited[cur] + 1) way[nxt] += way[cur];
      }
    }
  }

  return `${visited[k]}\n${way[k]}`;
}

console.log(solution(...input));
