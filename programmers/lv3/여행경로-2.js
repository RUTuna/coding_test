function solution(tickets) {
  let answer = ["ICN"];
  let country = new Set();
  let country_index = {};

  for (let [s, d] of tickets) {
    country.add(s);
    country.add(d);
  }
  let countryList = [...country].sort();
  let conturyLen = countryList.length;
  countryList.forEach((v, i) => (country_index[v] = i));
  let maps = Array.from({ length: conturyLen }, () => Array(conturyLen).fill(0));
  for (let [s, d] of tickets) {
    maps[country_index[s]][country_index[d]]++;
  }

  let isDone = false;
  function DFS(now, path) {
    if (path.length === tickets.length + 1) {
      answer = path;
      isDone = true;
      return;
    }

    for (let i = 0; i < conturyLen; i++) {
      if (maps[now][i]) {
        maps[now][i]--;
        DFS(i, [...path, countryList[i]]);
        maps[now][i]++;
      }
      if (isDone) break;
    }
  }

  DFS(country_index["ICN"], ["ICN"]);

  return answer;
}
