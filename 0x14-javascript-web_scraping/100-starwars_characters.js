#!/usr/bin/node
// Prints characters

const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;

request(url, (err, res, body) => {
  if (err) console.log(err);
  const movie = JSON.parse(body);
  movie.characters.forEach(charUrl => {
    request(charUrl, (err, res, body) => {
      if (err) throw err;
      console.log(JSON.parse(body).name);
    });
  });
});
