#!/usr/bin/node
// import an array and computes another new array

const list = require('./100-data').list;
const newList = list.map(x => (list.indexOf(x) * x));
console.log(list);
console.log(newList);
