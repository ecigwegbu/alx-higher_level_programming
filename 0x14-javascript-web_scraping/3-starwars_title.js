#!/usr/bin/node
// display title of a movie based on API

const request = require('request');
const id = parseInt(process.argv[2]);
const url = 'https://swapi-api.alx-tools.com/api/films/';
request(url, function (body, response) {
  const films = JSON.parse(response.body).results;
  console.log(films[id - 1].title);
});
