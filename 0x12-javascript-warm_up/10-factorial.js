#!/usr/bin/node

const x = parseInt(process.argv[2]);

function factorial (a) {
  if (a === 0 || a === 1) {
    return 1;
  }
  return a * factorial(a - 1);
}
console.log(factorial(x));
