function solution(n) {
    let left = 1;
    let right = 1;
    let sum = 1;
    let answer = 0;
    
    while (left <= right) {
        if (sum == n) {
            answer += 1;
            sum -= left;
            left += 1;
            continue;
        }
        
        if (sum > n) {
            sum -= left;
            left += 1;
            continue;
        }
        
        right += 1;
        sum += right;
    }
    
    return answer
}