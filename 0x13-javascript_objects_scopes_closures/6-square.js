#!/usr/bin/node

const newSqr = require('./5-square');

module.exports = class Square extends newSqr {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    let myChar = '';
    for (let i = 0; i < this.height; i++) {
      myChar = '';
      for (let j = 0; j < this.width; j++) {
        myChar += c
      }
      console.log(myChar);
    }
  }
};
