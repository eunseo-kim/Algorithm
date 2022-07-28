/*
========================================================
언어 : Javascript
날짜 : 2022.7.28
문제 : K번째 수
레벨 : level 1
========================================================
*/

function solution(array, commands) {
  const answer = [];
  commands.forEach(([i, j, k]) => {
    const arr = array.slice(i - 1, j);
    arr.sort((a, b) => a - b);
    answer.push(arr[k - 1]);
  });
  return answer;
}

const array = [1, 5, 2, 6, 3, 7, 4];
const commands = [
  [2, 5, 3],
  [4, 4, 1],
  [1, 7, 3],
];
const result = solution(array, commands);
console.log(result);
