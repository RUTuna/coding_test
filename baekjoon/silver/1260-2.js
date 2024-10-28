let fs = require("fs");
let input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n")
  .map((e) => e.split(" ").map(Number));

function solution(n, m, v, edges) {
  const maps = Array.from({ length: n + 1 }, () => Array(n + 1).fill(0));

  for (let i = 0; i < m; i++) {
    const [v, w] = edges[i];
    maps[v][w] = 1;
    maps[w][v] = 1;
  }

  function DFS(start) {
    let stack = [start];
    let visited = Array(n + 1).fill(false);
    let path = [];

    while (stack.length) {
      let top = stack.pop();
      if (visited[top]) continue;
      visited[top] = true;
      path.push(top);

      for (let nxt = n; nxt > 0; nxt--) {
        if (maps[top][nxt] && !visited[nxt]) stack.push(nxt);
      }
    }

    return path;
  }

  function BFS(start) {
    let queue = [start];
    let visited = Array(n + 1).fill(false);
    let path = [];

    while (queue.length) {
      let front = queue.shift();
      if (visited[front]) continue;
      visited[front] = true;
      path.push(front);

      for (let nxt = 1; nxt <= n; nxt++) {
        if (maps[front][nxt] && !visited[nxt]) queue.push(nxt);
      }
    }

    return path;
  }

  console.log(...DFS(v));
  console.log(...BFS(v));
}

solution(input[0][0], input[0][1], input[0][2], input.splice(1));
