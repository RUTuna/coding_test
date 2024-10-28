/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function (word1, word2) {
  let answer = [];
  let len1 = word1.length,
    len2 = word2.length;

  for (let i = 0; i < Math.max(len1, len2); i++) {
    if (i < len1) answer.push(word1[i]);
    if (i < len2) answer.push(word2[i]);
  }

  return answer.join("");
};
