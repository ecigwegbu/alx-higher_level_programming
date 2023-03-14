#!/usr/bin/node
// Compute the second biggest argument

// Edge cases first
let max = parseInt(process.argv[2]);
let secondMax = Number.MIN_SAFE_INTEGER;
if (process.argv.length <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < parseInt(process.argv.length); i++) {
    if (parseInt(process.argv[i]) > max) max = parseInt(process.argv[i]);
  }
  // console.log('Max: ', max);
  for (let i = 2; i < parseInt(process.argv.length); i++) {
    if (parseInt(process.argv[i]) > secondMax &&
        parseInt(process.argv[i]) !== max) secondMax = parseInt(process.argv[i]);
  }
  console.log(secondMax);
}
