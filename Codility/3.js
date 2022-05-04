function solution(S) {
  const maxLength = S.length;

  let cut = 1; // cut의 초깃값은 1
  const letterSet = new Set();

  for (let i = 0; i < maxLength; i += 1) {
    const currentLetter = S[i];

    // 이전까지의 letterSet에 중복되는 letter이 있으면 cut을 1 늘린다.
    if (letterSet.has(currentLetter)) {
      cut += 1;
      letterSet.clear(); // 그리고 letterSet을 다시 초기화시킨다.
    }
    letterSet.add(currentLetter);
  }

  return cut;
}

const result = solution('abbasseua');
console.log('result', result);
