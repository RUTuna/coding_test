function solution(tickets) {
  let answer = [];
  let contury = new Set();
  let contury_index = {};

  for (let [s, d] of tickets) {
    contury.add(s);
    contury.add(d);
  }
  contury = [...contury].sort();
  for (let i in contury) contury_index[contury[i]] = i;

  const contury_len = contury.length;
  const maps = Array.from({ length: contury_len }, () => Array(contury_len).fill(0));
  for (let [s, d] of tickets) maps[contury_index[s]][contury_index[d]]++;

  function DFS(now, path) {
    if (answer.length) return;
    if (path.length === tickets.length + 1) {
      answer = path;
      return;
    }

    for (let i in maps[now]) {
      if (maps[now][i]) {
        maps[now][i]--;
        DFS(i, [...path, contury[i]]);
        maps[now][i]++;
      }
    }
  }

  DFS(contury_index["ICN"], ["ICN"]);

  return answer;
}
