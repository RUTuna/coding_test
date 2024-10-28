/**
 * @param {string} str1
 * @param {string} str2
 * @return {string}
 */

let getGCD = function (num1, num2) {
  return num2 > 0 ? getGCD(num2, num1 % num2) : num1;
};

var gcdOfStrings = function (str1, str2) {
  let gcd = getGCD(str1.length, str2.length);
  let gcdString = str1.slice(0, gcd);

  for (let i = 0; i < Math.max(str1.length, str2.length); i += gcd) {
    if (i + gcd <= str1.length && gcdString !== str1.slice(i, i + gcd)) {
      gcdString = "";
      break;
    }
    if (i + gcd <= str2.length && gcdString !== str2.slice(i, i + gcd)) {
      gcdString = "";
      break;
    }
  }

  return gcdString;
};
