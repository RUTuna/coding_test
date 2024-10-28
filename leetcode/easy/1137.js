/**
 * @param {number} n
 * @return {number}
 */
var tribonacci = function (n) {
  let dp = Array(38).fill(-1);
  [dp[0], dp[1], dp[2]] = [0, 1, 1];

  let recur = function (num) {
    if (dp[num] >= 0) return dp[num];
    dp[num] = recur(num - 3) + recur(num - 2) + recur(num - 1);
    return dp[num];
  };

  return recur(n);
};
