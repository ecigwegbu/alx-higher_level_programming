#!/usr/bin/node
// prints the number of movies where the character “Wedge Antilles” is present

const request = require('request');
const url = process.argv[2];
request(url, function (body, response) {
  const films = JSON.parse(response.body).results;
  const moviesCount = JSON.parse(response.body).count;
  let numMovies = 0;
  for (let i = 0; i < moviesCount; i++) {
    if (films[i].characters.indexOf('https://swapi-api.alx-tools.com/api/people/18/') !== -1) {
      numMovies++;
    }
  }
  console.log(numMovies);
}
);
