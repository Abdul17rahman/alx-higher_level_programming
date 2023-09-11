#!/usr/bin/node

const x = parseInt(process.argv[2]);

function add () {
  let fact = 1;
  for (let i = 1; i <= x; i++) {
    fact *= i;
  }
  console.log(fact);
}
add();
