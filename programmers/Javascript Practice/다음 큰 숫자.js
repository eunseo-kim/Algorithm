function solution(n) {
    var answer = 0;
    
    let myCount = 0;
    const nStr = n.toString(2);
    (nStr.split("")).forEach((element) => {
        if (element === '1') myCount += 1;
    });
    
    let nextNumber = n+1;
    while (true) {
        const nextBinary = nextNumber.toString(2);
        let count = 0;
        (nextBinary.split("")).forEach((element) => {
            if (element === '1') count += 1;
        });
        
        if (count === myCount) return nextNumber;
        nextNumber += 1;
    }
}