/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
  let zeros = nums.filter((e) => !e).length;
  if (zeros > 1) return Array(nums.length).fill(0);
  let total = nums.reduce((acc, cur) => (cur ? acc * cur : acc), 1);
  if (zeros === 1) return nums.map((e) => (e ? 0 : total));
  return nums.map((e) => total / e);
};
