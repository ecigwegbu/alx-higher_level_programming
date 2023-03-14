#!/usr/bin/node
// Add 2 integers

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);
function add (a, b) {
  // console.log(a);
  // console.log(b);
  if (isNaN(a) || isNaN(b)) {
    return (NaN);
  } else {
    return (a + b);
  }
}
console.log(add(a, b));
