function solution(prices) {
  let n = prices.length;
  let answer = Array(n).fill(0);

  let stack = [];

  prices.forEach((cur, i) => {
    while (stack.length > 0 && stack[stack.length - 1][0] > cur) {
      let top = stack.pop();
      answer[top[1]] = i - top[1];
    }
    stack.push([cur, i]);
  });

  for (let cur of stack) answer[cur[1]] = n - cur[1] - 1;

  return answer;
}
