function solution(genres, plays) {
    const genrePlayCount = {};
    genres.forEach((genre, i) => {
        genrePlayCount[genre] ? genrePlayCount[genre] += plays[i] : genrePlayCount[genre] = plays[i];
    });
    
    const musicPlayer = [];
    genres.forEach((genre, i) => {
       musicPlayer.push([genrePlayCount[genre], plays[i], i]);
    });
    
    // sort
    musicPlayer.sort((a, b) => {
       if (a[0] == b[0]) {
           if (a[1] == b[1]) {
               return a[2] - b[2];
           } else {
               return b[1] - a[1];
           }
       } else {
           return b[0] - a[0];
       }
    });
    
    const player = {};
    const answer = [];
    musicPlayer.forEach(([genre, _, i]) => {
        player[genre] ? player[genre] += 1 : player[genre] = 1;
        if (player[genre] < 3) {
            answer.push(i);
        }
    });
    return answer;
}