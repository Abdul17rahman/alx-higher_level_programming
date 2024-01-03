#!/usr/bin/node
/// Read content of a file

const request = require('request');

const id = parseInt(process.argv[2]);

request(`https://swapi-api.alx-tools.com/api/films/${id}`, (err, res, body) => {
  if (err) console.log(err);
  console.log(JSON.parse(body).title);
});
