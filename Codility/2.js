function solution(S) {
  let prevLetter = S[0]; // N은 1 ~ 200000이므로 S[0]이 존재함
  let index = 1; // index of S
  let result = prevLetter; // 첫 글자는 포함하고 시작함
  let continuousLength = 1; // 연속되는 길이 (첫 글자를 포함하므로 초깃값은 1)

  const maxLength = S.length;

  while (index < maxLength) {
    const currentLetter = S[index];

    // 현재 글자의 연속되는 길이가 3보다 크면 result에 넣지 않음
    if (currentLetter === prevLetter) {
      continuousLength += 1;
      if (continuousLength < 3) {
        result += currentLetter;
      }
    } else { // 연속이 끊기는 부분 (continuousLength, prevLetter을 새로 갱신함)
      result += currentLetter;
      continuousLength = 1;
      prevLetter = S[index];
    }
    index += 1;
  }

  return result;
}

const result = solution('eeeuussssxx');
console.log('result', result);
