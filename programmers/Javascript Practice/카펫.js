function solution(brown, yellow) {
    const brownCount = parseInt((brown + 4) / 2);
    for (let col=2; col<=parseInt(brownCount/2); col+=1) {
        const row = brownCount - col;
        const yellowRow = row-2;
        const yellowCol = col-2;
        if (yellowRow * yellowCol === yellow) {
            return [row, col];
        }
    }
}