/**
 * @param {number} k
 * @param {number} n
 * @return {number[][]}
 */
var combinationSum3 = function (k, n) {
  let answer = [];

  let DFS = function (cur, sum, path) {
    if (path.length === k) {
      if (sum === n) answer.push(path);
      return;
    }

    if (cur > 9) return;

    DFS(cur + 1, sum + cur, [...path, cur]);
    DFS(cur + 1, sum, path);
  };

  DFS(1, 0, []);
  return answer;
};
