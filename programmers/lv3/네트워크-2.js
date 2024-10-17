function solution(n, computers) {
  let answer = 0;
  let visited = Array(n).fill(false);

  function BFS(start) {
    let queue = [start];

    while (queue.length > 0) {
      let top = queue.shift();
      if (visited[top]) continue;

      visited[top] = true;
      computers[top].forEach((v, i) => {
        if (v && !visited[i]) queue.push(i);
      });
    }
  }

  for (let i in visited) {
    if (!visited[i]) {
      answer++;
      BFS(i);
    }
  }

  return answer;
}
