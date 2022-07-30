/*
========================================================
언어 : Javascript
날짜 : 2022.7.30
문제 : 베스트앨범
레벨 : level 3
========================================================
*/

function solution(genres, plays) {
  const player = {};

  genres.forEach((genre, i) => {
    if (!player[genre]) player[genre] = { count: 0, playList: [] };
    player[genre].count += plays[i];
    player[genre].playList.push([plays[i], i]);
  });

  // sort by count
  const answer = [];
  Object.keys(player)
    .sort((a, b) => player[b].count - player[a].count)
    .forEach((genre) => {
      const sortedList = player[genre].playList.sort((a, b) => {
        if (a[0] === b[0]) return a[1] - b[1];
        return b[0] - a[0];
      });

      sortedList.forEach(([, i], index) => {
        if (index <= 1) answer.push(i);
      });
    });

  return answer;
}

const genres = ['classic', 'pop', 'classic', 'classic', 'pop'];
const plays = [500, 600, 150, 800, 2500];
const result = solution(genres, plays);
console.log(result);
