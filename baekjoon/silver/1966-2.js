let fs = require("fs");
let input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

function solution(n, target, arr) {
  let counter = Array(10).fill(0);
  let answer = Array(n).fill(0);
  let priority = 1;

  for (let i in arr) counter[arr[i]]++;

  let j = 0;
  for (let i = 9; i > 0; i--) {
    for (; counter[i] > 0; j = (j + 1) % n) {
      if (i === arr[j]) {
        counter[i]--;
        answer[j] = priority;
        priority++;
      }
    }
  }

  return answer[target];
}

for (let i = 0; i < Number(input[0]); i++) {
  const [n, target] = input[i * 2 + 1].split(" ").map(Number);
  const arr = input[i * 2 + 2].length > 1 ? input[i * 2 + 2].split(" ").map(Number) : [Number(input[i * 2 + 2])];
  console.log(solution(n, target, arr));
}
