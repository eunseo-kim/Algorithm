/*
========================================================
언어 : Javascript
날짜 : 2022.8.18
문제 : H-Index
레벨 : level 2
========================================================
*/

function solution(citations) {
  const sortedCitations = citations.sort((a, b) => a - b);

  let answer = 0;
  const N = sortedCitations.length;
  for (let i = N - 1, count = 1; i > -1; i -= 1, count += 1) {
    if (sortedCitations[i] >= count) answer = count;
  }

  return answer;
}

const result = solution([3, 0, 6, 1, 5, 4]);
console.log(result);
