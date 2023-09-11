#!/usr/bin/node

const x = parseInt(process.argv[2]);

function factorial (a) {
  let fact = 1;
  for (i = 1; i <= a; i++) {
    fact *= i;
  }
  return fact;
}
console.log(factorial(x));
