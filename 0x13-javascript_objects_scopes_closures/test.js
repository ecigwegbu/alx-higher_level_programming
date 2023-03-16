#!/usr/bin/node

const letters = ["a", "b", "c", "a", "b", "c", "a", "b"];
const count = {};
letters.forEach(e => count[e] ? count[e]++ : count[e] = 1 );

console.log(count)
