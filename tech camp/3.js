function solution(board) {
  // [1] 연결된 각 조각마다 고유한 번호를 붙이고 조각의 크기 알아내기
  const n = board.length;

  const visited = []; // 이미 방문한 조각인지 여부
  const newBoard = []; // 조각 id로 board 표시

  for (let i = 0; i < n; i += 1) {
    const v = [];
    const b = [];
    for (let j = 0; j < n; j += 1) {
      v.push(false);
      b.push(0);
    }
    visited.push(v);
    newBoard.push(b);
  }

  const moves = [[0, 1], [1, 0], [-1, 0], [0, -1]];

  const partSizes = {}; // id 별로 조각의 크기를 저장
  let id = 0; // 조각의 고유한 id (알파벳이 같아도 떨어져있는 조각이면 id가 다름)

  for (let row = 0; row < n; row += 1) {
    for (let col = 0; col < n; col += 1) {
      let size = 0; // 현재 조각과 연결된 조각의 크기 찾기
      let check = false;

      if (visited[row][col] === false) {
        const queue = [[row, col]];
        check = true;

        while (queue.length > 0) {
          const loc = queue.pop();
          newBoard[loc[0]][loc[1]] = id;

          const currentAlpha = board[loc[0]][loc[1]];

          if (visited[loc[0]][loc[1]] == false) {
            visited[loc[0]][loc[1]] = true;
            size += 1;
            moves.forEach((move) => {
              const nextRow = loc[0] + move[0];
              const nextCol = loc[1] + move[1];

              if (nextRow >= 0 && nextRow < n && nextCol >= 0 && nextCol < n) {
                if (board[nextRow][nextCol] === currentAlpha) {
                  queue.push([nextRow, nextCol]);
                }
              }
            });
          }
        }
      }

      // 조각의 크기를 기억하기
      if (check === true) {
        partSizes[id] = size;
        id += 1;
      }
    }
  }

  // [2] 각 줄마다 Set 안에 [번호, 크기]를 넣고 마지막에 블록의 크기를 계산
  let maxSum = 0;

  // [2-1] 가로 줄 비교
  for (let row = 0; row < n; row += 1) {
    const idSet = new Set();
    for (let col = 0; col < n; col += 1) {
      const id = newBoard[row][col];
      idSet.add(id);
    }

    // [3] 빈칸 블록 크기 계산하고 가장 큰 경우 갱신
    let currSum = 0;
    idSet.forEach((id) => {
      currSum += partSizes[id];
    });
    maxSum = Math.max(maxSum, currSum);
  }

  // [2-2] 세로 줄 비교
  for (let col = 0; col < n; col += 1) {
    const idSet = new Set();
    for (let row = 0; row < n; row += 1) {
      const id = newBoard[row][col];
      idSet.add(id);
    }

    // [3] 빈칸 블록 크기 계산하고 가장 큰 경우 갱신
    let currSum = 0;
    idSet.forEach((id) => {
      currSum += partSizes[id];
    });
    maxSum = Math.max(maxSum, currSum);
  }

  return maxSum;
}
