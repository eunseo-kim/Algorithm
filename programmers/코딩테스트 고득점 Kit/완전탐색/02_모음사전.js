/*
========================================================
언어 : Javascript
날짜 : 2022.7.27
문제 : 모음사전
레벨 : level 2
========================================================
*/

function wordDictionary() {
  const words = 'AEIOU'.split('');
  const dictionary = {};
  let index = 0;

  function dfs(word) {
    dictionary[word] = index;
    index += 1;

    if (word.length === 5) return;

    for (let i = 0; i < 5; i += 1) {
      dfs(word + words[i]);
    }
  }

  dfs('');
  return dictionary;
}

function solution(word) {
  const dictionary = wordDictionary();

  return dictionary[word];
}

const result = solution('AAAAE');
console.log(result);
