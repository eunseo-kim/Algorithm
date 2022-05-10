function solution(scores) {
  // [1] 어려운 문제(difficult) 구하기
  let score1 = 0;
  let score2 = 0;

  scores.forEach((score) => {
    score1 += score[0];
    score2 += score[1];
  });

  let difficult = -1; // -1은 어려운 문제가 존재하지 않는 경우
  if (score1 > score2) {
    difficult = 1;
  } else if (score1 < score2) {
    difficult = 0;
  }

  // [2] 점수 총점 계산하기
  const scoreList = [];
  const n = scores.length;
  for (let i = 0; i < n; i += 1) {
    const scoreSum = scores[i][0] + scores[i][1];

    if (difficult !== -1) {
      // [합계, 어려운문제 점수, 응시자 ID] 순으로 저장
      scoreList.push([scoreSum, scores[i][difficult], i + 1]);
    } else { // 어려운 문제가 없는 경우
      scoreList.push([scoreSum, 0, i + 1]);
    }
  }

  // [3] [합계, 어려운문제 점수, 응시자 ID] 순으로 정렬하기
  const sortedScoreList = scoreList.sort((a, b) => {
    if (a[0] === b[0]) {
      if (a[1] === b[1]) {
        return a[2] - b[2]; // ID는 더 작은 순서대로
      }
      return b[1] - a[1];
    }
    return b[0] - a[0];
  });

  // [4] key(=응시자 ID) / value(=순위) 저장하기
  const result = {};
  for (let i = 1; i <= n; i += 1) {
    result[sortedScoreList[i - 1][2]] = i;
  }

  // [5] 결과 출력
  const answer = [];
  for (let i = 1; i <= n; i += 1) {
    answer.push(result[i]);
  }

  return answer;
}
