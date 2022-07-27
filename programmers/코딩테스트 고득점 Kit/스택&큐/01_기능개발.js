/*
========================================================
언어 : Javascript
날짜 : 2022.7.27
문제 : 기능개발
레벨 : level 2
========================================================
*/

function solution(progresses, speeds) {
  const requiredDays = [];

  progresses.forEach((progress, i) => {
    const need = 100 - progress;
    const speed = speeds[i];
    requiredDays.push(Math.ceil(need / speed));
  });

  const answer = [];
  let cnt = 0;
  let boundary = requiredDays[0];
  requiredDays.forEach((days) => {
    if (days > boundary) {
      answer.push(cnt);
      boundary = days;
      cnt = 1;
    } else {
      cnt += 1;
    }
  });
  answer.push(cnt);

  return answer;
}

const pregresses = [95, 90, 99, 99, 80, 99];
const speeds = [1, 1, 1, 1, 1, 1];
console.log(solution(pregresses, speeds));
