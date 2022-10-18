function solution(s) {
    const arr = s.split(" ").map((string) => Number(string))
    let answer = '';
    answer += Math.min(...arr)
    answer += " "
    answer += Math.max(...arr)
    
    return answer;
}