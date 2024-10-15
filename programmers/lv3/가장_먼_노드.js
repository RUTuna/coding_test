function solution(n, edge) {
  const maps = {};

  for (let [v, w] of edge) {
    if (Object.hasOwn(maps, v)) maps[v] = [...maps[v], w];
    else maps[v] = [w];
    if (Object.hasOwn(maps, w)) maps[w] = [...maps[w], v];
    else maps[w] = [v];
  }

  const visited = Array(n + 1).fill(0);
  const queue = [1];
  visited[1] = 1;

  while (queue.length > 0) {
    const now = queue.shift();

    for (let ni in maps[now]) {
      let nxt = maps[now][ni];
      if (visited[nxt] == 0) {
        queue.push(nxt);
        visited[nxt] = visited[now] + 1;
      }
    }
  }

  let max = 0,
    answer = 0;
  for (let i in visited) {
    if (visited[i] > max) {
      max = visited[i];
      answer = 1;
    } else if (visited[i] == max) answer++;
  }

  return answer;
}
