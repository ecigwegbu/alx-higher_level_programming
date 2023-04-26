#!/usr/bin/node
// safe a string to a file

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const file = process.argv[3];
let page;

request(url, function (body, response) {
  page = response.body;

  fs.writeFile(file, page, 'utf8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
