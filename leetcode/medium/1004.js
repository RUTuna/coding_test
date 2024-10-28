/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var longestOnes = function (nums, k) {
  let count = 0;
  let queue = [];
  let answer = 0;

  for (let num of nums) {
    if (num) queue.push(num);
    else {
      answer = Math.max(answer, queue.length);
      if (count === k) {
        while (queue[0] === 1) queue.shift();
        if (queue[0] === 0) {
          queue.shift();
          count--;
        }
      }
      if (count < k) {
        queue.push(num);
        count++;
      }
    }
  }

  return Math.max(answer, queue.length);
};
