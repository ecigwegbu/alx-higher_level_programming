#!/usr/bin/node

import { argv } from 'node:process';

// node script arg2 arg3
// console.log(argv.length);
let myVar;
if (argv[2] == null) {
  myVar = 'No argument';
} else if (argv[3] == null) {
  myVar = 'Argument found';
} else {
  myVar = 'Arguments found';
}
console.log(myVar);
