#!/usr/bin/node
// Prints characters

const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;

request(url, (err, res, body) => {
  if (err) console.log(err);
  const movie = JSON.parse(body);
  movie.characters.map(char_url => {
    request(char_url, (err, res, body) => {
      console.log(JSON.parse(body).name);
    });
  });
});
