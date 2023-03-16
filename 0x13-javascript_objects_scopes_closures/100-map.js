#!/usr/bin/node
// import an array and computes another new array

const list = require('./100-data').list;
const newList = list.map((elt, indx) => indx * elt);
console.log(list);
console.log(newList);
