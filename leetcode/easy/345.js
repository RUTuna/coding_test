/**
 * @param {string} s
 * @return {string}
 */

var reverseVowels = function (s) {
  let re = /[aeiou]/i;
  let vowles = s.split("").filter((e) => re.test(e));
  return s
    .split("")
    .map((e, i) => (re.test(e) ? vowles.pop() : s[i]))
    .join("");
};
