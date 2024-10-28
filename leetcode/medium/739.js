/**
 * @param {number[]} temperatures
 * @return {number[]}
 */
var dailyTemperatures = function (temperatures) {
  let n = temperatures.length;
  let answer = Array(n).fill(0);
  let stack = [];

  temperatures.forEach((e, i) => {
    while (stack.length && stack[stack.length - 1][0] < e) {
      let [_, index] = stack.pop();
      answer[index] = i - index;
    }
    stack.push([e, i]);
  });

  return answer;
};
