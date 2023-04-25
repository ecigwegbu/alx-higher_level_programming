#!/usr/bin/node

// import { argv } from 'node:process';

let myVar;
if (process.argv[2] == null) {
  myVar = 'No argument';
} else if (process.argv[3] == null) {
  myVar = 'Argument found';
} else {
  myVar = 'Arguments found';
}
console.log(myVar);
