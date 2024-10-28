/**
 * @param {number[]} nums
 * @return {boolean}
 */
var increasingTriplet = function (nums) {
  let first = Number.MAX_SAFE_INTEGER,
    second = Number.MAX_SAFE_INTEGER;

  for (let third of nums) {
    if (third < first) first = third;
    else if (third < second && first < third) second = third;
    else if (second < third && first < third) return true;
  }

  return false;
};
