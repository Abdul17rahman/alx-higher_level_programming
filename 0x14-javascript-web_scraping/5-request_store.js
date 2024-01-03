#!/usr/bin/node
// Get Movies where char is Wedge

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const path = process.argv[3];

request(url, (err, res, body) => {
  if (err) console.log(err);
  fs.writeFile(path, body, 'utf-8', (er) => {
    if (er) console.log(er);
  });
});
