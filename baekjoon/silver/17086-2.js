let fs = require("fs");
let input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n")
  .map((e) => e.split(" ").map(Number));

function solution(n, m, maps) {
  let distance = Array.from({ length: n }, () => Array(m).fill(Number.MAX_SAFE_INTEGER));
  let direction = [
    [0, 1],
    [1, 1],
    [1, 0],
    [1, -1],
    [0, -1],
    [-1, -1],
    [-1, 0],
    [-1, 1],
  ];

  for (let r = 0; r < n; r++) {
    for (let c = 0; c < m; c++) {
      if (maps[r][c]) {
        BFS(r, c);
      }
    }
  }

  function BFS(startR, startC) {
    let queue = [[startR, startC, 0]];

    while (queue.length > 0) {
      let [nowR, nowC, depth] = queue.shift();
      if (distance[nowR][nowC] <= depth) continue;

      distance[nowR][nowC] = depth;
      for (let [dr, dc] of direction) {
        let newR = nowR + dr,
          newC = nowC + dc;
        if (0 <= newR && newR < n && 0 <= newC && newC < m && !maps[newR][newC] && distance[newR][newC] > depth + 1) {
          queue.push([newR, newC, depth + 1]);
        }
      }
    }
  }

  let answer = 0;
  for (let rows of distance) {
    answer = Math.max(answer, ...rows);
  }

  return answer;
}

console.log(solution(input[0][0], input[0][1], input.slice(1)));
