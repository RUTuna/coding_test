/**
 * @param {number[]} gain
 * @return {number}
 */
var largestAltitude = function (gain) {
  let cur = 0,
    max = 0;
  gain.forEach((e) => {
    cur += e;
    max = Math.max(max, cur);
  });

  return max;
};
