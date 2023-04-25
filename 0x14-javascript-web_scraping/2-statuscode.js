#!/usr/bin/node
// display status code after GET request

const request = require('request');
const url = process.argv[2];
request(url, function (body, response) {
  console.log(`code: ${response && response.statusCode}`);
});
