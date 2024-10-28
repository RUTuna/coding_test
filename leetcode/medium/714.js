/**
 * @param {number[]} prices
 * @param {number} fee
 * @return {number}
 */
var maxProfit = function (prices, fee) {
  let sell = 0,
    buy = -Number.MAX_SAFE_INTEGER;

  for (let price of prices) {
    sell = Math.max(sell, buy + price); // 계속 가지고 있기 vs 지금 팔기
    buy = Math.max(buy, sell - price - fee); // 계속 안 사고 있기 vs 지금 사기
  }

  return sell;
};
