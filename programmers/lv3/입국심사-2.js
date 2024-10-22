function solution(n, times) {
  let answer = 0;
  let l = times.length;
  let left = Math.min(...times),
    right = Math.max(...times) * (n - l + 1);

  while (left <= right) {
    let mid = parseInt((left + right) / 2);

    let count = 0;
    for (let i = 0; i < l; i++) {
      count += parseInt(mid / times[i]);
      if (count > n) break;
    }

    if (count < n) {
      left = mid + 1;
    } else {
      answer = mid;
      right = mid - 1;
    }
  }
  return answer;
}
