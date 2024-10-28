/**
 * @param {character[]} chars
 * @return {number}
 */
var compress = function (chars) {
  let answer = [];
  let cur = chars[0],
    count = 0;

  for (let c of chars) {
    if (cur !== c) {
      answer.push(cur);
      if (count > 1) answer.push(count + "");
      cur = c;
      count = 1;
    } else count++;
  }

  answer.push(cur);
  if (count > 1) answer.push(count + "");

  answer = answer.join("").split("");
  for (let i = 0; i < answer.length; i++) chars[i] = answer[i];
  return answer.length;
};
