#!/usr/bin/node
// return number of occurences in a list

// const letters = ["a", "b", "c", "a", "b", "c", "a", "b"];
// const count = {};
// letters.forEach(e => count[e] ? count[e]++ : count[e] = 1 );

// console.log(count)

exports.nbOccurences = function (list, searchElement) {
  if (!list || !searchElement) return (0);
  const count = {};
  list.forEach(e => count[e] ? count[e]++ : count[e] = 1 );
  return (count[searchElement]);
}
