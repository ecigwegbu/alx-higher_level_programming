#!/usr/bin/node
// display title of a movie based on API

const request = require('request');
const movieId = parseInt(process.argv[2]);
const url = 'https://swapi-api.alx-tools.com/api/films/';
request(url, function (body, response) {
  const film = JSON.parse(response.body).results[movieId - 1];
  //  console.log(film);
  for (var ch = 0; ch < film.characters.length; ch++) {
    async function getData() {
      await request(film.characters[ch], function (body, response) {
      console.log((JSON.parse(response.body)).name);
      })
    } getData();
  }
});
