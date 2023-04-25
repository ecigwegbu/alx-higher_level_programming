#!/usr/bin/node
// read and print a file

const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data.toString());
  }
});
