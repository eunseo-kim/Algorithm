function solution(N, K) {
  let n = N;
  let k = K;

  // [1] 백의 자리(hundreds), 십의 자리(tens), 일의 자리(units)
  let hundreds = parseInt(n / 100, 10);
  n -= 100 * hundreds;
  let tens = parseInt(n / 10, 10);
  n -= 10 * tens;
  let units = n;

  // [2] 큰 자릿수부터 차례대로 1씩 추가 → 최대 K번까지
  while (k > 0) {
    if (hundreds < 9) {
      hundreds += 1;
    } else if (tens < 9) {
      tens += 1;
    } else if (units < 9) {
      units += 1;
    } else {
      break; // 만약 999라면 while문 종료
    }
    k -= 1;
  }

  // [3] 최대로 가능한 세`자리 수 구하기
  const result = 100 * hundreds + 10 * tens + units;

  return result;
}

const result = solution(100, 10);
console.log('result', result);
