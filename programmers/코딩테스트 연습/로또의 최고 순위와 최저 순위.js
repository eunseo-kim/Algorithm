/*
========================================================
언어 : Javascript
날짜 : 2022.8.12
문제 : 로또의 최고 순위와 최저 순위
레벨 : level 1
========================================================
*/

function solution(lottos, winNums) {
  const scoreBoard = [6, 6, 5, 4, 3, 2, 1];

  // [1] 보이는 숫자들 중에 몇개 당첨 됐는지
  // [2] 안보이는 숫자(0)의 개수
  // [3] 당첨번호 중 민우가 사용하지 않은 숫자 개수

  let winningScore = 0; // [1]
  let deletedNumbers = 0; // [2]

  lottos.forEach((lotto) => {
    if (lotto === 0) {
      deletedNumbers += 1;
    }

    if (winNums.includes(lotto)) {
      winningScore += 1;
    }
  });

  const notUsedWinningNumbers = 6 - winningScore; // [3]

  // 최저 순위 => [1]
  // 최대 순위 => min([2], [3])
  const minScore = winningScore;
  const maxScore =
    winningScore + Math.min(deletedNumbers, notUsedWinningNumbers);

  return [scoreBoard[maxScore], scoreBoard[minScore]];
}

solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]);
