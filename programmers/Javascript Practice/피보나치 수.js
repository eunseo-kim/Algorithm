function solution(n) {
    const array = new Array(n+1);
    array[0] = 0;
    array[1] = 1;
    
    for (let i=2; i<=n; i+=1) {
        array[i] = (array[i-1] + array[i-2]) % 1234567;
    }
    
    return array[n] % 1234567;
}