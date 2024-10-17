function solution(n, computers) {
  let answer = 0;
  const visited = Array(n).fill(false);

  function DFS(now) {
    visited[now] = true;
    computers[now].forEach((element, index) => {
      if (element && !visited[index]) DFS(index);
    });
  }

  for (let i = 0; i < n; i++)
    if (!visited[i]) {
      DFS(i);
      answer++;
    }
  return answer;
}
