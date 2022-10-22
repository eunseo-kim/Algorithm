function solution(begin, target, words) {
    let turns = 0;
    let used = [];
    const stack = [];
    let minTurns = Number.MAX_VALUE;
    
    stack.push([begin, turns, used]);
    while (stack.length > 0) {
        let [curr, turns, used] = stack.pop();
        
        if (curr == target) {
            minTurns = Math.min(minTurns, turns);
            continue;
        }
        
        for (let i=0; i<words.length; i+=1) {
            if (!used.includes(words[i])) {
                let changedWords = 0;
                [...words[i]].forEach((letter, j) => {
                    if (letter !== curr[j]) changedWords += 1;
                });
                
                if (changedWords === 1) {
                    stack.push([words[i], turns + 1, used.concat([words[i]])]);
                }
            }
        }
    }
    
    if (minTurns === Number.MAX_VALUE) return 0;
    return minTurns;
}