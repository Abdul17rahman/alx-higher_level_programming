#!/usr/bin/node

const list = require('./100-data').list;

console.log(list);
function comp () {
  return list.map((a, idx) => (a * idx));
}
console.log(comp());
