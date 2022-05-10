// 누적합 문제
function solution(salaries, days) {
    var peopleCount = salaries.length;
    var salaryList = [];

    for (var i=0; i<peopleCount; i++) {
        var arr = []
        for (var j=0; j<=days; j++) {
            arr.push(0);
        }
        salaryList.push(arr);
    }


    // 누적합을 배열에 세팅하기
    for (var i=0; i<peopleCount; i++) {
        const salary = salaries[i];
        const gap = salary[0];
        const price = salary[1];

        for (var j=gap; j<=days; j+=gap) {
            salaryList[i][j] += price;
        }
        salaryList[i][days] = price;
    }

    // 계산하기
    var answer = 0;

    salaryList.forEach((salary) => {
        var sum = 0;
        for (var i=1; i<=days; i++) {
            sum = sum + salary[i];
        }
        answer += sum;
    })

    return answer;
}