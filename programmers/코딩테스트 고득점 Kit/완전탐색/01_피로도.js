/*
========================================================
언어 : Javascript
날짜 : 2022.7.26
문제 : 피로도
레벨 : level 2
========================================================
*/

function solution(k, dungeons) {
  const N = dungeons.length;
  const visited = Array(8).fill(false);
  let maxCount = 0;

  function dfs(fatigue, count) {
    dungeons.forEach(([required, cost], j) => {
      if (!visited[j]) {
        if (fatigue >= required && fatigue - cost >= 0) {
          visited[j] = true;
          dfs(fatigue - cost, count + 1, N);
          visited[j] = false;
        }
      }
    });

    maxCount = Math.max(maxCount, count);
  }

  dfs(k, 0);
  return maxCount;
}

// 입력 및 실행
const k = 80;
const dungeons = [
  [80, 20],
  [50, 40],
  [30, 10],
];

const result = solution(k, dungeons);
console.log(result);
