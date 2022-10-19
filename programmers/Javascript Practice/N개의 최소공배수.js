function LCM(n1, n2) {
    if (n1 < n2) {
        [n1, n2] = [n2, n1]; // swap
    }
    
    let a = n1;
    let b = n2;
    
    // 최대공약수
    while (b != 0) {
        let n = a % b;
        a = b;
        b = n;
    }
    
    return a * Number(n1 / a) * Number(n2 / a);
}

function solution(arr) {
    let lcm = 1;
    for (let i=0; i<arr.length; i+=1) {
        lcm = LCM(lcm, arr[i]);
    }
    
    return lcm;
}