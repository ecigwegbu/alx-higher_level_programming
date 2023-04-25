#!/usr/bin/node
// safe a string to a file

const fs = require('fs');
const file = process.argv[2];
const string = process.argv[3];
fs.writeFile(file, string, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
