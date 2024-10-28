/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findMaxAverage = function (nums, k) {
  let max = nums.slice(0, k).reduce((acc, cur) => acc + cur);
  let cur = max;

  for (let i = k; i < nums.length; i++) {
    cur = cur - nums[i - k] + nums[i];
    max = Math.max(max, cur);
  }

  return max / k;
};
