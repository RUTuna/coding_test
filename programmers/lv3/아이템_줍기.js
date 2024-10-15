function solution(rectangle, characterX, characterY, itemX, itemY) {
  const maps = Array.from({ length: 102 }, () => Array(102).fill(-1));
  rectangle = rectangle.map((element) => element.map((ele) => ele * 2));
  const new_value = [characterX, characterY, itemX, itemY].map((ele) => ele * 2);

  function filling(rect) {
    for (let i = rect[0]; i <= rect[2]; i++) {
      for (let j = rect[1]; j <= rect[3]; j++) {
        if (rect[0] < i && i < rect[2] && rect[1] < j && j < rect[3]) maps[i][j] = 0;
        else maps[i][j] = maps[i][j] ? 1 : 0;
      }
    }
  }

  for (let r of rectangle) filling(r);

  const direct = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
  ];
  const queue = [[new_value[0], new_value[1], 0]];

  while (queue.length > 0) {
    let [r, c, depth] = queue.shift();
    if (r === new_value[2] && c === new_value[3]) return depth / 2;

    for (let [dr, dc] of direct) {
      let nr = dr + r,
        nc = dc + c;
      if (0 <= nr && nr < 102 && 0 <= nc && nc < 102 && maps[nr][nc] == 1) {
        maps[r][c] = 0;
        queue.push([nr, nc, depth + 1]);
      }
    }
  }

  return 0;
}
