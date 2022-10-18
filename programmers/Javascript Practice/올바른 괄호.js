function solution(s){
    if (s.length <= 1) return false;
    if (s.length % 2 == 1) return false;
    
    const stack = new Array();
    s.split("").forEach((char) => {
        if (char === '(') {
            stack.push(char);
        } else {
            if (stack.length == 0) {
                return false;
            }
            stack.pop();
        }
    });

    if (stack.length != 0) return false;
    return true;
}
