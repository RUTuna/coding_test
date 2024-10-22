function solution(n, results) {
  let answer = 0;
  const maps = Array.from({ length: n }, () => Array(n).fill(Number.MAX_SAFE_INTEGER));

  for (let [w, l] of results) maps[w - 1][l - 1] = 1;
  for (let i = 0; i < n; i++) maps[i][i] = 0;

  for (let d = 0; d < n; d++) {
    for (let a = 0; a < n; a++) {
      for (let b = 0; b < n; b++) {
        maps[a][b] = Math.min(maps[a][b], maps[a][d] + maps[d][b]);
      }
    }
  }

  for (let a = 0; a < n; a++) {
    let count = 0;
    for (let b = 0; b < n; b++) {
      if (maps[a][b] !== Number.MAX_SAFE_INTEGER || maps[b][a] !== Number.MAX_SAFE_INTEGER) count++;
    }

    if (count === n) answer++;
  }

  return answer;
}
