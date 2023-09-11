#!/usr/bin/node

if (process.argv.length <= 2) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  const arg = process.argv[2];
  console.log(arg);
}
