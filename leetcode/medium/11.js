/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function (height) {
  let n = height.length;
  let left = 0,
    right = n - 1;
  let answer = 0;

  while (left < right) {
    answer = Math.max(answer, Math.min(height[left], height[right]) * (right - left));
    let leftH = height[left],
      rightH = height[right];

    if (leftH < rightH) {
      while (leftH >= height[left]) left++;
    } else {
      while (rightH >= height[right]) right--;
    }
  }

  return answer;
};
