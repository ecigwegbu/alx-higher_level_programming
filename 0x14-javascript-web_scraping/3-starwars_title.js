#!/usr/bin/node
// display title of a movie based on API

const request = require('request');
const id = parseInt(process.argv[2]);
const url = 'https://swapi-api.alx-tools.com/api/films/';
request(url, function (body, response) {
  const films = JSON.parse(response.body).results;
  const count = JSON.parse(response.body).count;
  for (let i = 0; i < count; i++) {
    if (films[i].episode_id === id) {
      console.log(films[i].title);
    }
  }
});
