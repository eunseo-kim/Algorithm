// [1] 숫자-기호 조합표 만들기
const number2sign = {
  0: ['O', '()'],
  1: ['I'],
  2: ['Z', 'S', '7_'],
  3: ['E', 'B'],
  4: ['A'],
  5: ['Z', 'S'],
  6: ['b', 'G'],
  7: ['T', 'Y'],
  8: ['B', 'E3'],
  9: ['g', 'q'],
};

const allCases = new Set();

function getAllCases(words, idx, path, used) {
  if (idx === words.length - 1) {
    allCases.add(path);
    return;
  }

  for (let i = idx + 1; i < words.length; i += 1) {
    const number = Number(words[i]);
    const signs = number2sign[number];
    signs.forEach((sign) => {
      if (sign in used) {
        // sign을 이미 사용했다면 같은 숫자로 사용했는지 체크
        if (used[sign] === number) {
          const newPath = path + sign;
          getAllCases(words, i, newPath, used);
        }
      } else {
        const newPath = path + sign;
        used[sign] = number;
        getAllCases(words, i, newPath, used);
      }
    });
  }
}

function solution(numstrs, words) {
  const result = [];

  // [2] 가능한 모든 경우 조합을 구하기
  words.forEach((word) => {
    allCases.clear();
    let count = 0;

    getAllCases(word, -1, '', {});

    // [3] 정규식 search로 포함하고 있는지 구하기
    allCases.forEach((w) => {
      numstrs.forEach((s) => {
        if (s.search(w) !== -1) {
          count += 1;
        }
      });
    });

    result.push(count);
  });

  return result;
}
