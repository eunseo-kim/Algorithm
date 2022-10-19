let maxCount = 0;

function dfs(dungeons, gauge, N, count, path) {
    maxCount = Math.max(maxCount, count);
    
    for (let j=0; j<N; j+=1) {
        if (dungeons[j][0] <= gauge && !path.includes(j)) {
            dfs(dungeons, gauge - dungeons[j][1], N, count + 1, path.concat([j]));
        }
    }
}

function solution(k, dungeons) {
    dfs(dungeons, k, dungeons.length, 0, []);
    return maxCount;
}