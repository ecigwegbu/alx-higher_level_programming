#!/usr/bin/node
// Compute the second biggest argument

// get biggest
let max = parseInt(process.argv[2]);
for (let i = 2; i < parseInt(process.argv.length); i++) {
  if (parseInt(process.argv[i]) > max) max = parseInt(process.argv[i]);
}

// get second biggest
let secondMax = parseInt(process.argv[2]);
for (let i = 2; i < parseInt(process.argv.length); i++) {
  if (parseInt(process.argv[i]) > secondMax &&
      parseInt(process.argv[i]) !== max) secondMax = parseInt(process.argv[i]);
}
console.log(secondMax);
