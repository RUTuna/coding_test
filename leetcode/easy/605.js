/**
 * @param {number[]} flowerbed
 * @param {number} n
 * @return {boolean}
 */
var canPlaceFlowers = function (flowerbed, n) {
  let newFlowerbed = [0, ...flowerbed, 0];
  let answer = 0;
  let start = 0;

  while (start < newFlowerbed.length) {
    if (newFlowerbed[start]) start++;
    else {
      let end = start + 1;
      while (end < newFlowerbed.length && !newFlowerbed[end]) end++;
      if (end - start - 1 > 0) {
        answer += parseInt((end - start - 1) / 2);
      }
      start = end;
    }
  }

  return answer >= n ? true : false;
};
