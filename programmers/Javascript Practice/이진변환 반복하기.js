function changeToBinary(number) {
    let binary = '';
    while (number > 0) {
        binary = String(number % 2) + binary;
        number = parseInt(number / 2);
    }
    
    return binary;
}

function solution(s) {
    let removedZeroCount = 0;
    let replaceCount = 0;
    let string = s;
    
    while (string != '1') {
        let newString = '';
        for (let i=0; i<string.length; i+=1) {
            if (string[i] == '0') {
                removedZeroCount += 1;
            } else {
                newString += string[i];
            }
        }
        string = changeToBinary(newString.length);
        replaceCount += 1;
    }
    
    return [replaceCount, removedZeroCount];
}