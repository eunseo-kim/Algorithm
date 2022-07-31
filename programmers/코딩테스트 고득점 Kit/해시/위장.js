/*
========================================================
언어 : Javascript
날짜 : 2022.7.31
문제 : 위장
레벨 : level 2
========================================================
*/

function solution(clothes) {
  const spy = {};
  clothes.forEach(([cloth, kind]) => {
    spy[kind] = spy[kind] ? [...spy[kind], cloth] : [cloth];
  });

  const cases = [];
  Object.values(spy).forEach((_case) => cases.push(_case.length));

  let answer = 1;
  for (let i = 0; i < cases.length; i += 1) {
    answer *= cases[i] + 1;
  }

  return answer - 1;
}

const clothes = [
  ['crow_mask', 'face'],
  ['blue_sunglasses', 'face'],
  ['smoky_makeup', 'face'],
];

const result = solution(clothes);
console.log(result);
