#!/usr/bin/node

if (process.argv.length <= 3) { console.log(0); } else {
  console.log(process.argv.sort((x, y) => y - x).slice(3)[0]);
}
