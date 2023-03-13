#!/usr/bin/node

import { argv } from 'node:process';

const myVar = argv[2];
if (myVar == null) {
  console.log('No argument');
} else {
  console.log(myVar);
}
