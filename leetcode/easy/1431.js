/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
var kidsWithCandies = function (candies, extraCandies) {
  let maxCandy = Math.max(...candies);
  return candies.map((c) => (c + extraCandies >= maxCandy ? true : false));
};
