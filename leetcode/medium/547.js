/**
 * @param {number[][]} isConnected
 * @return {number}
 */
var findCircleNum = function (isConnected) {
  let answer = 0;
  let n = isConnected.length;
  let visited = Array(n).fill(false);

  let DFS = function (cur) {
    visited[cur] = true;

    for (let i = 0; i < n; i++) {
      if (isConnected[cur][i] && !visited[i]) DFS(i);
    }
  };

  for (let i = 0; i < n; i++) {
    if (!visited[i]) {
      answer++;
      DFS(i);
    }
  }

  return answer;
};
