function solution(s) {
    const lst = s.split("");
    const stack = [lst.pop(0)];
    
    lst.forEach((num) => {
        if (stack.length > 0 && stack[stack.length-1] === num) {
            stack.pop();
        } else {
            stack.push(num);
        }
    })
    return Number(stack.length === 0);
}