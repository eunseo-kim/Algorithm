function solution(n, words) {
    let answer = [0, 0];
    const wordSet = new Set();
    words.reduce((prevLetter, currentWord, i, src) => {
        const currentLetter = currentWord[0];
        if (prevLetter.length > 0 && prevLetter !== currentLetter) {
            answer = [i%n+1, Math.ceil((i+1)/n)];
            src.splice(0);
        }
        
        if (wordSet.has(currentWord)) {
            answer = [i%n+1, Math.ceil((i+1)/n)];
            src.splice(0);
        }
        
        wordSet.add(currentWord);
        return currentWord[currentWord.length-1];
    }, '');
    
    return answer;
}