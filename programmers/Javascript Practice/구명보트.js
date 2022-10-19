function solution(people, limit) {
    let left = 0;
    let right = people.length - 1;
    
    people.sort((a, b) => a - b);
    let boatCount = 0;
    
    while (left <= right) {
        const left_weight = people[left];
        const right_weight = people[right];
        
        if (left_weight + right_weight > limit) {
            right -= 1;
            boatCount += 1;
        } else {
            left += 1;
            right -= 1;
            boatCount += 1;
        }
    }
    return boatCount;
}