function solution(s) {
    const arr = s.split(" ");
    const answer = arr.map((string) => {
        return string.substring(0, 1).toUpperCase() + (string.substring(1)).toLowerCase();
    });
    return answer.join(" ");
}