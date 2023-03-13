#!/usr/bin/node

import { argv } from 'node:process';

// console.log(argv.length);
let myVar;
if (argv.length === 2) {
  myVar = 'No argument';
} else if (argv.length === 3) {
  myVar = 'Argument found';
} else {
  myVar = 'Arguments found';
}
console.log(myVar);
