#!/usr/bin/node

const num = parseInt(process.argv[2]);

if (!num) { console.log('Not a number'); } else { console.log(`My number: ${num}`); }
