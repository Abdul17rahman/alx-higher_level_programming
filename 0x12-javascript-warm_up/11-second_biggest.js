#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const value = process.argv.sort();
  console.log(value[process.argv.length - 2]);
}
