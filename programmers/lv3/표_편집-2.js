function solution(n, k, cmds) {
  let cur = k + 1,
    lastIndex = n;
  let linked = Array.from({ length: n + 2 }, (_, i) => [i - 1, i + 1]);
  let state = Array(n + 2).fill(true);
  let trash = [];

  for (let cmd of cmds) {
    let c = cmd.split(" ");

    if (c[0] === "U" || c[0] === "D") {
      let count = Number(c[1]);
      while (count > 0) {
        cur = linked[cur][c[0] === "U" ? 0 : 1];
        count--;
      }
    } else if (c[0] === "C") {
      state[cur] = false;
      trash.push(cur);
      let nxtIndex = linked[cur][cur === lastIndex ? 0 : 1];
      if (cur === lastIndex) lastIndex = nxtIndex;
      linked[linked[cur][0]][1] = linked[cur][1];
      linked[linked[cur][1]][0] = linked[cur][0];
      cur = nxtIndex;
    } else if (c[0] === "Z") {
      let alive = trash.pop();
      state[alive] = true;
      if (alive > lastIndex) lastIndex = alive;
      linked[linked[alive][0]][1] = alive;
      linked[linked[alive][1]][0] = alive;
    }
  }

  return state
    .slice(1, n + 1)
    .map((e) => (e ? "O" : "X"))
    .join("");
}
