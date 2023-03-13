#!/usr/bin/node

import { argv } from 'node:process';

console.log(argv[2] == null ? 'No argument' : argv[2]);
