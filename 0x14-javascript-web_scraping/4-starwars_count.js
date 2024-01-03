#!/usr/bin/node
// Get Movies where char is Wedge

const request = require('request');

const url = process.argv[2];
if (!url) process.exit();

request(url, (err, res, body) => {
  if (err) console.log(err);
  const movies = JSON.parse(body);
  const wedge = movies.results.filter(m => {
    return m.characters.includes('https://swapi-api.alx-tools.com/api/people/18/');
  });
  console.log(wedge.length);
});
