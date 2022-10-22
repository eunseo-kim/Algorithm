function solution(n, works) {
    works.sort((a, b) => b - a);
    let maxAmount = works[0];
    const worksLength = works.length;
    
    while (n > 0) {
        for (let i=0; i<worksLength; i+=1) {
            if (works[i] === maxAmount) {
                works[i] -= 1;
                maxAmount = Math.max(works[i], works[i+1] || 0);
                break;
            }
        }
        n -= 1;
    }
    
    return works.reduce((acc, cur) => {
        if (cur < 0) cur = 0;
        return acc + (cur * cur);
    }, 0);
}