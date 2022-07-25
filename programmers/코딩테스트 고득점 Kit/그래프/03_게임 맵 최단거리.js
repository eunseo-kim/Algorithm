/*
========================================================
언어 : Javascript
날짜 : 2022.7.25
문제 : 게임 맵 최단거리
레벨 : level 2
========================================================
*/

function solution(maps) {
  const moves = [[0, 1], [1, 0], [0, -1], [-1, 0]];

  const N = maps.length;
  const M = maps[0].length;

  const queue = [[0, 0, 1]];
  const visited = Array.from(Array(N), () => Array(M).fill(false));

  while (queue.length > 0) {
    const [row, col, count] = queue.shift();

    if (row === N - 1 && col === M - 1) {
      return count;
    }

    if (!visited[row][col]) {
      visited[row][col] = true;

      moves.forEach(([r, c]) => {
        const newRow = row + r;
        const newCol = col + c;

        if (newRow >= 0 && newRow < N
              && newCol >= 0 && newCol < M
              && maps[newRow][newCol] !== 0
              && !visited[newRow][newCol]) {
          queue.push([newRow, newCol, count + 1]);
        }
      });
    }
  }

  return -1;
}

const maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]];
const result = solution(maps);
console.log(result);
