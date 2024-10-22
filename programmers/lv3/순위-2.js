function solution(n, results) {
  let cost = Array.from({ length: n }, () => Array(n).fill(Number.MAX_SAFE_INTEGER));
  for (let i = 0; i < n; i++) cost[i][i] = 0;
  for (let [w, l] of results) cost[w - 1][l - 1] = 1;

  for (let m = 0; m < n; m++) {
    for (let w = 0; w < n; w++) {
      for (let l = 0; l < n; l++) {
        cost[w][l] = Math.min(cost[w][l], cost[w][m] + cost[m][l]);
      }
    }
  }

  let answer = 0;
  for (let i = 0; i < n; i++) {
    let connect = 0;
    for (let j = 0; j < n; j++) {
      if (cost[i][j] !== Number.MAX_SAFE_INTEGER || cost[j][i] !== Number.MAX_SAFE_INTEGER) connect++;
    }
    if (connect === n) answer++;
  }

  return answer;
}
