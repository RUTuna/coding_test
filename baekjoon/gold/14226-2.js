let fs = require("fs");
let input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim();

function solution(s) {
  let queue = [[1, 0, 0]]; // 현재 개수, 클립 보드, 시간
  let visited = Array.from({ length: s * 2 }, () => Array(s * 2).fill(false));

  while (queue.length) {
    let [len, clip, time] = queue.shift();
    if (visited[len][clip]) continue;
    visited[len][clip] = true;
    if (len === s) return time;

    if (len > 0) {
      queue.push([len - 1, clip, time + 1]);
      queue.push([len, len, time + 1]);
    }
    if (clip > 0 && len + clip < s * 2) queue.push([len + clip, clip, time + 1]);
  }
}

console.log(solution(Number(input)));
