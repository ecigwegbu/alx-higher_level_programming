#!/usr/bin/node
// print a square

const arg = parseInt(process.argv[2]);
let square = '';
if (isNaN(arg)) {
  console.log('Missing size');
} else if (arg >= 0) {
  for (let i = 0; i < arg; i++) { // build one line
    square += 'X';
  }
  for (let j = 0; j < arg; j++) { // output several lines
    console.log(square);
  }
}
