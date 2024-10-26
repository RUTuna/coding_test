let fs = require("fs");
let input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n")
  .map((r) => r.split(" ").map(Number));

function solution(mathes) {
  let [win, lose, duo, country] = [0, 0, 0, 0];

  for (let i = 0; i < 18; i++) {
    if (i % 3 === 0) {
      country = mathes[i];
      win += mathes[i];
    } else if (i % 3 === 1) {
      country += mathes[i];
      duo += mathes[i];
    } else {
      if (country !== 5 - mathes[i]) return 0;
      lose += mathes[i];
    }
  }

  if (win !== lose || duo % 2) return 0;
  return 1;
}

let answer = [];
for (let i = 0; i < 4; i++) {
  answer.push(solution(input[i]));
}

console.log(...answer);
