#!/usr/bin/node
// import an array and computes another new array

const dict = require('./100-data').dict;
const newDict = Object.keys(dict).map(key => `${dict[key]}: ${key}`);
console.log(dict);
console.log(newDict);
