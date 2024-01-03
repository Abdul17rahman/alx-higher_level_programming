#!/usr/bin/node
/// Read content of a file

const fs = require('fs');

const path = process.argv[2];

fs.readFile(path, 'utf-8', (err, data) => {
  if (err) console.log(err);
  console.log(data);
});
