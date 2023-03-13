#!/usr/bin/node

import { argv } from 'node:process';

// node script arg2 arg3
// console.log(argv.length);
console.log(`${argv[2]} is ${argv[3]}`);
