#!/usr/bin/node
// read and write files

const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

console.log(fileA);
console.log(fileB);

// Use fs.readFile() method to read fileA
fs.readFile('fileA', 'utf8', function (err, data) {
  if (err) throw err;
  // save file contents to fileC
  fs.writeFile('fileC', data, function (err) {
    if (err) throw err;
    // Use fs.readFile() method to read fileB
    fs.readFile('fileB', 'utf8', function (err, data) {
      if (err) throw err;
      // append file contents to fileC
      fs.appendFile('fileC', data, function (err) {
        if (err) throw err;
      });
    });
  });
});
console.log(fileC);
