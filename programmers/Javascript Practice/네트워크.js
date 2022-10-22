function solution(n, computers) {
    let answer = 0;
    const visited = new Array(n).fill(false);
    for (let i=0; i<n; i+=1) {
        if (!visited[i]) {
            answer += 1;
            visited[i] = true;
            dfs(i, visited, computers, n);
        }
    }
    
    return answer;
}

function dfs(curr, visited, computers, n) {
    for (let i=0; i<n; i+=1) {
        if (i !== curr && !visited[i] && computers[curr][i] == 1) {
            visited[i] = true;
            dfs(i, visited, computers, n);
        }
    }
}