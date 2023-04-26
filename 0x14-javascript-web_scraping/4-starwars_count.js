#!/usr/bin/node
// display title of a movie based on API

const request = require('request');
const url = process.argv[2];
request(url, function (body, response) {
  const films = JSON.parse(response.body).results;
  const count = JSON.parse(response.body).count;
  let numMovies = 0;
  for (let i = 0; i < count; i++) {
    for (let j = 0; j < (films[i].characters.length); j++) {
      const mychar = films[i].characters[j];
      if (mychar.includes('18')) {
        numMovies++;
      }
    }
  }
  console.log(numMovies);
}
);
